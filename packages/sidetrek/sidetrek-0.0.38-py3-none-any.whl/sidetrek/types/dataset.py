from typing import Dict
from dataclasses import dataclass
from dataclasses_json import dataclass_json
from torchdata.datapipes.iter import IterDataPipe
from torchdata.datapipes.map import MapDataPipe


@dataclass_json
@dataclass
class FsspecOptions:
    kwargs_for_open: Dict
    storage_kwargs: Dict


@dataclass_json
@dataclass
class SidetrekDatasetOptions:
    fsspec: FsspecOptions


@dataclass_json
@dataclass
class SidetrekDataset:
    io: str
    source: str
    options: Dict  # change to SidetrekDatasetOptions later


SidetrekIterDataPipe = IterDataPipe
SidetrekMapDataPipe = MapDataPipe
