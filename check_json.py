### parsing - converting string into data structure


import os
import sys
import json

if len(sys.argv) > 1:  # if more than 1 arg do the (if the command in the terminal is valid)...:
    if os.path.exists(sys.orig_argv[1]):  # if the file I'm checking exists run this code
        file = open(sys.argv[1], "r")  # "read"
        json.load(file)
        file.close()
        print("JSON is valid!")
    else:
        print(sys.argv[1] + " not found")
else:
    print("usage: check_json.py ,file.")

# to check it I need to use a terminal:
# python check_json.py example.json - to check if they are valid
