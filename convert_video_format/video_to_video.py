import subprocess
import os


def video_to_video(video, target_format):
    root_dir = "storage"
    name_ext = os.path.splitext(os.path.basename(video))
    subprocess.run([
        "ffmpeg", "-i", f"{root_dir}/{video}", 
        f"{root_dir}/{name_ext[0]}{target_format}"], 
        stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )

video_to_video("input.mp4", ".avi")
