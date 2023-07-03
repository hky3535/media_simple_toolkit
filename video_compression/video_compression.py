import subprocess
import os


def video_compression(video, compression_rate):
    root_dir = "storage"
    name_ext = os.path.splitext(os.path.basename(video))
    subprocess.run([
        "ffmpeg", "-i", f"{root_dir}/{video}", 
        "-vcodec", "libx264", "-crf", f"{str(compression_rate)}", 
        f"{root_dir}/{name_ext[0]}_{str(compression_rate)}{name_ext[1]}"], 
        stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )

# compression_rate: 0~51
video_compression("input.mp4", 51)
