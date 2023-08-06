from typing import Dict
from dataclasses import dataclass
from torchdata.datapipes.iter import IterDataPipe
from torchdata.datapipes.map import MapDataPipe


@dataclass
class FsspecOptions:
    kwargs_for_open: Dict
    storage_kwargs: Dict


@dataclass
class SidetrekDatasetOptions:
    fsspec: FsspecOptions


@dataclass
class SidetrekDataset:
    io: str
    source: str
    options: Dict  # change to SidetrekDatasetOptions later


SidetrekIterDataPipe = IterDataPipe
SidetrekMapDataPipe = MapDataPipe
