import logging

class LogModule:
    @staticmethod
    def get_logger(name):
        logger = logging.getLogger(name)
        #stream Handler
        streamHandler = logging.StreamHandler()
        streamFormatter = logging.Formatter(fmt="%(asctime)s - %(name)s - %(levelname)s - %(message)s" , datefmt="%d/%m/%y  %H:%M:%S")
        streamHandler.setFormatter(streamFormatter)

    
        #Log file handler
        fileHandler = logging.FileHandler("AllLogs.log")
        formatter = logging.Formatter(fmt="%(asctime)s - %(name)s - %(levelname)s - %(message)s" , datefmt="%d/%b/%y  %H:%M:%S")
        fileHandler.setFormatter(formatter)

        logger.addHandler(streamHandler)
        logger.addHandler(fileHandler)
        logger.setLevel(logging.DEBUG)
        return logger