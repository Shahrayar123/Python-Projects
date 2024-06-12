import os
from common.loggerUtil import Logger

def main():
    fileName = os.path.splitext(os.path.basename(__file__))[0]
    logger = Logger(name=fileName)
    for i in range(10):
        logger.info('Hi!!!')
        logger.debug('How are you? testing')
        logger.warning(f'Exceptional warning {fileName}'.format(fileName))
        logger.error('Exceptional error')

if __name__ == "__main__":
    main()