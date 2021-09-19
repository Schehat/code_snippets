import time


def my_timer(orig_func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = orig_func(*args, **kwargs)
        end = time.time()
        print(f"execution time: {end - start}")
        return result

    return wrapper


@my_timer
def display_info(name, age):
    time.sleep(1)
    print(f"arguments are: {name}, {age}")


display_info("Schehat", 20)
