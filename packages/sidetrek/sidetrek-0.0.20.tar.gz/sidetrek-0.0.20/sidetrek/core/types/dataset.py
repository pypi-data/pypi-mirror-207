from typing import TypedDict, Dict
from torchdata.datapipes.iter import IterDataPipe
from torchdata.datapipes.map import MapDataPipe


class FsspecOptions(TypedDict):
    kwargs_for_open: Dict
    storage_kwargs: Dict


class SidetrekDatasetOptions(TypedDict):
    fsspec: FsspecOptions


class SidetrekDataset(TypedDict):
    io: str
    source: str
    options: Dict  # change to SidetrekDatasetOptions later


SidetrekIterDataPipe = IterDataPipe
SidetrekMapDataPipe = MapDataPipe
