from src.DataScienceProject import logger
from src.DataScienceProject.pipeline.data_ingetion_pipeline import DataIngetionTrainingPipeline
from src.DataScienceProject.pipeline.data_transformation_pipeline import DataTransformationTrainingPipeline
from src.DataScienceProject.pipeline.data_validation_pipeline import DataValidationTrainingPipeline

STAGE_NAME = 'Data Ingetion Stage'

try:
  logger.info(f"{'>>'*20} {STAGE_NAME} {'<<'*10}")
  data_ingetion = DataIngetionTrainingPipeline()
  data_ingetion.initiate_data_ingestion()
  logger.info(f"{'>>'*20} {STAGE_NAME} {'<<'*10}")
except Exception as e:
  logger.exception(e)
  
STAGE_NAME = 'Data Validation Stage'

try:
  logger.info(f"{'>>'*20} {STAGE_NAME} {'<<'*10}")
  data_validation = DataValidationTrainingPipeline()
  data_validation.initiate_data_validation()
  logger.info(f"{'>>'*20} {STAGE_NAME} {'<<'*10}")
except Exception as e:
  logger.exception(e)
  
STAGE_NAME = 'Data Transformation Stage'

try:
  logger.info(f"{'>>'*20} {STAGE_NAME} {'<<'*10}")
  data_transformation = DataTransformationTrainingPipeline()
  data_transformation.initiate_data_transformation()
  logger.info(f"{'>>'*20} {STAGE_NAME} {'<<'*10 }")
except Exception as e:
  logger.exception(e) 