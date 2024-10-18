from mlProject.config.configuration import ConfigurationManager
from mlProject.components.model_trainer import ModelTrainer
from mlProject import logger

STAGE_NAME = "Model Training Stage"

class ModelTrainerPipeline:
  def __init__(self):
    pass

  def train_model(self):
    try: 
      config = ConfigurationManager()
      model_trainer_config = config.get_model_trainer_config()
      model_trainer = ModelTrainer(config=model_trainer_config)
      model_trainer.train() 
    except Exception as e:
      e

if __name__ == '__main__':
  try:
    logger.info(f">>>>> Stage {STAGE_NAME} started")
    obj = ModelTrainerPipeline
    obj.main()
    logger.info(f">>>>> Stage {STAGE_NAME} completed")
  except Exception as e:
    logger.exception(e)