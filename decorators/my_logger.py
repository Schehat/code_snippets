import os
import logging

os.chdir(os.path.dirname(__file__))


def my_logger(orig_func):
    logging.basicConfig(filename=f"{orig_func.__name__}.log", level=logging.INFO)

    def wrapper(*args, **kwargs):
        logging.info(f"Ran with args: {args} and kwargs: {kwargs}")
        return orig_func(*args, **kwargs)

    return wrapper


@my_logger
def display_info(name, age):
    print(f"arguments are: {name}, {age}")


display_info("Schehat", 20)
