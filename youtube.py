import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
import pandas as pd
from IPython.display import JSON

API_KEY = 'AIzaSyBKENtAZHb4HDC8NlyQr9Y5A-RT6rERVb4'
channel_id = 'UC75V5b1wgQgf0cU_QN6Vw2g'

api_service_name = "youtube"
api_version = "v3"


# Get credentials and create an API client
youtube = googleapiclient.discovery.build(
    api_service_name, api_version, developerKey=API_KEY)

request = youtube.channels().list(
    part="snippet,contentDetails,statistics",
    id=','.join(channel_id)
)
response = request.execute()

print(response)