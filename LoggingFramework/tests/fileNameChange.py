from common.logger_util import Logger
import time
import os

def main():
    fileName = os.path.splitext(os.path.basename(__file__))[0]
    logger = Logger(name=fileName)
    for i in range(10):
        logger.info('Hi')
        logger.debug('How are you?')
        logger.warning('Exceptional warning')
        logger.error('Exceptional error')
    logger.end()

if __name__ == "__main__":
    main()