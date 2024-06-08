import os 
import sys
import pandas as pd
from src.DataScienceProject.exception import CustomeException
from src.DataScienceProject.logger import logging
import pymysql
from dotenv import load_dotenv

load_dotenv()

host=os.getenv("host")
user=os.getenv("user")
password=os.getenv("password")
db=os.getenv('db')


def read_sql_data():
    logging.info("Reading SQL database Stareted")
    try:
        mydb=pymysql.connect(
            host=host,
            user=user,
            password=password,
            db=db
        )
        logging.info("connection established ",mydb)
        df=pd.read_sql_query('select * from student',mydb)
        print(df.head())
        return df 
        
    except Exception as ex:
        raise CustomeException(ex)
