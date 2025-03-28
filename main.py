# Import necessary modules
from mlProject import logger  # Logger for tracking execution and errors
from mlProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline  # Data Ingestion Pipeline
from mlProject.pipeline.stage_02_data_validation import DataValidationTrainingPipeline  # Data Validation Pipeline

# ---------------------------------------
#  STAGE 1: Data Ingestion
# ---------------------------------------

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
    # Logging the exception if an error occurs
    logger.exception(e)
    raise e  # Raising the exception for debugging

# ---------------------------------------
#  STAGE 2: Data Validation
# ---------------------------------------

# Define the stage name for logging purposes
STAGE_NAME = "Data Validation stage"

try:
    # Logging the start of the data validation process
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")

    # Initializing and executing the data validation pipeline
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()

    # Logging the successful completion of the data validation process
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")

except Exception as e:
    # Logging the exception if an error occurs
    logger.exception(e)
    raise e  # Raising the exception for debugging
