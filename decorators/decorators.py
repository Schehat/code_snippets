# closure
def outer_function(msg):
    def inner_function():
        print(msg)

    return inner_function


# closure is an inner function that remembers and has access
# to variables in the local scope in which it was created even
#  after the outer function has finished executing
my_hi = outer_function("hi")
my_bye = outer_function("bye")
my_hi()
my_hi()
my_bye()
my_bye()

# decorator simalair to closure, but instead of accessing a variable,
# it will execute a function which was given as an argument
# pro: add functionality to the original function without editing it, instead
# add additional functionality inside the wrapper function
def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print("wrapper executed")
        return original_function(*args, **kwargs)

    return wrapper_function


@decorator_function  # replaces to assign dispaly = decorator_function(display)
def display():
    print("display function ran ")


# when the original function has arguments the wrapper function
# has these arguments. Can be implemented with *args and **kwargs
@decorator_function
def display_info(name, age):
    print(f"arguments are: {name}, {age}")


display_info("Schehat", 20)
display()

# decorator with classes
class decorator_class(object):
    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        print("wrapper class executed")
        return self.original_function(*args, **kwargs)


@decorator_class
def display_info2(name, age):
    print(f"arguments are: {name}, {age}")


display_info2("Schehat", 20)
