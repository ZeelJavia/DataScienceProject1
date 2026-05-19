from src.DataScienceProject.config.configuration import ConfigurationManager
from src.DataScienceProject.components.data_ingetion import DataIngetion
from src.DataScienceProject import logger
from src.DataScienceProject.components.data_transformation import DataTransformation
from pathlib import Path

STAGE_NAME = "Data Transformation Stage"

class DataTransformationTrainingPipeline:
  def __init__(self):
    pass
  
  def initiate_data_transformation(self):
    try:
        with open(Path("artifacts/data_validation/status.txt" )) as f:
          status = f.read()
          
        if status == 'Validation status : True ':
            logger.info("Data validation is completed successfully. Starting data transformation")
            config = ConfigurationManager()
            data_transformation_config = config.get_data_transformation_config()
            data_transformation = DataTransformation(data_transformation_config)
            data_transformation.train_test_splitting()
        else:
            logger.info("YOur schema is not valid.")
    except Exception as e:
        raise e