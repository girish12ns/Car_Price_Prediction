import sys
import os
from src.logger import logging


def get_error_message(error_message,error_detail:sys):
    _,_,exc_traceback=error_detail.exc_info()
    line_number=exc_traceback.tb_lineno
    file_name=exc_traceback.tb_frame.f_code.co_filename

    error_message="The message occured in line no {} and in {} and error_message is {}".format(line_number,file_name,str(error_message))

    return error_message

class customException(Exception):
    def __init__(self,error_message,error_detail):
        self.error_message=get_error_message(error_message,error_detail)

    def __str__(self):
        return self.error_message


if __name__=="__main__":
    try:
        result=1/0
    except Exception as e:
        logging.info('logging has started')
        raise customException(e,sys)
    
