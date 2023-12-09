import os
from pytube import YouTube
from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip

youtube_url = 'https://www.youtube.com/watch?v=sofdx4DWkWU'


def download_youtube_video(youtube_url):
    yt = YouTube(youtube_url)
    stream = yt.streams.get_highest_resolution()
    video_file = stream.download(output_path='.')
    return video_file


video_file = download_youtube_video(youtube_url)


def rename_files():
    i = 1
    for file_name in os.listdir():
        if file_name.endswith('.mp4'):
            os.rename(file_name, f'video{i}.mp4')
            i += 1


rename_files()
