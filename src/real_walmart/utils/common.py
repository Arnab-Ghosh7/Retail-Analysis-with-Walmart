import os
import yaml
from box.exceptions import BoxValueError
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

from real_walmart.logging import logger



@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Reads a YAML file and returns its content as a ConfigBox.

    Args:
        path_to_yaml (Path): Path to the YAML file

    Raises:
        ValueError: If the YAML file is empty
        Exception: For any other file-related issues

    Returns:
        ConfigBox: Parsed YAML content
    """
    try:
        with open(path_to_yaml, "r") as yaml_file:
            content = yaml.safe_load(yaml_file)
            if content is None:
                raise BoxValueError("YAML file is empty")

            logger.info(f"YAML file loaded successfully: {path_to_yaml}")
            return ConfigBox(content)

    except BoxValueError:
        raise ValueError("YAML file is empty")

    except Exception as e:
        raise e


@ensure_annotations
def create_directories(path_to_directories: list, verbose: bool = True):
    """
    Create directories from a list of paths.

    Args:
        path_to_directories (list): List of directory paths
        verbose (bool): Whether to log directory creation
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory at: {path}")


@ensure_annotations
def get_size(path: Path) -> str:
    """
    Get file size in KB.

    Args:
        path (Path): Path to the file

    Returns:
        str: File size in KB
    """
    size_in_kb = round(os.path.getsize(path) / 1024)
    return f"~ {size_in_kb} KB"
