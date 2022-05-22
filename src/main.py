#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""TODO

Write Docstring.
"""

__author__ = "author_name"
__copyright__ = "Copyright 2022, some_name"
__credits__ = ["author_name"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "maintainer_name"
__email__ = "maintainer_main@domain.com"
__status__ = "Production"

import configparser
import datetime
import logging


# Create and configure logger
current_day = datetime.datetime.now().strftime("%Y%m%d")

logging.basicConfig(filename=f"logs\{current_day}_log.log",
                    format='%(asctime)s %(levelname)s %(message)s',
                    filemode='a')

# Creating an object
logger = logging.getLogger()

# Setting the threshold of logger
logger.setLevel(logging.INFO)

logger.info("####################")
logger.info("Script started")

# read config.ini file
logger.info("Reading config")
config = configparser.ConfigParser()
config.read('config\config.ini')
config_default = config['DEFAULT']


def main():
    pass
    

if __name__ == "__main__":
    main()


logger.info("Script ended")
logger.info("####################")
