import os
import pathlib
import xml.etree.ElementTree
from datetime import datetime
from typing import Union
from xml.etree import ElementTree as ET

import bioformats as bf
import javabridge
import numpy as np
import pandas as pd

from fileops.image import to_8bit
from fileops.image.imagemeta import MetadataImageSeries, MetadataImage
from fileops.logger import get_logger
from fileops.pathutils import ensure_dir


def create_jvm():
    log = get_logger(name='create_jvm')
    log.debug("Starting javabridge JVM to be used by the bioformats package.")
    log.debug("Limit 1G for heap.")

    javabridge.start_vm(class_path=bf.JARS, max_heap_size="1G", run_headless=True)
    env = javabridge.attach()

    # Forbid Javabridge to spill out DEBUG messages during runtime from CellProfiler/python-bioformats.
    root_logger_name = javabridge.get_static_field("org/slf4j/Logger",
                                                   "ROOT_LOGGER_NAME",
                                                   "Ljava/lang/String;")
    root_logger = javabridge.static_call("org/slf4j/LoggerFactory",
                                         "getLogger",
                                         "(Ljava/lang/String;)Lorg/slf4j/Logger;",
                                         root_logger_name)
    log_level = javabridge.get_static_field("ch/qos/logback/classic/Level",
                                            "WARN",
                                            "Lch/qos/logback/classic/Level;")
    javabridge.call(root_logger,
                    "setLevel",
                    "(Lch/qos/logback/classic/Level;)V",
                    log_level)

    return env


class ImageFile:
    log = get_logger(name='ImageFile')

    def __init__(self, image_path: Union[str, pathlib.Path], image_series=0, failover_dt=1, **kwargs):
        self.image_path = image_path.as_posix() if type(image_path) == pathlib.Path else os.path.abspath(image_path)
        self.base_path = os.path.dirname(self.image_path)
        self.render_path = os.path.join(self.base_path, 'out', 'render')
        self.metadata_path = None
        self.failover_dt = failover_dt
        self.log.debug(f"Image file path is {self.image_path.encode('ascii')}.")

        ensure_dir(self.render_path)

        self._series = image_series
        self.all_series = []
        self.instrument_md = []
        self.objectives_md = []

        self._info = None
        self.md = None
        self.images_md = None
        self.planes_md = None
        self.all_planes = []
        self.all_planes_md_dict = {}

        self.timestamps = []  # list of all timestamps recorded in the experiment
        self.time_interval = None  # average time difference between frames
        self.channels = []  # list of channels that the acquisition took
        self.zstacks = []  # list of focal planes acquired
        self.frames = []  # list of timepoints recorded
        self.files = []  # list of filenames that the measurement extends to
        self.n_channels = 0
        self.n_zstacks = 0
        self.n_frames = 0
        self.magnification = None  # integer storing the magnitude of the lens
        self.um_per_pix = None  # calibration assuming square pixels
        self.pix_per_um = None  # calibration assuming square pixels
        self.um_per_z = None  # distance step of z axis
        self.width = None
        self.height = None
        self.all_planes_md_dict = {}
        self._load_imageseries()

        if self.timestamps is not None:
            self.time_interval = failover_dt
            self.timestamps = [failover_dt * f for f in self.frames]

    @staticmethod
    def has_valid_format(path: str):
        pass

    @property
    def info(self) -> pd.DataFrame:
        return pd.DataFrame()

    @property
    def series(self):
        return self.all_series[self._series]

    @series.setter
    def series(self, s):
        self._load_imageseries()

    def ix_at(self, c, z, t):
        czt_str = f"{c:0{len(str(self.n_channels))}d}{z:0{len(str(self.n_zstacks))}d}{t:0{len(str(self.n_frames))}d}"
        if czt_str in self.all_planes_md_dict:
            return self.all_planes_md_dict[czt_str]
        self.log.warning(f"No index found for c={c}, z={z}, and t={t}.")

    def image(self, *args, **kwargs) -> MetadataImage:
        if len(args) == 1 and isinstance(args[0], int):
            ix = args[0]
            plane = self.all_planes[ix]
            return self._image(plane, row=0, col=0, fid=0)

    def image_series(self, channel='all', zstack='all', frame='all', as_8bit=False) -> MetadataImageSeries:
        images = list()
        frames = self.frames if frame == 'all' else [frame]
        zstacks = self.zstacks if zstack == 'all' else [zstack]
        channels = self.channels if channel == 'all' else [channel]

        for t in frames:
            for zs in zstacks:
                for ch in channels:
                    ix = self.ix_at(ch, zs, t)
                    plane = self.all_planes[ix]
                    img = self._image(plane).image
                    images.append(to_8bit(img) if as_8bit else img)
        images = np.asarray(images).reshape((len(frames), len(zstacks), len(channels), *images[-1].shape))
        return MetadataImageSeries(images=images, pix_per_um=self.pix_per_um, um_per_pix=self.um_per_pix,
                                   frames=len(frames), timestamps=len(frames),
                                   time_interval=None,  # self.time_interval,
                                   channels=len(channels), zstacks=len(zstacks),
                                   width=self.width, height=self.height,
                                   series=None, intensity_ranges=None)

    def _load_imageseries(self):
        pass

    def _image(self, plane, row=0, col=0, fid=0) -> MetadataImage:
        raise NotImplementedError

    def _get_metadata(self):
        pass

    def z_projection(self, frame: int, channel: int, projection='max', as_8bit=False):
        images = list()
        zstacks = self.zstacks

        for zs in zstacks:
            ix = self.ix_at(channel, zs, frame)
            plane = self.all_planes[ix]
            img = self._image(plane).image
            images.append(to_8bit(img) if as_8bit else img)

        im_vol = np.asarray(images).reshape((len(zstacks), *images[-1].shape))
        im_proj = np.max(im_vol, axis=0)
        return MetadataImage(reader='MaxProj',
                             image=im_proj,
                             pix_per_um=self.pix_per_um, um_per_pix=self.um_per_pix,
                             frame=frame, timestamp=None, time_interval=None,
                             channel=channel, z=None,
                             width=self.width, height=self.height,
                             intensity_range=[np.min(im_proj), np.max(im_proj)])


