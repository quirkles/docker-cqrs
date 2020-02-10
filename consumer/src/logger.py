import logging

LOG_FORMAT = ('%(levelname) -5s %(asctime)s %(name) -10s %(funcName) '
              '-35s %(lineno) -5d: %(message)s')

logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

LOGGER = logging.getLogger(__name__)
