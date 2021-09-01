import os
from contextlib import contextmanager

os.chdir(os.path.dirname(__file__))


class Open_File:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode, encoding="UTF-8")
        return self.file

    def __exit__(self, exc_type, exc_val, tranceback):
        self.file.close()


# Open_File(...) executes init ant then automatically __enter__ which
# returns the file object and gets the alias
# after the with block __exit__ will be executed automatically
with Open_File("test.txt", "w") as f:
    f.write("Testing")

print(f.closed)

# implementation with functions
@contextmanager
def open_file(file, mode):
    try:
        f = open(file, mode, encoding="UTF-8")  # equals __enter__
        yield f  # stops here and executes the with block
    finally:
        f.close()  # equals __exit__


with open_file("test.txt", "w") as f:
    f.write("Check")

print(f.closed)
