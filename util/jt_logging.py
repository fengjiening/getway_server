import logging
import logging.handlers
import sys
from constants.configuration import Configuration

class JtLogging():
	logger = None
	
	@classmethod
	def getLogger(cls,classNmae):
		if cls.logger is None:

			print ("logger is None, config it!!")
			
			cls.logger = logging.getLogger(classNmae)
			cls.logger.setLevel(logging.DEBUG)

			formatter = logging.Formatter('%(name)-12s %(asctime)s %(module)s  %(lineno)d  %(levelname)-8s %(message)s', '%a, %d %b %Y %H:%M:%S',)
			
			sh = logging.StreamHandler(sys.stderr)
			sh.setFormatter(formatter)
			
			cls.logger.addHandler(sh)

			#fh = logging.handlers.RotatingFileHandler("%s%s.log" %(Configuration.LOG_PATH,classNmae), "a", 1024000, 10,encoding='utf-8')
			fh = logging.handlers.RotatingFileHandler("server.log", "a", 1024000, 10,encoding='utf-8')
			fh.setFormatter(formatter)
			
			cls.logger.addHandler(fh)
		else:
			#print "logger is not None"
			pass
			
		return cls.logger
