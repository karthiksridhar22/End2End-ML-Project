import os
import pathlib
from pathlib import Path
import requests
import zipfile
from mlProject import logger
from mlProject.utils.common import get_size
from mlProject.entity.config_entity import DataIngestionConfig

class DataIngestion:
  def __init__(self, config: DataIngestionConfig):
    self.config = config

  def download_file(self):
      # Ensure the directory 'artifacts/data_ingestion' exists
      os.makedirs(self.config.root_dir, exist_ok=True)

      # Define the path to save the downloaded file as 'data.zip'
      data_zip_path = self.config.local_data_file

      # Check if the file already exists
      if not os.path.exists(data_zip_path):
          # Download the file from the URL
          r = requests.get(url=self.config.source_URL, stream=True)

          # Save the file to the defined path
          with open(data_zip_path, 'wb') as fd:
              for chunk in r.iter_content(chunk_size=128):
                  fd.write(chunk)
          
          logger.info(f"File downloaded and saved as {data_zip_path}!")
      else:
          logger.info(f"{data_zip_path} already exists, with size: {get_size(Path(data_zip_path))}")

  
  def extract_zip_file(self):

    unzip_path = self.config.unzip_dir
    os.makedirs(unzip_path, exist_ok=True)
    with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
      zip_ref.extractall(unzip_path)

