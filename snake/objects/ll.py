import logging

logging.basicConfig(format='[%(levelname)s] [%(filename)s:%(lineno)d]: %(message)s',level=logging.DEBUG)
logger = logging.getLogger('my_logger')