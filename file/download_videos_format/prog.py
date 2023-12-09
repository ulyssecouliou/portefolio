import os
from googleapiclient.discovery import build

# Remplacez 'YOUR_API_KEY' par votre propre clé d'API YouTube Data v3
api_key = 'AIzaSyDtJkjeqAU_PUJEn64Nt573plv8Y76ub7A'

def get_youtube_links(channel_id):
    youtube = build('youtube', 'v3', developerKey=api_key)
    response = youtube.channels().list(id=channel_id, part='contentDetails').execute()
    uploads_playlist_id = response['items'][0]['contentDetails']['relatedPlaylists']['uploads']

    video_links = []
    next_page_token = None

    while True:
        playlist_response = youtube.playlistItems().list(
            playlistId=uploads_playlist_id,
            part='snippet',
            maxResults=50,  # Vous pouvez ajuster cela en fonction de vos besoins
            pageToken=next_page_token
        ).execute()

        for item in playlist_response['items']:
            video_id = item['snippet']['resourceId']['videoId']
            video_links.append(f'https://www.youtube.com/watch?v={video_id}')

        next_page_token = playlist_response.get('nextPageToken')

        if not next_page_token:
            break

    return video_links

channel_id = 'UC_x5XG1OV2P6uZZ5FSM9Ttw'  # Remplacez ceci par l'ID du canal que vous souhaitez scraper
global_youtube_links = get_youtube_links(channel_id)

# Écrire les liens dans un fichier texte
with open('youtube_links.txt', 'w') as file:
    for link in global_youtube_links:
        file.write(link + '\n')

print("Les liens ont été enregistrés dans youtube_links.txt")
