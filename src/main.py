#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""TODO

Write Docstring.
"""

__author__ = "author_name"
__copyright__ = "Copyright 2023, some_name"
__credits__ = ["author_name"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "maintainer_name"
__email__ = "maintainer_main@domain.com"
__status__ = "Production"

import configparser
import datetime
import logging
from pathlib import Path
import sys
import os

# -------------------------------------------------- #
# SET INITIAL CONSTANTS

# Get config file name from argument
CONFIG_NAME = sys.argv[1]

PROJECT_DIRECTORY = Path(os.getcwd())
LOGS_FOLDER = "logs"
DATA_PATH = Path(PROJECT_DIRECTORY) / "data"

# -------------------------------------------------- #
# READ CONFIG FILE

# Read main config file
config = configparser.ConfigParser()
config_path = Path(PROJECT_DIRECTORY) / "config" / CONFIG_NAME
config.read(config_path)
config_default = config["DEFAULT"]

# Read Secrets file
secrets_path = Path(PROJECT_DIRECTORY) / "config" / \
    f"secrets_{config_default['Project_Environment']}.ini"
config.read(secrets_path)
secrets_values = config["SECRETS"]

# -------------------------------------------------- #
# SET LOGGING

current_date = datetime.datetime.now().strftime("%Y%m%d")
log_file_name = f"log_{current_date}.log"
log_file = Path(PROJECT_DIRECTORY) / LOGS_FOLDER / log_file_name
file_handler = logging.FileHandler(
    filename=log_file, mode="a", encoding=None, delay=False)
stdout_handler = logging.StreamHandler(sys.stdout)
handlers = [file_handler, stdout_handler]
logging.basicConfig(handlers=handlers,
                    encoding='utf-8',
                    level=os.environ.get(
                        "LOGLEVEL", config_default['Loggin_Level']),
                    format='%(asctime)s:%(levelname)s:%(message)s')

# -------------------------------------------------- #

logging.info("# ------------------------------ #")


def main():
    """
    Main function of the script
    """
    logging.info("Script started")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        pass


logging.info("Script ended")
logging.info("# ------------------------------ #")
