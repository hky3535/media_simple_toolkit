import moviepy.editor


root_dir = "storage"
input_video = f"{root_dir}/input.mp4"
# {待拆分文件名: (起始时间戳(小时, 分钟, 秒), 终止时间戳(小时, 分钟, 秒))}
output_videos = {
    f"{root_dir}/output_0.mp4": ((0, 0, 2), (0, 0, 6)),
    f"{root_dir}/output_1.mp4": ((0, 0, 4), (0, 0, 8)),
    f"{root_dir}/output_2.mp4": ((0, 0, 6), (0, 0, 7)),
    f"{root_dir}/output_3.mp4": ((0, 0, 8), (0, 0, 9)),
}

_input_video = moviepy.editor.VideoFileClip(input_video)
for output_video in output_videos:
    output_video_clip = _input_video.subclip(
        t_start=output_videos[output_video][0], 
        t_end=output_videos[output_video][1]
    )
    output_video_clip.write_videofile(output_video)
    output_video_clip.reader.close()
