"""
何恺悦 hekaiyue 2023-07-03
"""
import urllib.parse
import requests
import subprocess
import os


def text_to_audio(text, sampling_rate, speed_rate, volume_rate):
    root_dir = "storage"
    # 如果mp3文件不存在则尝试从有道api中获取一次文件
    if not os.path.exists(f"{root_dir}/{text}.mp3"):
        text_url = urllib.parse.quote(text)
        res = requests.get(f"https://dict.youdao.com/dictvoice?audio={text_url}&le=zh")
        mp3 = open(f"{root_dir}/{text}.mp3", "wb")
        mp3.write(res.content)

    # 使用ffmpeg设置音频参数
    if not os.path.exists(f"{root_dir}/{text}_{sampling_rate}_{speed_rate}_{volume_rate}.mp3"):
        subprocess.run([
            "ffmpeg", "-i", f"{root_dir}/{text}.mp3", 
            "-b:a", f"{str(sampling_rate)}k",                                       # 设置比特率
            "-filter:a", f"atempo={str(speed_rate)},volume={str(volume_rate)}",     # 设置播放速度以及音量
            f"{root_dir}/{text}_{sampling_rate}_{speed_rate}_{volume_rate}.mp3"
        ], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
text_to_audio("你好，世界", 128, 1.5, 3.0)
