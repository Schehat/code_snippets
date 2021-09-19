import os
import subprocess

os.chdir(os.path.dirname(__file__))

# wls is needed to use bash instead of cmd.
# To use cmd second argument shell=True needed e.g.: .("dir", shell=True)
subprocess.run("wsl ls -al")

# does not print output in console but saves it
p1 = subprocess.run("wsl ls -al", capture_output=True)

# does not format correctly due to output stored in bytes
#  with new lines not evaluated as new lines
p1.stdout

# converts byte to unicode
p1.stdout.decode()

# converts to unicode in the first place
p1 = subprocess.run("wsl ls -al", capture_output=True, text=True)
print(p1.returncode)
print(p1.stdout)

with open("output.txt", "w") as f:
    # move stream to the file with specifying stdout
    subprocess.run("wsl ls -al", stdout=f, text=True)

# ls to a directory dne which does not exist. Python does not throw
# an exception if a command fails
p1 = subprocess.run("wsl ls -al dne", capture_output=True, text=True)
print(p1.returncode)
print(p1.stderr)

# when adding argument check=True python will throw an error
# p1 = subprocess.run("wsl ls -al dne", capture_output=True, text=True, check=True)
