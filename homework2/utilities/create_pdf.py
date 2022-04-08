import os, pdfkit
from gdrive_utils import download_files_from_gdrive, write_to_gdrive, get_gdrive_service

"""
    This script will download html files from our teams shared google drive and create pdfs. 
    Also the generated pdfs will be written to a shared Google drive folder.
    
    Dependencies: pdfkit
"""
SCRIPT_PATH = os.path.realpath(__file__).replace("/create_pdf.py", "")

def create_pdf(source_extension, input_dir, outpur_dir):
    for filename in os.listdir(input_dir):
        f = os.path.join(input_dir, filename)
        # checking if it is a file
        if os.path.isfile(f):
            options = {
                "enable-local-file-access": ""
            }    
            out_filename = filename.replace(source_extension, "pdf")
            pdfkit.from_file(input_dir + filename, outpur_dir + "pdfs" + os.sep + out_filename, options=options)

#  this is the id of the folder in the Google drive that the html files are in
parent = "1_9eRWu2AYMNx8WAUCCkBIbIKPa0KW0pe"
extension = "html"
# this is the id of shared Google Drive folder that the generated files can be uploaded to
source_parent = "1zMiu93_g16guGlj1BEhyVVOyPCEhQx2_"
service, drive = get_gdrive_service()

download_files_from_gdrive(service, drive, parent, extension, SCRIPT_PATH + os.sep + extension + os.sep)
create_pdf(extension, SCRIPT_PATH + os.sep + extension + os.sep, SCRIPT_PATH + os.sep + "generated" + os.sep)
write_to_gdrive(drive, source_parent, SCRIPT_PATH + os.sep + "generated" + os.sep + "pdfs" + os.sep)