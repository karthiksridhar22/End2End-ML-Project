import os
import pathlib
from pathlib import Path
import requests
import zipfile
from mlProject import logger
from mlProject.utils.common import get_size
from mlProject.entity.config_entity import DataValidationConfig
import pandas as pd

class DataValidation:
  def __init__(self, config = DataValidationConfig):
    self.config = config

  def validate_all_columns(self) -> bool:
    try:
      validation_status = False

      data = pd.read_csv(self.config.unzip_data_dir)
      names = list(data.columns)
      types = list(data.dtypes)
      
      all_schema_cols = self.config.all_schema['COLUMNS']
      schema_keys = self.config.all_schema.keys()

      for i in range (len(names)-1):
        if ((names[i] not in schema_keys) or (types[i] != all_schema_cols[names[i]])):
          validation_status = False
          break
        else:
          validation_status = True

      with open(self.config.STATUS_FILE, "w") as f:
        f.write(f"Status: {validation_status}")


      return validation_status
          
    except Exception as e:
      e