from src.DataScienceProject import logger
from src.DataScienceProject.pipeline.data_ingetion_pipeline import DataIngetionTrainingPipeline

STAGE_NAME = 'Data Ingetion Stage'

try:
  logger.info(f"{'>>'*20} {STAGE_NAME} {'<<'*10}")
  data_ingetion = DataIngetionTrainingPipeline()
  data_ingetion.initiate_data_ingestion()
  logger.info(f"{'>>'*20} {STAGE_NAME} {'<<'*10}")
except Exception as e:
  logger.exception(e)
  