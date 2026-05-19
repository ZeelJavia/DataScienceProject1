import os 
from numpy.testing import verbose
import yaml
from src.DataScienceProject import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
from box.exceptions import BoxValueError

@ensure_annotations
def read_yaml(path_to_yaml:Path)->ConfigBox:
  """Reads yaml files and returns

  Args:
      path_to_yaml (Path): path like input

  Raises:
      ValueError: If the yaml file is empty
      e: empty yaml file
  Returns:
      ConfigBox: config box type
  """
  
  try:
    with open(path_to_yaml) as yaml_file:
      content = yaml.safe_load(yaml_file)
      logger.info(f"yaml file: {path_to_yaml} loaded successfully")
      return ConfigBox(content)
  except BoxValueError:
    raise ValueError("yaml file is empty")
  except Exception as e:
    raise e

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
  """create list of directories
  Args:
  path_to_directories (list): list of path of directories
  ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to
  """
  for path in path_to_directories:
    os.makedirs(path, exist_ok=True)
    if verbose:
      logger.info(f"created directory at: {path}")

@ensure_annotations
def save_json(path: Path, data: dict):
  """save json data

  Args:
      path (Path): path to json file
      data (dict): data to be saved in json file
  """
  with open(path, "w") as f:
    json.dump(data, f, indent=4)
  logger.info(f"json file saved at: {path}")

@ensure_annotations
def load_json(path: Path) -> ConfigBox:
  """load json data

  Args:
      path (Path): path to json file

  Returns:
      ConfigBox: data loaded from json file
  """
  with open(path) as f:
    data = json.load(f)
  logger.info(f"json file loaded from: {path}")
  return ConfigBox(data)

@ensure_annotations
def save_bin(data: Any, path: Path):
  """save binary data

  Args:
      data (Any): data to be saved in binary file
      path (Path): path to binary file
  """
  joblib.dump(data, path)
  logger.info(f"binary file saved at: {path}")

@ensure_annotations
def load_bin(path: Path) -> Any:
  """load binary data

  Args:
      path (Path): path to binary file

  Returns:
      Any: data loaded from binary file
  """
  data = joblib.load(path)
  logger.info(f"binary file loaded from: {path}")
  return data