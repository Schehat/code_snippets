import os
from contextlib import contextmanager


@contextmanager
def change_dir(destination):
    try:
        cwd = os.getcwd()
        os.chdir(destination)
        # just yield is enough, yield f or something not necessary due to no need working with an object
        yield
    finally:
        os.chdir(cwd)


with change_dir("custom_context_managers"):  # without an alias is enough
    print(os.listdir())

with change_dir("decorators"):
    print(os.listdir())
