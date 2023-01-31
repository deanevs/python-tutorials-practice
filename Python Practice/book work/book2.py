import logging

from BrandElevate_old import mylib

logtime = mylib.get_datetime()
log_filename = "log_" + logtime + ".txt"
logging.basicConfig(filename= log_filename, level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug("This is a log message")





#print (my_library.get_datetime())

