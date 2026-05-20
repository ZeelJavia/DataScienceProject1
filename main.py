from src.DataScienceProject import logger
from src.DataScienceProject.components.model_traine import ModelTrainer
from src.DataScienceProject.config.configuration import ConfigurationManager
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
  
STAGE_NAME = 'Model Trainer Stage'

try:
  config = ConfigurationManager()
  model_trainer_config = config.get_model_trainer_config()
  model_trainer_config = ModelTrainer(config=model_trainer_config)
  model_trainer_config.train_model()
except Exception as e:
  logger.exception(e)