# Homework 3 Folder

Contains files needed for homework 3.

#### OCR, saving extracted text, named entity recognition and analysis (NER)
Link contains all the folders for the images, texts extracted, and tokenization from texts.
https://drive.google.com/drive/folders/1Na-wf7FhTfL_ecuyuyPh5QYxsnxMCqKI?usp=sharing

Folders:
    
    Final Images after OCR using Tesseract per day of month:
    Longcat_2000px_images 
    
    Text Extraction for three news sources into .txt formats per day of month:
    aljazeera_text
    cnn_text
    fox_text
    
    Tokenization and performing NER with SpaCY on three news sources:
    aljazeera_NER_tokenization
    cnn_NER_tokenization
    fox_NER_tokenization

Code to run split Images:
python test_longcat.py
    Requirements: python libraries
        __future__, PIL, math,os

Code to extract text: 
python extract_text.py
     Requirements: python libraries
           PIL, pytesseract, os

Code to tokenize text:
python token_text.py
    Requirements: python libraries
        spacy, os, json

#### Plot Distributions from NER 

#### Geolocation
