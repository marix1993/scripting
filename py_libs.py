### Pythin Libraries and Modules

### LIBRARIES - https://docs.python.org/3/library/

### Extensive libraries in Python (external package that you can use to accelerate everything)
# - external collection of useful methods and functions
### Python comes with some integrated libraries

# for eg.

# import random
# print(random.random())

# from random import random
#
# print(random())

# from random import *
# import math
#
# print(random())
#
# num_float = 23.66
# print(math.ceil(num_float))
# print(math.floor(num_float))
# print(round(num_float))
# print(math.pi)

### Modules (module is a set of code or functions with .py extension)
# Both used by programmers and devs
# Make it easy to read the code
# When someone imports a module the interpreter searches
# various locations for the module's definition or body
# Always Python
# DRY concept
# You can return list of functions available
# os (operating system), sys, math, random

### Library is a collection of related modules and packages ( much bigger)
# Libraries are harder to read than modules
# Used byd community members, devs and researches.
# Before we want to use it we have install it into Python project
# We generally use the pip install command
# Different languages
# Pygame, Pytorch


### Module - much smaller than library
# import os
# import datetime, sys
#
# working_dir = os.getcwd()  # Working current directory
# print(working_dir)
#
# print(datetime.date.today())
#
# print(sys.path)
#
#
# def operating_sys_information():
#     print(os.cpu_count())
#
#
# operating_sys_information()


### pip - pythons package manager (pip install requests)
# import requests
#
# requests_bbc = requests.get("https://www.bbc.co.uk")
# print(requests_bbc.status_code)
# print(requests_bbc.content)

## subprocess module - running to other code, from other profile,
# automate only after you are happy with the manual process

# import subprocess

# # Be careful to not an infinite loop
# subprocess.run(["python", "hello_world.py"])

## math module
# import math
#
# pi = math.pi
# pi_string = str(pi)
# print("The value of pi is: " + pi_string)

## random
# import random

# randum = random.randrange(1, 10)
# print(randum)

## datetime module
# import datetime

# what_is_the_date = datetime.datetime.now()
# print(what_is_the_date)

## JSON module (human readable language to transport between systems)

# import json

# x = {
#     "name": "John",
#     "age": 30,
#     "city": "London"
# }

# y = json.dumps(x)

# print(type(x))
# print(type(y))


