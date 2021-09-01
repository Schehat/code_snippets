import os
import logging
import time
from functools import wraps

os.chdir(os.path.dirname(__file__))


def my_logger(orig_func):
    logging.basicConfig(filename=f"{orig_func.__name__}.log", level=logging.INFO)

    @wraps(orig_func)  # this preserve the orig_func information
    def wrapper(*args, **kwargs):
        logging.info(f"Ran with args: {args} and kwargs: {kwargs}")
        return orig_func(*args, **kwargs)

    return wrapper


def my_timer(orig_func):
    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = orig_func(*args, **kwargs)
        end = time.time()
        print(f"{orig_func.__name__} execution time: {end - start}")
        return result

    return wrapper


# stacking possible, from bottom to top
# => display_info = my_logger(my_timer(display_info))
@my_logger
@my_timer
def display_info(name, age):
    print(f"arguments are: {name}, {age}")


# problem is that the name of this function is wrapper and after that when
# we stack the next decorator my_logger will get the name wrapper this can
# be avoided with the wraps decorator and the name display_info will be preserved
print(my_timer(display_info).__name__)

display_info("Tom", 30)
