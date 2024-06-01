# upload_to_google_drive.py

import os
from Google1 import Create_Service
from googleapiclient.http import MediaFileUpload

# Constants
CLIENT_SECRET_FILE = '/app/secrets/client_secret.json'
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPES = ["https://www.googleapis.com/auth/drive"]
UPLOAD_FILE_PATH = 'newupload.txt'
OWNERS =['kmaryam@gmail.com','manasvivarma20@gmail.com','manishimmi2k3@gmail.com']  # List of users to grant ownership

def upload_to_google_drive():
    # Create Google Drive service
    service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)
    
    # Check if service is successfully created
    if service:
        # Upload file to Google Drive
        file_name = os.path.basename(UPLOAD_FILE_PATH)
        file_metadata = {'name': file_name}
        media = MediaFileUpload(UPLOAD_FILE_PATH)
        file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
        print('File uploaded successfully. File ID:', file.get('id'))
        
        # Grant ownership to specific users
        file_id = file.get('id')
        if file_id:
            try:
                for user_email in OWNERS:
                    # Define the permission (owner)
                    permission = {
                        'type': 'user',
                        'role': 'reader',
                        'emailAddress': user_email,
                        'transferOwnership': True  # Enable transferOwnership parameter
                    }
                    
                    service.permissions().create(fileId=file_id, body=permission).execute()
                    
                    print(f"Ownership granted to user '{user_email}'.")
            except Exception as e:
                print("Error occurred while granting ownership:", e)
    else:
        print('Failed to create Google Drive service. File upload aborted.')

if __name__ == "__main__":
    upload_to_google_drive()