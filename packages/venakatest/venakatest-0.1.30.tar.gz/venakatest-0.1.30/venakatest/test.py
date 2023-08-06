
import binascii
import traceback
import warnings
import sys
import argparse
import subprocess
import json
import re
import logging
import os
import threading
import logging.config
import datetime
def testing():
    return "ok"
def exception_handler(type, value, tb):
    logging.exception("Uncaught exception: {0} {1} - Line : {2} ".format(str(value), str(type),str(tb.tb_lineno)))
    
DEBUG = True
LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': True,

    'formatters': {
        'default': {
            'format': '[%(asctime)s] %(levelname)-8s [%(funcName)s:%(lineno)d] %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },

    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'default'
        },
   
    },
    'loggers': {
        '': {
            'level': 'INFO' if not DEBUG else 'DEBUG',
            'handlers': ['console', 'file']
        },
    }
}
def check():
    if len(sys.argv) > 0 and sys.argv[0].endswith('.bat'):
        logging.exception("Running from a batch file")

        print("Running from a batch file")
        # Additional batch-specific code here
    elif len(sys.argv) > 0 and sys.argv[0].endswith('.ps1'):
        print("Running from PowerShell")
        logging.exception("Running from a PowerShell file")
        # Additional PowerShell-specific code here
    else:
        logging.exception("Running from a Python file")
        print("Running directly from Python")
    # Code to handle other cases
logging.config.dictConfig(LOGGING_CONFIG)
# Install exception handler
sys.excepthook = exception_handler

def tobe():
    logging.info('Started syncing commits to {}'.format("testubg"))
    check()
    logging.info('Start commit: {}'.format("start"))


parser = argparse.ArgumentParser(description='Sync a number of commits before a specific commit')

parser.add_argument('--project', type=str, required=True,
                    help='Enter project name')
parser.add_argument('--token', type=str, required=True,
                    help='The API key to communicate with API')

args = parser.parse_args()

project = args.project
token = args.token

debug = True




if __name__ == '__main__':
    tobe()