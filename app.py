'''@app

This file is the acting web server.

@debug, enables debugging, and tracebacks
@host, tells the OS (guest VM) to accept connections from all public IP
    addresses.

Note: both the handler, and logger has levels. If the level of the logger is
      higher than that of the handler, no messages will be handled by the
      corresponding handler.

'''

import sys
import yaml
import logging
from log.logger import Logger
from logging.handlers import RotatingFileHandler
from interface import app

# path to yaml
prefix = ''
if len(sys.argv) >= 2:
    if sys.argv[1] == 'test':
        prefix = 'test/'
hiera_path = prefix + 'hiera/settings.yaml'

# define configuration
with open(hiera_path, 'r') as stream:
    try:
        # local variables
        settings = yaml.load(stream)

        # local logger: used for this module
        root = settings['general']['root']
        LOG_PATH = root + '/' + settings['webserver']['flask_log_path']
        HANDLER_LEVEL = settings['application']['log_level']

        # flask attributes: accessible across application
        app.config.update(
            HOST=settings['general']['host'],
            PORT_REDIS=settings['redis']['port'],
            ROOT=settings['general']['root'],
            DB_LOG_PATH=settings['database']['log_path'],
            DB_ML=settings['database']['name'],
            DB_USERNAME=settings['database']['username'],
            DB_PASSWORD=settings['database']['password'],
            LOG_LEVEL=HANDLER_LEVEL,
            FLASK_LOG_PATH=settings['webserver']['flask_log_path'],
            ERROR_LOG_PATH=settings['application']['error_log_path'],
            WARNING_LOG_PATH=settings['application']['warning_log_path'],
            INFO_LOG_PATH=settings['application']['info_log_path'],
            DEBUG_LOG_PATH=settings['application']['debug_log_path'],
            MODEL_TYPE=settings['application']['model_type']
        )
    except yaml.YAMLError as error:
        logger = Logger('error', 'yaml')
        logger.log(error)

# log handler: requires the below logger
formatter = logging.Formatter(
    "[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s")
handler = RotatingFileHandler(LOG_PATH, maxBytes=10000000, backupCount=5)
handler.setLevel(HANDLER_LEVEL)
handler.setFormatter(formatter)
app.logger.addHandler(handler)

# logger: complements the log handler
log = logging.getLogger('werkzeug')
log.setLevel(logging.DEBUG)
log.addHandler(handler)

# run application
app.run(host='0.0.0.0')
