# media_simple_toolkit

apt install ffmpeg  
pip install moviepy  
pip install opencv-python  

### 文字转语音 convert_text_to_audio
* 文字转语音 convert_text_to_audio.py
> 使用有道词典的api进行语音生成
> 通过ffmpeg进行格式修整
### 视频压缩 video_compression
* 视频压缩 video_compression.py
> 使用ffmpeg对视频质量进行压缩
### 视频剪切拼接 video_cutting_merging
* 视频剪切 video_cutting.py
> 使用moviepy对视频的片段进行提取并保存为新的文件
* 视频拼接 video_merging.py
> 使用moviepy对视频文件进行先后拼接
* 视频墙 video_wall.py
> 使用opencv+numpy将多个视频按照类似监控的样式堆叠在同一个画面中（视频墙）
### 视频格式转换 convert_video_format
* 视频格式转换 video_to_video.py
> 使用ffmpeg将视频格式进行转换
* 视频转动图 video_to_gif.py
> 使用moviepy将视频保存为gif动图
* 视频添加音轨 video_audio_combination.py
> 使用moviepy将视频和音频进行叠加
### 视频图片转换 video_picture_conversion
* 图片拼接为视频 picture_to_video.py
> 使用opencv将图片拼接成视频
* 视频拆分为图片 video_to_picture.py
> 使用opencv将视频拆分保存为图片
