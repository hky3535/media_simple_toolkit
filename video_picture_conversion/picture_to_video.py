"""
何恺悦 hekaiyue 2023-07-03
"""
import cv2
import os

"""
需要将待合成图片放入文件夹内

确保所有图片按照一定规律顺序排放
所有图片分辨率需要相同
视频默认存储到图片文件夹下的output.avi
"""

pic_path = "storage"  # 输入图片文件夹路径
output_path_name = "output.avi"
output_vid_fps = 12     # 设置输出视频帧率

pic_file_list = list()  # 获取图片文件名列表
for _, __, files in os.walk(pic_path):
    pic_file_list = files.copy()
pic_file_list = sorted(pic_file_list, key=lambda i: len(i), reverse=False)  # 增加排序方式保证最后文件是以windows相同方式排序的
print(pic_file_list)
input_pic_size = cv2.imread(f"{pic_path}/{pic_file_list[0]}").shape     # 根据第一帧图像获取到输出的视频分辨率
output_vid_size = (input_pic_size[1], input_pic_size[0])

# 创建输出视频句柄
output_vid = cv2.VideoWriter(output_path_name, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), output_vid_fps, output_vid_size)

pic_file_tasks_num = len(pic_file_list) - 1

for pic_file_tasks_count, pic_file in enumerate(pic_file_list):
    pic_full_path = f"{pic_path}/{pic_file}"    # 当前处理的图像完整路径
    print(f"({pic_file_tasks_count}/{pic_file_tasks_num}) {pic_full_path}")  # 输出监控信息
    pic = cv2.imread(pic_full_path)             # 读取一张图片并写入视频流
    output_vid.write(pic.copy())

output_vid.release()
