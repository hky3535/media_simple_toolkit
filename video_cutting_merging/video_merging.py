import moviepy.editor


root_dir = "storage"
# {待拼接文件名: (起始时间戳(小时, 分钟, 秒), 终止时间戳(小时, 分钟, 秒))}
input_videos = {
    f"{root_dir}/output_0.mp4",
    f"{root_dir}/output_1.mp4",
    f"{root_dir}/output_2.mp4",
    f"{root_dir}/output_3.mp4",
}
output_video = f"{root_dir}/output.mp4"

_output_video = moviepy.editor.concatenate_videoclips([moviepy.editor.VideoFileClip(input_video) for input_video in input_videos])
_output_video.write_videofile(output_video)
