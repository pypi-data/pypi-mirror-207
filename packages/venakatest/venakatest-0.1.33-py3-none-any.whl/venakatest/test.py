
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
python_executable = 'python.exe'
batch_executable = 'cmd.exe'
powershell_executable = 'powershell.exe'
def testing():
    return "ok"
def exception_handler(type, value, tb):
    logging.exception("Uncaught exception: {0} {1} - Line : {2} ".format(str(value), str(type),str(tb.tb_lineno)))
logging.basicConfig(level=logging.DEBUG)
def check():
    
        # Additional batch-specific code here
    if os.environ.get('COMSPEC', '').endswith('cmd.exe'):
        print("Running from batch")
        logging.exception("Running from a batch file")
        # Additional PowerShell-specific code here
    elif 'MyInvocation' in str(globals().get('Get-Variable')):
        logging.exception("Running from a powershell file")
        print("Running directly from powershell")
    else:
        logging.exception("Running from python file")

        print("Running from a python file")
    # Code to handle other cases

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