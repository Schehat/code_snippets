def prefix_decorator(prefix):
    def decorator_func(orig_func):
        def wrapper_func(*args, **kwargs):
            print(f"{prefix} executed before {orig_func.__name__}")
            result = orig_func(args, kwargs)
            print(f"{prefix} executed after {orig_func.__name__}\n")
            return result

        return wrapper_func

    return decorator_func


@prefix_decorator("TESTING:")
def display_info(name, age):
    print(f"display_info ran with arguments {name}, {age}")


display_info("John", 28)
