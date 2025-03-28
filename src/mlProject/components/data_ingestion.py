import os
import urllib.request as request
import zipfile
from pathlib import Path
from mlProject import logger
from mlProject.utils.common import get_size
from pathlib import Path
from mlProject.entity.config_entity import DataIngestionConfig

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        """Downloads the dataset if not already present."""
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url=self.config.source_URL,
                filename=self.config.local_data_file
            )
            logger.info(f"{filename} downloaded successfully! Headers:\n{headers}")
        else:
            logger.info(f"File already exists with size: {get_size(Path(self.config.local_data_file))}")

    def extract_zip_file(self):
        """Extracts the dataset zip file into the specified directory."""
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)

        logger.info(f"Extracting {self.config.local_data_file} to {unzip_path}...")
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)
        logger.info(f"Extraction complete: Files extracted to {unzip_path}")
