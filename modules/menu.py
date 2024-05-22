from modules.module.logic import calculate
from logging import getLogger

logger = getLogger(__name__)        # __name__ - имя модуля


def start():
    while True:
        expression = input("Введите выражение для вычисления ")
        logger.debug('Your expression is %s', expression)
        if not expression:
            logger.info("empty expression, stopping...")
            break
        result = calculate(expr=expression)
        if result is None:
            logger.info("No result back, stopping...")
            break
        print(f'Result is {result}')
