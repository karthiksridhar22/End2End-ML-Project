from mlProject.config.configuration import ConfigurationManager
from mlProject.components.model_evaluation import ModelEvaluation
from mlProject import logger

STAGE_NAME = "Model Evaluation Stage"

class ModelEvaluationPipeline:
  def __init__(self):
    pass

  def main(self):
    try: 
      config = ConfigurationManager()
      model_evaluation_config = config.get_model_evaluation_config()
      model_evaluation = ModelEvaluation(config=model_evaluation_config)
      model_evaluation.log_into_mlflow() 
    except Exception as e:
      e

if __name__ == '__main__':
  try:
    logger.info(f">>>>> Stage {STAGE_NAME} started")
    obj = ModelEvaluationPipeline()
    obj.main()
    logger.info(f">>>>> Stage {STAGE_NAME} completed")
  except Exception as e:
    logger.exception(e)