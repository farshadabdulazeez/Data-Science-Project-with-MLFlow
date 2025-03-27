from mlProject.config.configuration import ConfigurationManager
from mlProject.components.data_ingestion import DataIngestion
from mlProject import logger

# Define the stage name for logging
STAGE_NAME = "Data Ingestion stage"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass  # Constructor (currently not performing any operations)

    def main(self):
        # Initialize configuration manager to fetch configurations
        config = ConfigurationManager()
        
        # Get data ingestion configuration
        data_ingestion_config = config.get_data_ingestion_config()
        
        # Initialize DataIngestion class with the fetched config
        data_ingestion = DataIngestion(config=data_ingestion_config)
        
        # Download the dataset if not already available
        data_ingestion.download_file()
        
        # Extract the dataset from zip format
        data_ingestion.extract_zip_file()

# Run the pipeline only if the script is executed directly
if __name__ == '__main__':
    try:
        # Log the start of the ingestion stage
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        
        # Create an instance of the pipeline and execute it
        obj = DataIngestionTrainingPipeline()
        obj.main()
        
        # Log the successful completion of the stage
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        # Log any exceptions that occur during execution
        logger.exception(e)
        raise e