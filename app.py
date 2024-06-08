from src.DataScienceProject.logger import logging
from src.DataScienceProject.exception import CustomeException
import sys  
from src.DataScienceProject.components.data_ingestion import DataIngestion
from src.DataScienceProject.components.data_ingestion import DataIngestionConfig

if __name__ == "__main__":
    logging.info("The execuction ha started ")
     
    try:
       # data_ingestion_config=DataIngestionConfig()
        data_ingestion=DataIngestion()
        data_ingestion.initiate_data_ingestion()
        
    except Exception as e :
        logging.info("customeException")
        raise CustomeException(e,sys)     