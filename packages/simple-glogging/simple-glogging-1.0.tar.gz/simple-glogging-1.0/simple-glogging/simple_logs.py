import logging
import os
from datetime import datetime, timedelta
import pathlib
import os
from functools import singledispatch
import yaml
from yaml.loader import SafeLoader
import sys
from datetime import datetime

from abc import ABC, abstractmethod


class SimpleLogging():
    logger = None
    log_level_name = {
        'DEBUG': logging.DEBUG,
        "INFO": logging.INFO,
        "WARNING": logging.WARNING,
        "ERROR": logging.ERROR,
        "CRITICAL": logging.CRITICAL
    }
    def __init__(self,root_log_name) -> None:
        logging.basicConfig(
            level=logging.DEBUG,
            format="RRRR %(asctime)s %(levelname)s %(name)s.%(funcName)s %(lineno)s %(message)s",
        )
        SimpleLogging.logger = logging.getLogger(root_log_name)
        #SimpleLogging.logger.propagate = False

    @classmethod
    def getLogger(cls,logger_name):
        return cls.logger.getChild(logger_name)

    @classmethod
    def initializeLogger(cls):

        #handeler dict

        file_path = os.path.abspath("resources/{}".format('log-config.yaml'))
        #reading config file
        with open(file_path) as f:
            config_data = yaml.load(f, Loader=SafeLoader)
        #print(config_data)
        #get log level from environment
        log_level = os.getenv('log_level', config_data['default_loglevel'])

        file_log_formate = config_data['default_formate']
        cls.logger.setLevel(cls.log_level_name[log_level ])
        formatter = logging.Formatter(file_log_formate)

        if 'file' in config_data['handelers'].keys():
            file_config = config_data['handelers']['file']
            file_path = file_config['filepath'].format(datetime.now())
            file_handler = logging.FileHandler(file_path)
            file_handler.setFormatter(formatter)
            cls.logger.addHandler(file_handler)
        
        if 'console' in config_data['handelers'].keys():
            console_config = config_data['handelers']['console']
            console_handler = logging.StreamHandler(sys.stdout)
            console_handler.setFormatter(formatter)
            cls.logger.addHandler(console_handler)
        #logger.propagate = False to make sure that child logger does not propagate its message to the root logger.
        cls.logger.propagate = False
    
    @classmethod
    def updateLogger(cls,**kwargs):
        if 'level' in kwargs:
            if kwargs['level'] in cls.log_level_name:
                cls.logger.setLevel(cls.log_level_name[kwargs['level']])
        if 'formate' in kwargs:
            pass





if __name__ == '__main__':
    root_log_name = 'Falcon'
    sl = SimpleLogging(root_log_name)
    sl.logger.info("This is from root logging")
    sl.getLogger("Child logger").info("This is child logger")
    sl.initializeLogger()
    print("==================After Initializing =========================")
    log = sl.getLogger("Child1")
    log.info("This is info in child 1 logger")
    log.error("This is error in child 1 logger")
    
    print("=================== After Updating ============================")
    change_settings = {'level':'DEBUG'}
    sl.updateLogger(**change_settings)

    log = sl.getLogger("Child2")
    log.info("This is info in child 2 logger")
    log.debug("This is debug in child 2 logger")
    log.error("This is error in child 2 logger")



