import os
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.http import MediaFileUpload


# Define scopes and other constants
SCOPES = ['https://www.googleapis.com/auth/drive']
CLIENT_SECRET_FILE = 'client_secret_713297955222-k97vteamh4raorb4ut73bpa33edodifm.apps.googleusercontent.com.json'  # Path to your downloaded credentials file
API_NAME = 'drive'
API_VERSION = 'v3'

def authenticate():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json')
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return creds

def upload_file(service, file_path):
    file_metadata = {'name': os.path.basename(file_path)}
    media = MediaFileUpload(file_path)
    file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
    print('File uploaded successfully. File ID:', file.get('id'))

def main():
    creds = authenticate()
    service = build(API_NAME, API_VERSION, credentials=creds)
    upload_file(service, 'newupload.txt')

if __name__ == "__main__":
    main()
