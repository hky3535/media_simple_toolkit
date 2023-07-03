"""
何恺悦 hekaiyue 2023-07-03
"""
from moviepy.editor import *

video = 'video_with_no_sound.mp4'
sound = 'sound.mp3'
output = 'video_with_sound.mp4'

video = VideoFileClip(video)
sound = AudioFileClip(sound)
video = video.set_audio(sound)
video.write_videofile(output)
