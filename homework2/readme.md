# Homework 2 Folder

Contains files needed for homework 2.

Folders:
    articles-generated: 
        contains all generated html, pdfs and json
    articles-input: 
        comntains the input articles as jsomn as extracted from the pdfs using Tika
    grover: 
        contains adapted grover code due to 1.X and 2.X issues
    utilities:
        contains various utilities used for:
            1) accessing Google Drive
            2) creating/manipulation of json
            3) creation of pdfs
            4) creasting fake names, universitirs, etc.

#### Generate Fake Paper (as HTML)
    generate_fake_html.py

    Description - This script reads the information extracted from the Bik papers and generates fake text and fake titles.  The output is a formatted html file with generated text, image and captions.  The falsified text and titles were generated using Grover and some of the code was adapted from an example on creating a fake news website (https://medium.com/swlh/how-to-create-a-fake-news-site-with-machine-learning-and-gatsby-js-e68da94256d6).  
    
    Inputs - The script reads the extracted Bik information stored as json files in the articles-input/json folder.  Each file is expected to contain the data about a single paper and there can be any number of json files in the directory.  The script also uses the generated images stored in a Google Drive and the generated cations from the articles-input/image-captions.json file.
    
    Outputs - The script will generate html files for each generated paper and store the files in the articles-generated/html folder.
    
    Exection - This script was run using a Google Colab GPU runtime.
    Google Colab Code:
    <code><i>
        from google.colab import drive
        drive.mount('/content/gdrive', force_remount=True)
        %cd /content/gdrive/MyDrive/dsci550
        !git clone https://github.com/mnicosia99/grover.git /content/gdrive/MyDrive/dsci550/grover
        %cd grover
        !python3 -m pip install regex jsonlines pdfkit faker
        %tensorflow_version 1.x
        !python3 /content/gdrive/MyDrive/dsci550/grover/generate_fake_html.py
    </i></code>

    Requirements: tensorflow

#### Generate Fake Paper PDF
    utilities/create_pdf.py

    Description - This script reads the html files generated and creates pdf for each.  
    
    Inputs - The script reads the generated html files in articles-generated/html.       Each file is expected to contain a single generated paper in html format.
    
    Outputs - The script will generate pdf files for each generated paper and store the files in the articles-generated/pdfs folder.
    
    Execution - This script can be run from command line with no arguments after installing the pdfkit module.

    Requirements: pdfkit

#### Generate Fake Paper Metadata
    utilities/fakedata.py

    Description - This script creates fake names and dates and random universities and departments for use in creating the fake papers.

    Inputs - The script reads the universities.json and majors.json to randomly create a university and department.

    Outputs - The functions return data requested.  Nothing is written to disk/file.

    Execution - This script can be run from command line with no arguments after installing the faker module.

    Requirements: faker

#### Utility Scripts
    utilities/<script_name>.py

    There were various other utility scripts created that do things such as upload/download from Google Drive and create jsonl format for falsification testing.

#### Create jsonl File
    utilities/create_jsonl.py

    Description - This script creates a jsonl file from all the json files.  
    
    Inputs - The script reads all the json files in a given directory.

    Outputs - The script will create a single jsonl file.

    Execution - This script can be run from command line with no arguments after installing the faker module.

    Requirements: None

#### Downloading the PDFs for all the Research Papers
This code was used to successfully download all of the PDF for the papers. It will save them in your default folder for downloads and it will output file_locations.json to list the file name for each DOI and missed_doi.json to list any documents that were not found successfully after the many attempts made by the program. It also uses Undetectable Chromedriver to evade cloud flare bot detection and this will require a current chrome driver to be used.

Requirements: os, requests, json, glob, time, selenium, undetected_chromedriver, chromedriver.exe, researchGate_id.py

Additional Requirements: researchGate_id.py must be edited to add a valid user name and password (You will receive 1 email to notify you that your account was accessed but I have had no issue of the account being banned - even without undetected_chromedriver). The included chromedriver.exe is version 100.0.4896.60 and it may need to be updated if it becomes too old or does not match your version of Google Chrome.

Example: <br/>

    python3 get_pdf_files.py

#### Extracting text from downloaded pdfs using Tika
This code uses Tika to extract the content/text from each of the downloaded pdfs of the papers. 

Requirements: os, tika, json

Additional Requirements: Need have access to 2 directories in the same directory as the code is run. 1- downloaded_pdfs (input directory) 2- Extracted_Text (output directory). Both directories can be downloaded from the following Google Drive: https://drive.google.com/drive/u/2/folders/15vVU--6hbwyU-oTz_b-I2k9JJbhjaMJQ 

Example: <br/>

    python3 Text_Extraction.py
    
#### Creating input JSON files for Grover Input
This code combines data from the Bik dataset, scraped data from Pubmed, and the extracted text output from Text_Extraction.py to create input JSON files for Grover that contain text and metadata for each paper. 

Requirements: os, json, requests, lxml, bs4

Additional Requirements: Need to have access to 3 directories in the same directory as the code is run. 1-Extracted_Text (input directory) 2- Metadata(Input Directory-data from Bik dataset and scraped data) 3- Grover_Input (output directory). All directories can be downloaded from the following Google Drive: https://drive.google.com/drive/u/2/folders/15vVU--6hbwyU-oTz_b-I2k9JJbhjaMJQ

Example: <br/>

    python3 Grover_Input.py 
    
#### Extracting images from downloaded pdfs 
This code extracts images from the downloaded pdfs that contain images, creates a directory named after the title of the papers, and place the extracted images in the new directory. 

Requirements: os, fitz(PyMuPDF), json 

Additional Requirements: Need to have access to 4 directories in the same directory as the code is run. 1-Extracted_Text (input directory) 2- Metadata(Input Directory-data from Bik dataset and scraped data) 3- downloaded_pdfs (input directory) 4-Extracted_Images (output directory). All directories can be downloaded from the following Google Drive: https://drive.google.com/drive/u/2/folders/15vVU--6hbwyU-oTz_b-I2k9JJbhjaMJQ

Example: <br/>

    python3 Image_Extraction.py 
    
#### DCGAN generated images
Celebrity dataset was used as input into DCGAN to generate images for our falsified pdfs. These images can be found in the following Google Drive in the folder called DCGAN_Images: https://drive.google.com/drive/u/2/folders/15vVU--6hbwyU-oTz_b-I2k9JJbhjaMJQ

#### Combining the original Bik papers with the falsified data
This code loads in the tsv from assignment 1 and appends 500 randomly generated paper data for Grover to guess on.

Example: <br/>
    
    python3 synthetic500.py
