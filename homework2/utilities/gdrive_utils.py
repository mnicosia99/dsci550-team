from __future__ import print_function

import os
from typing import Tuple
import os.path

from google.oauth2.credentials import Credentials
from googleapiclient.errors import HttpError
from google_drive_downloader import GoogleDriveDownloader as gdd

from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import Resource
from pydrive2.drive import GoogleDrive
from pydrive2.auth import GoogleAuth

SCRIPT_PATH = os.path.realpath(__file__).replace("/gdrive_utils.py", "")
"""
    This script provides variopus utilities to download and upload files from Google Drive.
    
    To use this script you will need to privide your pown credentials files 
    which are not incl;uded in this repository.

    Dependencies: google, google_drive_downloader, pydrive2, googleapiclient
"""
# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly',
          'https://www.googleapis.com/auth/drive.file']

def get_gdrive_service() -> Tuple[Resource, GoogleDrive]:
    gauth = GoogleAuth()           
    drive = GoogleDrive(gauth)  
    
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('working/credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
            
    try:
        #  find all html files with ".html" extenstion that are in 
        #  the parent 1_9eRWu2AYMNx8WAUCCkBIbIKPa0KW0pe for Articles
        service = build('drive', 'v3', credentials=creds)
    except HttpError as error:
        print(f'An error occurred: {error}')

    t = (service, drive)
    return t

def download_files_from_gdrive(service, drive, parent, extension, output_dir):
    print(parent)
    # Google Drive v3 API
    # https://developers.google.com/drive/api/v3/reference/files/list
    try:
        nextPageToken = None
        done = False
        
        # page through results to search for files matching the extension and parent
        while not done:
            results = service.files().list(supportsAllDrives=True, includeItemsFromAllDrives=True, pageSize=1000, pageToken=nextPageToken, 
                fields="nextPageToken, files(id, name, parents, properties)").execute()
            items = results.get('files', [])
            nextPageToken = results.get('nextPageToken')

            if not items or len(items) < 1:
                print('No files found.')
                done = True
            for item in items:
                if extension in item['name'] and parent in item['parents']:
                    print(item)
                    file_obj = drive.CreateFile({'id': item['id']})
                    print(output_dir)
                    file_obj.GetContentFile(output_dir + item['name'])
            if nextPageToken == None:
                done = True
    except HttpError as error:
        print(f'An error occurred: {error}')

def write_to_gdrive(drive, parent, input_dir):
    for filename in os.listdir(input_dir):
        f = os.path.join(input_dir, filename)
        # checking if it is a file
        if os.path.isfile(f):
            options = {
                "enable-local-file-access": ""
            }    
            gfile = drive.CreateFile({'parents': [{'id': parent}]})
            # Read file and set it as the content of this instance.
            gfile.SetContentFile(input_dir + filename)
            gfile.Upload(param={'supportsTeamDrives': True})
