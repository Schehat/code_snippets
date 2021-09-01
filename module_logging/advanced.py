import os
import logging
import employee

os.chdir(os.path.dirname(__file__))

# pro of custom logger multiple handler possible
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("advanced.log")
formatter = logging.Formatter("%(asctime)s:%(levelname)s:%(name)s:%(message)s")
file_handler.setFormatter(formatter)

# this will only print something into the file_handler which means the advanced.log
# if level ERROR or higher even though our logger is in level DEBUG
file_handler.setLevel(logging.ERROR)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)


def add(x, y):
    """Add Function"""
    return x + y


def subtract(x, y):
    """Subtract Function"""
    return x - y


def multiply(x, y):
    """Multiply Function"""
    return x * y


def divide(x, y):
    """Divide Function"""
    try:
        result = x / y
    except ZeroDivisionError:
        # logger.error("tried to divide by zero")
        # error does not include traceback, exception does
        logger.exception("tried to divide by zero")
    else:
        return result


num_1 = 20
num_2 = 0

add_result = add(num_1, num_2)
logger.debug("Add: {} + {} = {}".format(num_1, num_2, add_result))

sub_result = subtract(num_1, num_2)
logger.debug("Sub: {} - {} = {}".format(num_1, num_2, sub_result))

mul_result = multiply(num_1, num_2)
logger.debug("Mul: {} * {} = {}".format(num_1, num_2, mul_result))

div_result = divide(num_1, num_2)
logger.debug("Div: {} / {} = {}".format(num_1, num_2, div_result))
