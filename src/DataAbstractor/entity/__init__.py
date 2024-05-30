from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    # with respect to config.yaml
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path