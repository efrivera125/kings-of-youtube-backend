import os
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
import pickle

SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]
CLIENT_SECRETS_FILE = "client_secret.json"  # Descarga de Google Cloud Console

def get_authenticated_service():
    credentials = None
    if os.path.exists("token.pickle"):
        with open("token.pickle", "rb") as token:
            credentials = pickle.load(token)

    if not credentials or not credentials.valid:
        flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
        credentials = flow.run_console()
        with open("token.pickle", "wb") as token:
            pickle.dump(credentials, token)

    return build("youtube", "v3", credentials=credentials)

def upload_to_youtube(clip):
    youtube = get_authenticated_service()

    request = youtube.videos().insert(
        part="snippet,status",
        body={
            "snippet": {
                "title": clip['title'],
                "description": "Clip viral automático - Kings of YouTube",
                "tags": ["viral", "streamers", "youtube", "Kings of YouTube"],
                "categoryId": "20",  # Gaming category
            },
            "status": {
                "privacyStatus": "public"
            }
        },
        media_body=MediaFileUpload(clip['clip_path'])
    )
    response = request.execute()
    print(f"Video subido: {response['id']}")
