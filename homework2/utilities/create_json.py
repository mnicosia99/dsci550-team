import json, os, pdfkit
from gdrive_utils import download_files_from_gdrive, write_to_gdrive, get_gdrive_service

SCRIPT_PATH = os.path.realpath(__file__).replace("/create_json.py", "")
    
def create_json(source_extension, input_dir, output_dir):
    # all_papers = list()
    for filename in os.listdir(input_dir):
        afn = os.path.join(input_dir, filename)
        print(filename)
        # checking if it is a file
        if os.path.isfile(afn) and ".html" in filename:
            f = open(afn)
            line1 = f.readline()
            line2 = f.readline()
            line3 = f.readline()
            line4 = f.readline()
            line5 = f.readline()
            line6 = f.readline()
            line7 = f.readline()
            line8 = f.readline()

            title = line1.split("<body><h1>")[1].split("</h1>")[0]
            authors = line2.split("<p>Authors: ")[1].split(" </p>")[0]
            published_date = line3.split("Published Date: ")[1].split("<br/>")[0]
            affiliation = line5.split("<p>")[1].split("</p>")[0] + ", " + line6.split("<br/>")[0]
            text = line8.split("<br/><br/>")[1].split("<p><figure>")[0]
            
            paper_data = dict()
            paper_data["title"] = title
            paper_data["authors"] = authors
            paper_data["published_date"] = published_date
            paper_data["affiliation"] = affiliation
            paper_data["text"] = text
            # all_papers.append(paper_data)
        
            jsonString = json.dumps(paper_data)
            jsonFile = open(SCRIPT_PATH + os.sep + "generated" + os.sep + "json" + os.sep + filename.replace(".html", ".json"), "w")
            jsonFile.write(jsonString)
            jsonFile.close()


# parent = "1_9eRWu2AYMNx8WAUCCkBIbIKPa0KW0pe"
extension = "html"
# source_parent = "1zMiu93_g16guGlj1BEhyVVOyPCEhQx2_"
# service, drive = get_gdrive_service()

# download_files_from_gdrive(service, drive, parent, extension, SCRIPT_PATH + os.sep + extension + os.sep)
create_json(extension, SCRIPT_PATH + os.sep + extension + os.sep, SCRIPT_PATH + os.sep + "generated" + os.sep)
# write_to_gdrive(drive, source_parent, SCRIPT_PATH + os.sep + "generated" + os.sep + "pdfs" + os.sep)

# add_captions()