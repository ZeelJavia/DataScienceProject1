from src.DataScienceProject.config.configuration import ConfigurationManager
from src.DataScienceProject.components.data_validation import DataValidation
from src.DataScienceProject import logger
from src.DataScienceProject.components.model_traine import ModelTrainer
STAGE_NAME = "Data Validation Stage"

class ModelTrainerPipeline:
  def __init__(self):
    pass
  
  def initiate_model_trainer(self):
      config=ConfigurationManager()
      model_trainer_config = config.get_model_trainer_config()
      model_trainer = ModelTrainer(config=model_trainer_config)
      model_trainer.train_model()
      logger.info(f"Model training completed successfully")