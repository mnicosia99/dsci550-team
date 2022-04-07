#!/usr/bin/env python
import os
import fitz
import json


#Create a file map to map paper names to file names
new = {}
for file in os.listdir('Extracted_Text'):
    for file2 in os.listdir('Metadata'):
        f1 = open('Extracted_Text/'+file)
        if file.endswith('.json'):
            content = json.load(f1)
        if file2.endswith('.json'):
            f2 = open('Metadata/'+file2)
            meta = json.load(f2)
            if meta["title"][:10] in content['text']:
                new[meta["title"]] = file.replace('.json', '.pdf')

out_file = open("filemap", "w")
json.dump(new, out_file, indent=4)
out_file.close()

#Access paper in filemap to name new directory
filemap = open('filemap')
m = json.load(filemap)

#Loop through papers
directory = os.fsencode('downloaded_pdfs')
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    try:
        for k,v in m.items():
            if v == filename:
                name = k
    except:
        name = filename
#Access photos in paper and write to new directory
    doc = fitz.open("downloaded_pdfs//"+filename)
    os.makedirs("Extracted_Images/"+name[:250],exist_ok=True)

    for i in range(len(doc)):
        for img in doc.get_page_images(i):
            xref = img[0]
            pix = fitz.Pixmap(doc, xref)
            if pix.n - pix.alpha < 4:       # this is GRAY or RGB
                pix.save("Extracted_Images/"+name[:250]+"/p%s-%s.png" % (i, xref))
            else:               # CMYK: convert to RGB first
                pix1 = fitz.Pixmap(fitz.csRGB, pix)
                pix1.save("Extracted_Images/"+name[:250]+"/p%s-%s.png" % (i, xref))
                pix1 = None
            pix = None
