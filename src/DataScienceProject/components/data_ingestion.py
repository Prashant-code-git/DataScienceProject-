import os 
import sys
import pandas as pd
from src.DataScienceProject.exception import CustomeException
from src.DataScienceProject.logger import logging
from src.DataScienceProject.utils import read_sql_data
from dataclasses import  dataclass

from sklearn.model_selection import train_test_split

@dataclass
class DataIngestionConfig:
    train_data_path:str=os.path.join('artifacts','train.csv')
    test_data_path:str=os.path.join('artifacts','test.csv')
    raw_data_path:str=os.path.join('artifacts','raw.csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()
    def initiate_data_ingestion(self):
        try:
            ## reading the data from mysql
            df= read_sql_data()  
            logging.info("Reading from mysql database")
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)
            df.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            df.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info("Data ingesstion in completedd")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
            

        except Exception as e :
            raise CustomeException(e,sys)

