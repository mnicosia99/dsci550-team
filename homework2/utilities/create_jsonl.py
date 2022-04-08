import json, os

"""
    This script will create a jsonl file from all jksopn files contained in a given directory.
    
    Alternatively, it can be used to augment json to add attribiutes needed for running 
    falsification tests.    
"""
SCRIPT_PATH = os.path.realpath(__file__).replace("/create_jsonl.py", "")

input_path = SCRIPT_PATH + os.sep + "inputs"
input_jsonl_file_name = "bik_papers-all.jsonl"
input_jsonl_dupes_file_name = "bik_papers-all-dupes.jsonl"
generated_path = SCRIPT_PATH + os.sep + "generated"
generated_jsonl_file_name = "generated_fake-all.jsonl"

# jsonl = open(input_path + os.sep + input_jsonl_file_name, "w")
# for filename in os.listdir(input_path + os.sep + "json"):
#     fp = os.path.join(input_path + os.sep + "json" + os.sep, filename)
#     f = open(fp)
#     data = json.load(f)
#     data["split"] = "test"
#     data["label"] = "human"
#     f.close()
#     jsonl.write(json.dumps(data).replace("\n", " ")  + "\n")
# jsonl.close()

#  this block checks for dupliactes before addding to the jsonl file
lines = list()
jsonl_dupes = open(input_path + os.sep + input_jsonl_dupes_file_name, "r")
for line in jsonl_dupes:
    if line.strip() in lines:
        continue
    lines.append(line.strip())
jsonl_dupes.close()

jsonl = open(input_path + os.sep + input_jsonl_file_name, "w")
for line in lines:        
    jsonl.write(line + "\n")
jsonl.close()
        