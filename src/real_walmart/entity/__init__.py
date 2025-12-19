from dataclasses import dataclass
from pathlib import Path
from typing import List


@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path

# ===============================
# Data Validation
# ===============================
@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    status_file: Path
    required_columns: List[str]


# ===============================
# Data Transformation
# ===============================
@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path
    train_data_path: Path
    test_data_path: Path


# ===============================
# Model Trainer
# ===============================
@dataclass(frozen=True)
class ModelTrainerConfig:
    root_dir: Path
    model_name: str


# ===============================
# Model Evaluation
# ===============================
@dataclass(frozen=True)
class ModelEvaluationConfig:
    root_dir: Path
    metric_file_name: Path
