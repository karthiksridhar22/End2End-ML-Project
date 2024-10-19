import joblib
import numpy as np
import pandas as pd
from pathlib import Path
from mlProject.constants import *
from mlProject.utils.common import read_yaml

config = read_yaml(CONFIG_FILE_PATH)
model_path = config.model_evaluation.model_path



class PredictionPipeline:
  def __init__(self):
    self.model = joblib.load(Path(model_path))

  def predict(self, data):
    prediction = self.model.predict(data)

    return prediction