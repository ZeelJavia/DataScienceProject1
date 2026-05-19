from src.DataScienceProject.config.configuration import ConfigurationManager
from src.DataScienceProject.components.data_ingetion import DataIngetion
from src.DataScienceProject import logger

STAGE_NAME = "Data Ingetion Stage"

class DataIngetionTrainingPipeline:
  def __init__(self):
    pass
  
  def initiate_data_ingestion(self):
      config=ConfigurationManager()
      data_ingestion_config = config.data_ingestion_config()
      data_ingestion = DataIngetion(config=data_ingestion_config)
      data_ingestion.download_self()
      data_ingestion.extract_zip_file( zip_file_path=data_ingestion_config.local_data_file , unzip_dir=data_ingestion_config.unzip_dir)

if __name__ == "__main__":
  try:
    logger.info(f"{'>>'*20} {STAGE_NAME} {'<<'*20}")
    data_ingetion = DataIngetionTrainingPipeline()
    data_ingetion.initiate_data_ingestion()
  except Exception as e:
    logger.exception(e)