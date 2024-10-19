from mlProject import logger 
from mlProject.components.model_trainer import ModelTrainer
from mlProject.config.configuration import ConfigurationManager
from mlProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeliine
from mlProject.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from mlProject.pipeline.stage_03_data_transformation import DataTransformationPipeline
from mlProject.pipeline.stage_04_model_trainer import ModelTrainerPipeline
from mlProject.pipeline.stage_05_model_evaluation import ModelEvaluationPipeline

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
  model_trainer = ModelTrainerPipeline()
  model_trainer.main()
  logger.info(f">>>>>>> Stage {STAGE_NAME} completed <<<<<<<<") 
except Exception as e:
  e

STAGE_NAME = "Model Evaluation Stage"
try:
  logger.info(f">>>>> Stage {STAGE_NAME} started")
  obj = ModelEvaluationPipeline()
  obj.main()
  logger.info(f">>>>> Stage {STAGE_NAME} completed")
except Exception as e:
  logger.exception(e)

