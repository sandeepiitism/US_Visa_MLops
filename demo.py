# from us_visa.logger import logging

# logging.info("Starting the demo")


from us_visa.logger import logging
from us_visa.exception import USvisaException
import sys

try:
    a=1/"10"
except Exception as e:
    raise USvisaException(e,sys)

