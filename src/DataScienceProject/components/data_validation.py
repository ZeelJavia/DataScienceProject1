from src.DataScienceProject import logger
from src.DataScienceProject.utils.common import read_yaml , create_directories
from src.DataScienceProject.constants import *
from src.DataScienceProject.entity.config_entity import (DataValidationConfig)
from src.DataScienceProject.config.configuration import ConfigurationManager
import pandas as pd
import os


class DataValidation:
  def __init__(self , config:DataValidationConfig):
    self.config = config
  
  def validate_all_columns(self)->bool:
    try:
      validate_status = None
      data = pd.read_csv(self.config.unzip_data_dir)
      all_columns = list(data.columns)
      all_schema = self.config.all_schema
      for column in all_columns:
        if column not in all_schema:
          validate_status = False
          with open(self.config.STATUS_FILE , "w") as f:
            f.write(f"Validation status : {validate_status} ")
        else:
          validate_status = True
          with open(self.config.STATUS_FILE , "w") as f:
            f.write(f"Validation status : {validate_status} ")
      return validate_status
    except Exception as e:
      raise e