ome_fields = {
    "T":            "FirstT",
    "C":            "FirstC",
    "Z":            "FirstZ",
    "N_T":          "SizeT",
    "N_C":          "SizeC",
    "N_Z":          "SizeZ",
    "width":        "SizeX",
    "height":       "SizeY",
    "um_per_pix_X": "PhysicalSizeX",
    "um_per_pix_Y": "PhysicalSizeY",
    "DeltaT":       "DeltaT",
}


class OMEImageFile(ImageFile):
    ome_ns = {'ome': 'http://www.openmicroscopy.org/Schemas/OME/2016-06'}
    log = get_logger(name='OMEImageFile')

    def __init__(self, image_path: Union[str, pathlib.Path], jvm=None, **kwargs):
        super().__init__(image_path, **kwargs)

        self._jvm = jvm
        self._rdr: bf.ImageReader = None

        self.md, self.md_xml = self._get_metadata()
        self.all_series = self.md.findall('ome:Image', self.ome_ns)
        self.instrument_md = self.md.findall('ome:Instrument', self.ome_ns)
        self.objectives_md = self.md.findall('ome:Instrument/ome:Objective', self.ome_ns)

        self._load_imageseries()

        if not self.timestamps:
            self.time_interval = self.failover_dt
            self.timestamps = [self.failover_dt * f for f in self.frames]

    @property
    def info(self) -> pd.DataFrame:
        fname_stat = pathlib.Path(self.image_path).stat()
        fcreated = datetime.fromtimestamp(fname_stat.st_ctime).strftime("%a %b/%d/%Y, %H:%M:%S")
        fmodified = datetime.fromtimestamp(fname_stat.st_mtime).strftime("%a %b/%d/%Y, %H:%M:%S")
        series_info = list()
        for imageseries in self.md.findall('ome:Image', self.ome_ns):  # iterate through all series
            instrument = imageseries.find('ome:InstrumentRef', self.ome_ns)
            obj_id = imageseries.find('ome:ObjectiveSettings', self.ome_ns).get('ID')
            objective = self.md.find(f'ome:Instrument/ome:Objective[@ID="{obj_id}"]', self.ome_ns)
            imgseries_pixels = imageseries.findall('ome:Pixels', self.ome_ns)
            for isr_pixels in imgseries_pixels:
                size_x = float(isr_pixels.get('PhysicalSizeX'))
                size_y = float(isr_pixels.get('PhysicalSizeY'))
                size_z = float(isr_pixels.get('PhysicalSizeZ'))
                size_x_unit = isr_pixels.get('PhysicalSizeXUnit')
                size_y_unit = isr_pixels.get('PhysicalSizeYUnit')
                size_z_unit = isr_pixels.get('PhysicalSizeZUnit')
                timestamps = sorted(
                    np.unique([p.get('DeltaT') for p in isr_pixels.findall('ome:Plane', self.ome_ns) if
                               p.get('DeltaT') is not None]).astype(np.float64))
                series_info.append({
                    'filename':                          os.path.basename(self.image_path),
                    'image_id':                          imageseries.get('ID'),
                    'image_name':                        imageseries.get('Name'),
                    'instrument_id':                     instrument.get('ID'),
                    'pixels_id':                         isr_pixels.get('ID'),
                    'channels':                          int(isr_pixels.get('SizeC')),
                    'z-stacks':                          int(isr_pixels.get('SizeZ')),
                    'frames':                            int(isr_pixels.get('SizeT')),
                    'delta_t':                           float(np.nanmean(np.diff(timestamps))),
                    # 'timestamps': timestamps,
                    'width':                             self.width,
                    'height':                            self.height,
                    'data_type':                         isr_pixels.get('Type'),
                    'objective_id':                      obj_id,
                    'magnification':                     int(float(objective.get('NominalMagnification'))),
                    'pixel_size':                        (size_x, size_y, size_z),
                    'pixel_size_unit':                   (size_x_unit, size_y_unit, size_z_unit),
                    'pix_per_um':                        (1 / size_x, 1 / size_y, 1 / size_z),
                    'change (Unix), creation (Windows)': fcreated,
                    'most recent modification':          fmodified,
                })
        out = pd.DataFrame(series_info)
        return out

    @property
    def series(self):
        return self.all_series[self._series]

    @series.setter
    def series(self, s):
        if type(s) == int:
            self._series = s
        elif type(s) == str:
            for k, imser in enumerate(self.all_series):
                if imser.attrib['Name'] == s:
                    self._series = k
                    break
        elif type(s) == xml.etree.ElementTree.Element:
            for k, imser in enumerate(self.all_series):
                if imser.attrib == s.attrib:
                    self._series = k
                    break
        else:
            raise ValueError("Unexpected type of variable to load series.")

        super().__init__(s)

    def _load_imageseries(self):
        if not self.all_series:
            return
        self.images_md = self.all_series[self._series]
        self.planes_md = self.images_md.find('ome:Pixels', self.ome_ns)
        self.all_planes = self.planes_md.findall(f'{{{self.ome_ns["ome"]}}}TiffData', self.ome_ns)
        # self.all_planes = self.planes_md.findall(f'TiffData', self.ome_ns)

        self.channels = sorted(np.unique([p.get('FirstC') for p in self.all_planes]).astype(int))
        self.zstacks = sorted(np.unique([p.get('FirstZ') for p in self.all_planes]).astype(int))
        self.frames = sorted(np.unique([p.get('FirstT') for p in self.all_planes]).astype(int))
        self.n_channels = int(self.planes_md.get('SizeC'))
        self.n_zstacks = int(self.planes_md.get('SizeZ'))
        self.n_frames = int(self.planes_md.get('SizeT'))
        self.um_per_pix = float(self.planes_md.get('PhysicalSizeX')) if \
            self.planes_md.get('PhysicalSizeX') == self.planes_md.get('PhysicalSizeY') else np.nan
        self.pix_per_um = 1. / self.um_per_pix
        self.width = int(self.planes_md.get('SizeX'))
        self.height = int(self.planes_md.get('SizeY'))
        self.um_per_z = float(self.planes_md.get('PhysicalSizeZ')) if self.planes_md.get('PhysicalSizeZ') else np.nan

        obj = self.images_md.find('ome:ObjectiveSettings', self.ome_ns)
        obj_id = obj.get('ID') if obj else None
        objective = self.md.find(f'ome:Instrument/ome:Objective[@ID="{obj_id}"]', self.ome_ns) if obj else None
        self.magnification = int(float(objective.get('NominalMagnification'))) if objective else None

        self.timestamps = sorted(
            np.unique([p.get('DeltaT') for p in self.all_planes if p.get('DeltaT') is not None]).astype(np.float64))
        self.time_interval = np.mean(np.diff(self.timestamps))

        # build dictionary where the keys are combinations of c z t and values are the index
        self.all_planes_md_dict = {f"{int(plane.get('FirstC')):0{len(str(self.n_channels))}d}"
                                   f"{int(plane.get('FirstZ')):0{len(str(self.n_zstacks))}d}"
                                   f"{int(plane.get('FirstT')):0{len(str(self.n_frames))}d}": i
                                   for i, plane in enumerate(self.all_planes)}

        self.log.info(f"Image series {self._series} loaded. "
                      f"Image size (WxH)=({self.width:d}x{self.height:d}); "
                      f"calibration is {self.pix_per_um:0.3f} pix/um and {self.um_per_z:0.3f} um/z-step; "
                      f"movie has {self.n_frames} frames, {self.n_channels} channels, {self.n_zstacks} z-stacks and "
                      f"{len(self.all_planes)} image planes in total.")

    def _lazy_load_jvm(self):
        if not self._jvm:
            self._jvm = create_jvm()
        if not self._rdr:
            self._rdr = bf.ImageReader(self.image_path, perform_init=True)

    def _image(self, plane, row=0, col=0, fid=0) -> MetadataImage:  # PLANE HAS METADATA INFO OF THE IMAGE PLANE
        c, z, t = plane.get('FirstC'), plane.get('FirstZ'), plane.get('FirstT')
        # logger.debug('retrieving image id=%d row=%d col=%d fid=%d' % (_id, row, col, fid))
        self._lazy_load_jvm()

        image = self._rdr.read(c=c, z=z, t=t, series=self._series, rescale=False)
        bf.clear_image_reader_cache()

        w = int(self.planes_md.get('SizeX'))
        h = int(self.planes_md.get('SizeY'))

        return MetadataImage(reader='OME',
                             image=image,
                             pix_per_um=1. / self.um_per_pix, um_per_pix=self.um_per_pix,
                             time_interval=None,
                             timestamp=float(plane.get('DeltaT')) if plane.get('DeltaT') is not None else 0.0,
                             frame=int(t), channel=int(c), z=int(z), width=w, height=h,
                             intensity_range=[np.min(image), np.max(image)])

    def _get_metadata(self):
        self._lazy_load_jvm()

        md_xml = bf.get_omexml_metadata(self.image_path)
        md = ET.fromstring(md_xml.encode("utf-8"))

        return md, md_xml
