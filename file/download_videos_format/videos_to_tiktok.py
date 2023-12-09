from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip
import os
import math


os.environ["IMAGEIO_FFMPEG_EXE"] = r"C:\Program Files\ImageMagick-7.1.1-Q16-HDRI\ffmpeg.exe"


os.environ["IMAGEIO_IMAGEMAGICK_BINARY"] = r"C:\Program Files\ImageMagick-7.1.0-Q16-HDRI\magick.exe"


video = VideoFileClip('video1.mp4')


segment_duration = 120


num_segments = math.ceil(video.duration / segment_duration)


for i in range(num_segments):
    start_time = i * segment_duration
    end_time = min((i + 1) * segment_duration, video.duration)
    segment = video.subclip(start_time, end_time)

    # Ajouter du texte (facultatif)
    text = f"Partie {i + 1}"
    text_clip = TextClip(text, fontsize=24, color='white')
    text_clip = text_clip.set_duration(segment.duration)
    text_clip = text_clip.set_position(('center', 'bottom'))

    segment = segment.fadein(1).fadeout(1)

    final_clip = CompositeVideoClip([segment, text_clip])

    final_clip.write_videofile(f'partie{i + 1}.mp4', codec='libx264', fps=24)
