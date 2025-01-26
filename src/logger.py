import logging
import os
import sys
from datetime import datetime
from src.exception import CustomException

log_file = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path = os.path.join(os.getcwd(),"logs",log_file)
os.makedirs(logs_path,exist_ok=True)

log_file_path = os.path.join(logs_path, log_file)

logging.basicConfig(
    filename=log_file_path,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

if __name__ =="__main__":

    try:
        a=1/0

    except Exception as e:
        logging.info("Divide by Zero")
        raise CustomException(e,sys)


