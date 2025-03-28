from pathlib import Path
from mlProject.utils.common import read_yaml, create_directories
from mlProject.constants import *
from mlProject.entity.config_entity import (DataIngestionConfig,
                                            DataValidationConfig)

# Define the file paths before using them
CONFIG_FILE_PATH = Path("config/config.yaml")
PARAMS_FILE_PATH = Path("params.yaml")
SCHEMA_FILE_PATH = Path("schema.yaml")

# Configuration Manager class
class ConfigurationManager:
    def __init__(
        self,
        config_filepath=CONFIG_FILE_PATH,
        params_filepath=PARAMS_FILE_PATH,
        schema_filepath=SCHEMA_FILE_PATH
    ):
        """Reads the YAML config files and creates necessary directories."""
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(schema_filepath)

        # Ensure artifacts directory exists
        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        """Fetches data ingestion config and creates required directories."""
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        return DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )
        

    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation  # Extracting data validation config
        schema = self.schema.COLUMNS  # Extracting schema details

        create_directories([config.root_dir])  # Ensuring root directory exists

        # Creating an instance of DataValidationConfig with required parameters
        data_validation_config = DataValidationConfig(
            root_dir=config.root_dir,
            STATUS_FILE=config.STATUS_FILE,
            unzip_data_dir=config.unzip_data_dir,
            all_schema=schema,
        )

        return data_validation_config
