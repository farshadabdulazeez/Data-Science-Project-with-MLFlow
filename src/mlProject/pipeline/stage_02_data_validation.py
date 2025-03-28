from mlProject.config.configuration import ConfigurationManager  # Configuration manager to handle config files
from mlProject.components.data_validation import DataValidation  # Data validation component
from mlProject import logger  # Logger for tracking execution and errors

# Define the stage name for logging purposes
STAGE_NAME = "Data Validation stage"

# Define the DataValidationTrainingPipeline class
class DataValidationTrainingPipeline:
    def __init__(self):
        pass  # No initialization logic needed

    # Main function to execute the data validation process
    def main(self):
        config = ConfigurationManager()  # Create an instance of ConfigurationManager
        data_validation_config = config.get_data_validation_config()  # Retrieve data validation configuration
        data_validation = DataValidation(config=data_validation_config)  # Initialize DataValiadtion class with config
        data_validation.validate_all_columns()  # Execute the validation method


# Run the data validation pipeline
if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")  # Log the start of the validation process
        obj = DataValidationTrainingPipeline()  # Instantiate the validation pipeline class
        obj.main()  # Execute the main validation function
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")  # Log the successful completion
    except Exception as e:
        logger.exception(e)  # Log any exceptions encountered during execution
        raise e