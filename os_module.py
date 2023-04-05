# OS Module (operating system module)

# Basic use of os module

import os
import shutil

# print message to terminal
os.system('echo "Hello world!"')

# os module to manipulate directories

# Directory
directory = "test_dir"

# Path to the parent directory
parent_dir = "C:/Users/Mateusz/Desktop/"

# Path
path = os.path.join(parent_dir, directory)

## Create the dir
# os.mkdir(path) # make directory
# print("Directory '% s' created" % directory)

## Put a file in the new directory

filename = "testfile.txt"
filename = os.path.join(path, filename)

with open(os.path.join(path, filename), "w") as file1:  # open ( for opening a file)
    toFile = "content of the file is written here"
    file1.write(toFile)

print("File " + filename + " created in " + directory + " folder")

