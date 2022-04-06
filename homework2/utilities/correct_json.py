import os, json

SCRIPT_PATH = os.path.realpath(__file__).replace("/correct_json.py", "")

for filename in os.listdir(SCRIPT_PATH + os.sep + "outputs/Grover_Input"):
    file = open(SCRIPT_PATH + os.sep + "outputs/Grover_Input/" + filename)
    content = file.read()
    print(content)
    file.close()
    content = content.replace("\\n", " ").replace("\\t", " ").replace(u"\ufffd", "-").replace(u"\u2019", "'").replace(u"\u2013", "-").replace(u"\u00a9", " ").replace(u'\\xa0', u' ').replace("\\r", " ").replace("\\U000f", "").replace("\\u2003", " ").replace("\\ufeff", " ").replace("\\u2002", " ").replace("\\u2009", " ")
    print(content)
    out_file = open(SCRIPT_PATH + os.sep + "outputs/Grover_Input/" + filename, "w")
    out_file.write(content)
    out_file.close()
    
    # print(json.loads(r'"\ud835\udc6a\ud835\udc89\ud835\udc90\ud835\udc84\ud835\udc8c"'))
