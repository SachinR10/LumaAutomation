import logging

class LogGen:
    @staticmethod
    def loggen():
        logging.basicConfig(filename="testloggerimp.log",format="%(asctime)s %(levelname)s %(module)s %(funcName)s %(message)s",level=logging.DEBUG,datefmt='%H:%M:%S')
        logger = logging.getLogger()
        #logger.setLevel(logging.INFO)
        return logger