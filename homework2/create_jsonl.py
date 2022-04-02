import json, os

SCRIPT_PATH = os.path.realpath(__file__).replace("/create_jsonl.py", "")

count = 0
jsonl = open(SCRIPT_PATH + os.sep + "inputs" + os.sep + "json" + os.sep + "bik_paper_data.jsonl", "w")
for filename in os.listdir(SCRIPT_PATH + os.sep + "inputs" + os.sep + "json"):
    fp = os.path.join(SCRIPT_PATH + os.sep + "inputs" + os.sep + "json" + os.sep, filename)
    if ".jsonl" in fp:
        continue
    f = open(fp)
    print(fp)
    data = json.load(f)
    jsonl.write(json.dumps(data)  + "\n")
    jsonl.write(json.dumps(data)  + "\n")
    if count < 104:
        jsonl.write(json.dumps(data)  + "\n")
    count += 1
        