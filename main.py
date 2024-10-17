from mlProject import logger 
from mlProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeliine

STAGE_NAME = "Data Ingestion Stage"
try:
  logger.info(f">>>>> stage {STAGE_NAME} started")
  data_ingestion = DataIngestionTrainingPipeliine()
  data_ingestion.main()
  logger.info(f">>>>> stage {STAGE_NAME} completed")
except Exception as e:
  logger.exception(e)
  raise e