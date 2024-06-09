from src.DataScienceProject.logger import logging
from src.DataScienceProject.exception import CustomeException
import sys  
from src.DataScienceProject.components.data_transformation import DataTransformationConfig,DataTransformation
from src.DataScienceProject.components.data_ingestion import DataIngestion
from src.DataScienceProject.components.data_ingestion import DataIngestionConfig

if __name__ == "__main__":
    logging.info("The execuction ha started ")
     
    try:
       # data_ingestion_config=DataIngestionConfig()
        data_ingestion=DataIngestion()
        train_data_path,test_data_path=data_ingestion.initiate_data_ingestion()

       # data_transformation_config=DataTransformationConfig()
        data_transformation=DataTransformation()
        data_transformation.initiate_data_transormation(train_data_path,test_data_path)

        
    except Exception as e :
        logging.info("customeException")
        raise CustomeException(e,sys)     