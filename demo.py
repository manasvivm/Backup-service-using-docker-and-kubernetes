from Google1 import Create_Service

CLIENT_SECRET_FILE = 'client_secret_973996084206-ekfl5srpg0ltadc3gsr0ascuafe69hoq.apps.googleusercontent.com.json'
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPES = ["https://www.googleapis.com/auth/drive"]

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION,SCOPES)

print(dir(service))

