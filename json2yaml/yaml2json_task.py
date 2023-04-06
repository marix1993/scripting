import json
import os
import sys
import yaml

# checking if file passed

if len(sys.argv) > 1:
    # opening file
    if os.path.exists(sys.argv[1]):
        source_file = open(sys.argv[1], "r")
        source_content = yaml.safe_load(source_file)  # added here yaml.safe_load(...) !!!
        source_file.close()
    # if it didn't find the file
    else:
        print("Error: " + sys.argv[1] + "not found.")
        exit(1)
else:
    print("Wrong format of the execution")

# processing the conversion
output = json.dumps(source_content)  # added here json.dumps(...) !!!

target_file = open(sys.argv[2], "w")
target_file.write(output)
target_file.close()

# Terminal
# python yaml2json_task.py input_task.yaml output_task.json
