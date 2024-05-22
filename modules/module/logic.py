from logging import getLogger

logger = getLogger(__name__)


def calculate(expr: str):
    logger.debug('Get expression %s', expr)
    try:
        result = eval(expr)
        logger.debug('Evaluated %s', result)
        return result
    except Exception as e:
        logger.error('Get an exception: %s', e)
        return None
