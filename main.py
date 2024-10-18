from mlProject import logger 
from mlProject.components.model_trainer import ModelTrainer
from mlProject.config.configuration import ConfigurationManager
from mlProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeliine
from mlProject.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from mlProject.pipeline.stage_03_data_transformation import DataTransformationPipeline

STAGE_NAME = "Data Ingestion Stage"
try:
  logger.info(f">>>>>>> Stage {STAGE_NAME} started <<<<<<<<")
  data_ingestion = DataIngestionTrainingPipeliine()
  data_ingestion.main()
  logger.info(f">>>>>>> Stage {STAGE_NAME} completed  <<<<<<<<")
except Exception as e:
  logger.exception(e)
  raise e


STAGE_NAME = "Data Validation Stage"
try:
    logger.info(f">>>>>>> Stage {STAGE_NAME} started <<<<<<<<")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f">>>>>>> Stage {STAGE_NAME} completed <<<<<<<<")
except Exception as e:
    logger.exception(e)


STAGE_NAME = "Data Transformation Stage"
try:
    logger.info(f">>>>>>> Stage {STAGE_NAME} started <<<<<<<<")
    data_transformation = DataTransformationPipeline()
    data_transformation.main()
    logger.info(f">>>>>>> Stage {STAGE_NAME} completed <<<<<<<<")
except Exception as e:
    logger.exception(e)

STAGE_NAME = "Model Trainer Stage"
try: 
  logger.info(f">>>>>>> Stage {STAGE_NAME} started <<<<<<<<")
  config = ConfigurationManager()
  model_trainer_config = config.get_model_trainer_config()
  model_trainer = ModelTrainer(config=model_trainer_config)
  model_trainer.train()
  logger.info(f">>>>>>> Stage {STAGE_NAME} completed <<<<<<<<") 
except Exception as e:
  e


