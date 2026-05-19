from src.DataScienceProject.config.configuration import ConfigurationManager
from src.DataScienceProject.components.data_validation import DataValidation
from src.DataScienceProject import logger

STAGE_NAME = "Data Validation Stage"

class DataValidationTrainingPipeline:
  def __init__(self):
    pass
  
  def initiate_data_validation(self):
      config=ConfigurationManager()
      data_validation_config = config.get_data_validation_config()
      data_validation = DataValidation(config=data_validation_config)
      status = data_validation.validate_all_columns()
      logger.info(f"Data validation status : {status}")

if __name__ == "__main__":
  try:
    logger.info(f"{'>>'*20} {STAGE_NAME} {'<<'*20}")
    data_validation = DataValidationTrainingPipeline()
    data_validation.initiate_data_validation()
  except Exception as e:
    logger.exception(e)