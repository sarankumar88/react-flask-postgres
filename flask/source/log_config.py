import logging

# Define the logging configuration of the current program.
def getLogger(loggername,logFileName):
    logger = logging.getLogger(loggername)
    logger.setLevel(logging.DEBUG)

    # Add the log message handler to the logger
    #fh = logging.handlers.RotatingFileHandler(logFileName, maxBytes=40, backupCount=15)
    fh = logging.FileHandler(logFileName)
    fh.setLevel(logging.DEBUG)
    # create console handler with a higher log level
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    # create formatter and add it to the handlers
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    fh.setFormatter(formatter)
    # add the handlers to logger
    logger.addHandler(ch)
    logger.addHandler(fh)
    return logger