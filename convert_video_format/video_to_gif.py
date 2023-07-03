import moviepy.editor
import os


def video_to_gif(video):
    root_dir = "storage"
    name_ext = os.path.splitext(os.path.basename(video))
    _video = moviepy.editor.VideoFileClip(f"{root_dir}/{video}")
    _video.write_gif(f"{root_dir}/{name_ext[0]}.gif")

video_to_gif("input.mp4")
