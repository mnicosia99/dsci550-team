import os, zipfile
from gdrive_utils import get_gdrive_service, download_files_from_gdrive

SCRIPT_PATH = os.path.realpath(__file__).replace("/load_articles.py", "")

#  shared Articles folder id: 1pNqtXT2mVBnHm1t9gUuD9tFoY4k3Eb2r
parent = "1pNqtXT2mVBnHm1t9gUuD9tFoY4k3Eb2r"
service, drive = get_gdrive_service()
download_files_from_gdrive(service, drive, parent, "zip", SCRIPT_PATH + os.sep + "inputs" + os.sep)

for filename in os.listdir(SCRIPT_PATH + os.sep + "inputs" + os.sep):
    f = os.path.join(SCRIPT_PATH + os.sep + "inputs" + os.sep, filename)
    if os.path.isfile(f):
        with zipfile.ZipFile(SCRIPT_PATH + os.sep + "inputs" + os.sep + filename, 'r') as zip_ref:
            zip_ref.extractall(SCRIPT_PATH + os.sep + "outputs" + os.sep)