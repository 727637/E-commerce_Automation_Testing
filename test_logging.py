import logging

def test_loggingDemo():
    logger = logging.getLogger(__name__)


    fileHandler = logging.FileHandler('logfile.log')
    logger.addHandler(fileHandler)  #filehandler
    formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
    fileHandler.setFormatter(formatter)

    logger.setLevel(logging.INFO)
    logger.debug("debug statement is executed")
    logger.info("info statement")
    logger.warning("something is in warning mode")
    logger.error("error occurs")
    logger.critical("critical")


