import os
from datetime import datetime

print(f"get working directory: {os.getcwd()}\n")

os.chdir(os.path.dirname(os.path.dirname(__file__)))  # change directory
print(f"get working directory {os.getcwd()}\n")

# returns list of folders in inside the directors, optional parametert path
print(f"list folders in working directory: {os.listdir()}\n")

# os.mkdir('<name>')  # creates a folder
# os.mkdirs('<name/name>')  # can both create a single folder & create sub folders

# os.rmdir(<'name'>)  # removes only last (child) folder
# os.rmdir(<'name/name'>)  # can parent folders too

# os.rename('original file', 'new file')

os.chdir(os.path.dirname(__file__))
print(f"get file information: {os.stat(os.path.basename(__file__))}\n")

# get a specific attribute possible
mod_time = os.stat(os.path.basename(__file__)).st_mtime

# convert timestamp in readable from
print(f"get timestap file last modified: {datetime.fromtimestamp(mod_time)}\n")

# goes trough all directories inside this path
for dirpath, dirnames, filenames in os.walk(r"os.path.dirname(__file__)"):
    print(f"current path: {dirpath}")
    print(f"directories: {dirnames}")
    print(f"files: {filenames}\n")

print(f"all environment variables: {os.environ}\n")
print(f"home directory: {os.environ.get('Userprofile')}\n")

# joins path & sets slashes correctly
print(f"join paths: {os.path.join(os.environ.get('Userprofile', 'text.txt'))}\n")

# cant use backslash in f-strings
print("get basename: {}\n".format(os.path.basename(r"\temp\test.txt")))

print("get dirname: {}\n".format(os.path.dirname(r"\temp\test.txt")))

print("get basename & dirname: {}\n".format(os.path.split(r"\temp\test.txt")))

print("check if path exists: {}\n".format(os.path.exists(r"\temp\test.txt")))

print("check if file: {}\n".format(os.path.isfile(r"\temp\test.txt")))

print("check if directory: {}\n".format(os.path.isdir(r"\temp\test.txt")))

print("split path from extension: {}\n".format(os.path.splitext(r"\temp\test.txt")))
