import urllib.request as request
from src.DataScienceProject import logger
import os 
import zipfile
from src.DataScienceProject.utils.common import read_yaml , create_directories
from src.DataScienceProject.constants import *
from src.DataScienceProject.entity.config_entity import (DataIngestionConfig)
from src.DataScienceProject.config.configuration import ConfigurationManager

# Component
class DataIngetion:
  def __init__(self , config: DataIngestionConfig):
    self.config = config
  
  def download_self(self):
    if not os.path.exists(self.config.local_data_file):
      filename , headers = request.urlretrieve(url=self.config.source_URL , filename=self.config.local_data_file)
      logger.info(f"File is downloaded at location {filename} with info {headers}")
    else:
      print(f"File already exists of path {self.config.local_data_file}")
  
  def extract_zip_file(self , zip_file_path:Path , unzip_dir:Path):
    with zipfile.ZipFile(zip_file_path , 'r') as zip_ref:
      zip_ref.extractall(unzip_dir)
  
