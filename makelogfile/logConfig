import sys
import logging
import logging.handlers
import logging.config

#make "root logger"
_root_logger = logging.getLogger('')

#configure log Level "INFO" 
_root_logger.setLevel(logging.INFO)

#formatter(OUTPUT datetime,level,modulename、defname、rownumber: messaga)
_simpleFormatter = logging.Formatter(
    fmt='%(asctime)s %(levelname)-8s %(module)-10s %(funcName)-10s %(lineno)4s: %(message)s'
)

#make handler for console.output log at configured log level and format
_consoleHandler = logging.StreamHandler(sys.stdout)
_consoleHandler.setLevel(logging.INFO)
_consoleHandler.setFormatter(_simpleFormatter)

#add the handler for console to rootlogger
_root_logger.addHandler(_consoleHandler)

#make hundler for file.filename is "logging.log", loglevel, filesize 1MB, make backup up to 3、utf-8
_fileHandler = logging.handlers.RotatingFileHandler(
    filename='logfile\\logging.log', maxBytes=1000000, backupCount=3, encoding='utf-8'
)
_fileHandler.setLevel(logging.INFO)
_fileHandler.setFormatter(_simpleFormatter)

#add the handler for file to rootlogger
_root_logger.addHandler(_fileHandler)
