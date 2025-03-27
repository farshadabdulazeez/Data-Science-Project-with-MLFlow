# Importing necessary modules
from mlProject import logger
from mlProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

# Define the stage name for logging purposes
STAGE_NAME = "Data Ingestion stage"

try:
    # Logging the start of the data ingestion process
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")

    # Initializing and executing the data ingestion pipeline
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()

    # Logging the successful completion of the data ingestion process
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")

except Exception as e:
    # Logging the exception in case of failure
    logger.exception(e)
    raise e  # Raising the exception for further debugging if necessary
