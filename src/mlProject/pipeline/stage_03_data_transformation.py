from mlProject.config.configuration import ConfigurationManager
from mlProject.components.data_transformation import DataTransformation
from mlProject import logger
from pathlib import Path
from mlProject.constants import *
from mlProject.utils.common import *

config_file_path = CONFIG_FILE_PATH

config = read_yaml(config_file_path)
status_file = config.data_validation.STATUS_FILE


STAGE_NAME = "Data Transformation Stage"

class DataTransformationPipeline:
  def __init__(self):
    pass

  def main(self):
    try:
      with open(str(status_file), "r") as f:
        status = f.read().split(" ")[-1]
        logger.info(f" Data scheme status: {status}")

      if status == "True":
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(config = data_transformation_config)
        data_transformation.train_test_spliting()
      else:
        raise Exception("Data schema not valid")
      
    except Exception as e:
      e


if __name__ == '__main__':
  try:
    logger.info(f">>>>> Stage {STAGE_NAME} started")
    obj = DataTransformationPipeline
    obj.main()
    logger.info(f">>>>> Stage {STAGE_NAME} completed")
  except Exception as e:
    logger.exception(e)