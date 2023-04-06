# Parsing

import json
import os

# json = json.load(open("C:/Users/Mateusz/PycharmProjects/pythonProject/pythonProject/scripting/example.json"))
# value = json['name']
# print(value)

# Why is that useful? I can now use data in JSON file in this parse_json.py
# and if something's going to change in example parse file will find it.

# Script to create absolute path variable
script_dir = os.path.dirname(__file__)
print("The script is locate at: " + script_dir)
script_absolute_path = os.path.join(script_dir, 'example.json')
print("The script path is: " + script_absolute_path)

# script parse
json = json.loads(open(script_absolute_path).read())
value = json['name']
print(value)

# Loop through json keys and values (for loop)
for key in json:
    print(key, ":", json[key])

# or

for key1 in json:
    value = json[key1]
    print("Blah blah blah ({}) = ({})".format(key1, value))
