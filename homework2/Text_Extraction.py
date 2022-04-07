#!/usr/bin/env python
import os
import tika
import json
tika.initVM()
from tika import parser

#Loop through each file in 'downloaded_pdfs' directory
directory = os.fsencode('downloaded_pdfs')
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    parsed = parser.from_file('downloaded_pdfs//'+filename) #Parse each PDF with Tika
    content = parsed["content"].replace("\n", " ").replace("\t", " ").replace(u"\ufffd", "-").replace(u"\u2019", "'").replace(u"\u2013", "-").replace(u"\u00a9", " ").replace("\xa0", " ")
    con = {'text': content}  # Save in a Dictionary
    out_file = open("Extracted_Text/"+filename.replace(".pdf", '')+".json", "w")
    json.dump(con, out_file, indent = 4) #Write to Json File
    out_file.close()
