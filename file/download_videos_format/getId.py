import os
from googleapiclient.discovery import build

# Remplacez 'YOUR_API_KEY' par votre propre clé d'API YouTube Data v3
api_key = 'AIzaSyDtJkjeqAU_PUJEn64Nt573plv8Y76ub7A'

def get_channel_id_by_name(channel_name):
    youtube = build('youtube', 'v3', developerKey=api_key)
    search_response = youtube.search().list(
        q=channel_name,
        type='channel',
        part='id',
        maxResults=1  # Vous pouvez ajuster cela en fonction de vos besoins
    ).execute()

    if 'items' in search_response:
        return search_response['items'][0]['id']['channelId']

    return None

channel_name = '@mistervofficial'  # Remplacez ceci par le nom de la chaîne que vous recherchez
channel_id = get_channel_id_by_name(channel_name)

if channel_id:
    with open('channel_id.txt', 'w') as file:
        file.write(channel_id)
    print(f"L'ID du canal '{channel_name}' a été enregistré dans channel_id.txt")
else:
    print(f"Le canal '{channel_name}' n'a pas été trouvé.")
