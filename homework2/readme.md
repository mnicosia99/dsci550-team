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

Files:
    generate_fake_html.py
        script to run grover to create fake papers as html from the Bik articles as json

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
