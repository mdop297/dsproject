from src.dsproject.config.configurations import ConfigurationManager
from src.dsproject.components.data_validation import DataValiadtion
from src.dsproject import logger

STAGE_NAME="Data Validation Stage"

class DataValidationTrainingPipeline:
    def __init__(self):
        pass
        
    def initiate_data_validation(self):
        try:
            config = ConfigurationManager()
            data_validation_config = config.get_data_validation_config()
            data_validation = DataValiadtion(config=data_validation_config)
            data_validation.validate_all_columns()
        except Exception as e:
            raise e
        
        
if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataValidationTrainingPipeline()
        obj.initiate_data_validation()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e