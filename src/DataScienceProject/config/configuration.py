from src.DataScienceProject.constants import *
from src.DataScienceProject.utils.common import read_yaml , create_directories
import zipfile
from src.DataScienceProject.entity.config_entity import (DataIngestionConfig)

class ConfigurationManager:
  def __init__(self , config_filepath=CONFIG_FILE_PATH , params_filepath=PARAMS_FILE_PATH , schema_filepath=SCHEMA_FILE_PATH):
    self.config = read_yaml(config_filepath)
    self.params = read_yaml(params_filepath)
    self.schema = read_yaml(schema_filepath)
    
    create_directories([self.config.artifacts_root])
  # downloading the zip file
  def data_ingestion_config(self) -> DataIngestionConfig:
    config = self.config.data_ingetion
    create_directories([config.root_dir])
    data_ingestion_config = DataIngestionConfig(
      root_dir = config.root_dir,
      source_URL = config.source_URL,
      local_data_file = config.local_data_file,
      unzip_dir = config.unzip_dir
    )
    
    return data_ingestion_config
  
  def extract_zip_file(self , zip_file_path:Path , unzip_dir:Path):
    with zipfile.ZipFile(zip_file_path , 'r') as zip_ref:
      zip_ref.extractall(unzip_dir)
    