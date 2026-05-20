from src.DataScienceProject import logger
from src.DataScienceProject.utils.common import read_yaml , create_directories
from src.DataScienceProject.constants import *
from src.DataScienceProject.entity.config_entity import (DataValidationConfig, ModelTrainerConfig)
from src.DataScienceProject.config.configuration import ConfigurationManager
import pandas as pd
import os
from sklearn.linear_model import ElasticNet
import joblib

class ModelTrainer:
  def __init__(self, config : ModelTrainerConfig):
    self.config = config

  def train_model(self):
    logger.info("Loading train and test data")
    train_data = pd.read_csv(self.config.train_data_path)
    test_data = pd.read_csv(self.config.test_data_path)

    logger.info("Splitting input and target feature from train and test data")
    train_x = train_data.drop(self.config.target_column, axis=1)
    train_y = train_data[self.config.target_column]

    test_x = test_data.drop(self.config.target_column, axis=1)
    test_y = test_data[self.config.target_column]

    logger.info("Initializing the ElasticNet model")
    model = ElasticNet(alpha=self.config.alpha, l1_ratio=self.config.l1_ratio)

    logger.info("Training the ElasticNet model")
    model.fit(train_x, train_y)

    logger.info("Saving the trained model")
    joblib.dump(model, os.path.join(self.config.root_dir, self.config.model_name))