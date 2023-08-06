import os
from ombot_utils import logging

os.environ.setdefault('IS_DEBUG', 'true')

logging.init_logger('ombot', 'ombot')

logging.debug('debug logging')
logging.info('info logging')
logging.warning('warning logging')
logging.error('error logging')
logging.critical('critical logging')
