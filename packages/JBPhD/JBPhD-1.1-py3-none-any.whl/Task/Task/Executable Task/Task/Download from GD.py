import os
import pandas as pd
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from io import BytesIO
from zipfile import ZipFile


# Set up credentials (see Google Drive API docs for details)
creds = Credentials.from_authorized_user_file('Api2.json', ['https://www.googleapis.com/auth/drive'])

# Build the Drive API client
drive_service = build('drive', 'v3', credentials=creds)

# Set folder ID (you can get this from the folder URL)
folder_id = 'YOUR_FOLDER_ID'

# Define MIME type for CSV files
mime_type = 'text/csv'

# Define a function to download a file from Google Drive
def download_file(file_id):
    # Make a request to the Drive API for the file
    file = drive_service.files().get_media(fileId=file_id).execute()

    # Load the file contents into a Pandas DataFrame
    df = pd.read_csv(BytesIO(file), encoding='utf-8')

    return df

# Define a function to download all CSV files in a folder
def download_csv_files(folder_id):
    # Set up query for CSV files in folder
    query = f"'{folder_id}' in parents and mimeType='{mime_type}' and trashed=false"

    try:
        # Make a request to the Drive API for the files in the folder
        files = drive_service.files().list(q=query, fields='files(id, name)').execute().get('files', [])

        # Download each file and load it into a Pandas DataFrame
        for file in files:
            file_id = file['id']
            file_name = file['name']
            file_contents = drive_service.files().get_media(fileId=file_id).execute()
            df = pd.read_csv(BytesIO(file_contents), encoding='utf-8')

            # Print some information about the file
            print(f"Downloaded {file_name} ({len(df)} rows)")

            # Do whatever you want with the DataFrame here
            # ...

    except HttpError as error:
        print(f"An error occurred: {error}")

# Call the download_csv_files function with the folder ID
download_csv_files(folder_id)
