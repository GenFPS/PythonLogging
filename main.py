import logging
from logConfig.log_config import activate_logging
from modules.menu import start

IS_LOGGER_CONFIG_USED = False

FORMAT = '%(asctime)s : %(name)s : %(levelname)s : %(message)s'

logger = logging.getLogger()


def main():
    if IS_LOGGER_CONFIG_USED:
        activate_logging()
    else:
        file_handler = logging.FileHandler(filename='data.log', encoding='utf-8', mode='w')
        file_handler.setLevel(logging.DEBUG)
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.ERROR)
        logging.basicConfig(level=logging.DEBUG, format=FORMAT, handlers=[file_handler, console_handler])

    logger.info("Старт программы")
    start()
    logger.info('Завершение программы')


if __name__ == '__main__':
    main()






