import os, zipfile
from gdrive_utils import get_gdrive_service, download_files_from_gdrive

# import parser object from tike
from tika import parser  
 
SCRIPT_PATH = os.path.realpath(__file__).replace("/parse_pdfs.py", "")

#  shared Articles/pdfs folder id: 1NDdoJyHwy89rxpDgEnIPYkuBF5yG24C9
# parent = "1NDdoJyHwy89rxpDgEnIPYkuBF5yG24C9"
# service, drive = get_gdrive_service()
# download_files_from_gdrive(service, drive, parent, "pdf", SCRIPT_PATH + os.sep + "inputs" + os.sep + "pdfs")

for filename in os.listdir(SCRIPT_PATH + os.sep + "inputs" + os.sep + "pdfs"):
    f = os.path.join(SCRIPT_PATH + os.sep + "inputs" + os.sep + "pdfs", filename)
    if os.path.isfile(f):            
             
        # opening pdf file
        print("========>" + filename)
        parsed_pdf = parser.from_file(SCRIPT_PATH + os.sep + "inputs" + os.sep + "pdfs" + os.sep + filename)
    
        # saving content of pdf
        # you can also bring text only, by parsed_pdf['text'] 
        # parsed_pdf['content'] returns string 
        data = parsed_pdf['content']
        metadata = parsed_pdf['metadata']
        
        # ['metadata'] attribute returns 
        # key-value pairs of meta-data 
        print(parsed_pdf['metadata']) 
        print(type(parsed_pdf['metadata']))

        # Returns keys applicable for given pdf.
        print(parsed_pdf.keys())
        
        # Printing of content 
        print(data)
        # print(type(data))

        break