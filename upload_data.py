from src.utils import dump_csv_file_to_mongodb_collection
from src.exception import SensorException
from src.logger import logging
import os, sys

def storing_record_in_mongo():
    try:
        file_path="D:\End to end project\Sensor fault detection mlproject\requirements.txt"
        database_name="sensor"
        collection_name="sensor_readings"
        dump_csv_file_to_mongodb_collection(file_path, database_name, collection_name)
        
    except Exception as e:
        raise e
    
    if __name__=="__main__":
        storing_record_in_mongo()