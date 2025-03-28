import os
from mlProject import logger
from mlProject.entity.config_entity import DataValidationConfig
import pandas as pd

# DataValidation class to validate dataset columns and data types
class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config  # Store configuration

    # Function to validate all columns and data types in the dataset
    def validate_all_columns(self) -> bool:
        try:
            validation_status = True  # Initialize validation status

            # Load the dataset
            data = pd.read_csv(self.config.unzip_data_dir)
            all_cols = list(data.columns)  # Get dataset columns
            all_schema = self.config.all_schema  # Expected schema columns and types

            # Check if dataset columns match expected schema and validate data types
            for col, expected_dtype in all_schema.items():
                if col not in all_cols:
                    validation_status = False
                    logger.error(f"Missing column: {col}")
                else:
                    actual_dtype = str(data[col].dtype)
                    expected_dtype = expected_dtype.lower()
                    if "int" in expected_dtype and "int" not in actual_dtype:
                        validation_status = False
                        logger.error(f"Column {col} has incorrect type. Expected: {expected_dtype}, Found: {actual_dtype}")
                    elif "float" in expected_dtype and "float" not in actual_dtype:
                        validation_status = False
                        logger.error(f"Column {col} has incorrect type. Expected: {expected_dtype}, Found: {actual_dtype}")

            # Write validation status to file
            with open(self.config.STATUS_FILE, 'w') as f:
                f.write(f"Validation status: {validation_status}")

            return validation_status  # Return final validation status
        
        except Exception as e:
            logger.exception("Error during validation")
            raise e  # Raise exception if validation fails