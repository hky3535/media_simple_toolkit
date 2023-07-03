"""
何恺悦 hekaiyue 2023-07-03
"""
import cv2

vid_path = "test.avi"   # 输入视频文件名
pic_path = "storage"    # 输出图片文件夹路径

input_vid = cv2.VideoCapture(vid_path)
frame_count = int(input_vid.get(cv2.CAP_PROP_FRAME_COUNT)) - 1


for vid_frame_count in range(frame_count):
    ret, input_vid_read = input_vid.read()

    if not ret:
        break

    pic_full_path = f"{pic_path}/{vid_frame_count+1}.jpg"  # 当前输出的帧的完整路径
    print(f"({vid_frame_count}/{frame_count}) {pic_full_path}")
    cv2.imwrite(pic_full_path, input_vid_read)
    vid_frame_count += 1
