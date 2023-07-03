"""
何恺悦 hekaiyue 2023-07-03
"""
import cv2
import numpy


class CombineFrame:
    def __init__(self):
        # 输入设置
        self.root_dir = "storage"
        self.cap_urls = {   # 设置视频路径（视频/视频流）
            0: f"{root_dir}/input_0.mp4",
            1: f"{root_dir}/input_1.mp4",
            2: f"{root_dir}/input_2.mp4",
            3: f"{root_dir}/input_3.mp4",

            4: f"{root_dir}/input_4.mp4",
            5: f"{root_dir}/input_5.mp4",
            6: f"{root_dir}/input_6.mp4",
            7: f"{root_dir}/input_7.mp4",

            8: f"{root_dir}/input_8.mp4",
            9: f"{root_dir}/input_9.mp4",
            10: f"{root_dir}/input_10.mp4",
            11: f"{root_dir}/input_11.mp4",
            12: f"{root_dir}/input_12.mp4",
            13: f"{root_dir}/input_13.mp4",
            14: f"{root_dir}/input_14.mp4",
            15: f"{root_dir}/input_15.mp4",
        }
        # 输出设置
        self.cap_rows = [   # 设置视频放置位置 空位填写None补足
            [0, 1, 2, 3],
            [4, 5, 6, 7],
            [8, 9, 10, 11],
            [None, 12, 13 , None],
            [14, 15, None, None]
        ]
        self.show_result = False    # 是否预览
        self.show_resize = 0.5      # 设置预览缩放比

        self.output_name = f"{root_dir}/output.avi"
        self.output_resize = 1  # 设置输出缩放比
        self.output_fps = 12    # 设置输出帧率

        # ===== ===== #

        self.cap_cols = self.get_cols(self.cap_rows)    # 转化成列数组
        self.caps, self.cap_shapes = self.get_caps_and_shapes()     # 得到视频的长宽和实际cap指针
        self.rows_height, self.cols_width = self.get_row_height_and_col_width(self.cap_rows, self.cap_cols, self.cap_shapes)    # 得到每行高度和每列宽度
        self.cap_yx_pos = self.get_cap_yx_pos()

        self.main()

    def get_cols(self, cap_rows):
        cap_cols = list()
        for index in range(len(cap_rows[0])):
            cap_col = list()
            for cap_row in cap_rows:
                cap_col.append(cap_row[index])
            cap_cols.append(cap_col)
        return cap_cols

    def get_caps_and_shapes(self):
        caps, cap_shapes = dict(), dict()
        for cap_url_index in self.cap_urls:
            current_cap = cv2.VideoCapture(self.cap_urls[cap_url_index])
            # 得到cap和cap的基础数据高和宽
            caps[cap_url_index] = current_cap
            cap_shapes[cap_url_index] = (int(current_cap.get(cv2.CAP_PROP_FRAME_HEIGHT)), int(current_cap.get(cv2.CAP_PROP_FRAME_WIDTH)))
        return caps, cap_shapes

    def get_row_height_and_col_width(self, cap_rows, cap_cols, cap_shapes):
        rows_height, cols_width = list(), list()
        for cap_row in cap_rows:    # 找到每行最高的画幅
            current_row_height = list()
            for cap in cap_row:
                if cap is not None:
                    current_row_height.append(cap_shapes[cap][0])
            rows_height.append(int(max(current_row_height)))
        for cap_col in cap_cols:    # 找到每列最宽的画幅
            current_col_width = list()
            for cap in cap_col:
                if cap is not None:
                    current_col_width.append(cap_shapes[cap][1])
            cols_width.append(int(max(current_col_width)))
        return rows_height, cols_width

    def get_cap_yx_pos(self):
        cap_yx_pos = dict()
        for cap_row_index, cap_row in enumerate(self.cap_rows):
            for cap_col_index, cap in enumerate(cap_row):
                start_y = sum(self.rows_height[:cap_row_index])
                start_x = sum(self.cols_width[:cap_col_index])
                # end_y = start_y + self.rows_height[cap_row_index]
                # end_x = start_x + self.cols_width[cap_col_index]
                end_y = start_y + self.cap_shapes[cap][0]
                end_x = start_x + self.cap_shapes[cap][1]
                cap_yx_pos[cap] = ((start_y, start_x), (end_y, end_x))
        # {0: ((0, 0), (1440, 2560)), 1: ((0, 2560), (1440, 5120)), 2: ((1440, 0), (2880, 2560)), 3: ((1440, 2560), (2880, 5120))}
        return cap_yx_pos

    def generate_output_frame(self):
        frame_size = (sum(self.rows_height), sum(self.cols_width))
        output_size = (int(frame_size[1] * self.output_resize), int(frame_size[0] * self.output_resize))
        show_size = (int(frame_size[1] * self.show_resize), int(frame_size[0] * self.show_resize))
        output_frame = numpy.zeros((frame_size[0], frame_size[1], 3), numpy.uint8)  # 创建一个空的输出画幅
        return frame_size, output_size, show_size, output_frame.copy()

    def main(self):
        frame_size, output_size, show_size, output_frame_init = self.generate_output_frame()

        output_vid = cv2.VideoWriter(self.output_name, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), self.output_fps, output_size)

        frame_count = 0
        ret_judge = [True] * len(self.cap_urls)     # 停止判断：全都为False之后跳出循环
        while True:     # 开始逐帧拼接
            output_frame = output_frame_init.copy()
            for ret_judge_index, cap_index in enumerate(self.cap_urls.keys()):      # 按照设定位置拼接放置画幅
                ret, cap_frame = self.caps[cap_index].read()
                if ret:
                    start_y = self.cap_yx_pos[cap_index][0][0]      # 将每个小块放置到对应的位置上
                    start_x = self.cap_yx_pos[cap_index][0][1]
                    end_y = self.cap_yx_pos[cap_index][1][0]
                    end_x = self.cap_yx_pos[cap_index][1][1]
                    output_frame[start_y:end_y, start_x:end_x] = cap_frame
                    ret_judge[ret_judge_index] = True
                else:   # 当前cap断流
                    ret_judge[ret_judge_index] = False
            if True not in ret_judge:               # 停止判断：如果所有路都停止则退出
                break
            output_frame_write = cv2.resize(output_frame.copy(), output_size)
            output_vid.write(output_frame_write)
            frame_count += 1
            print(f"(frame: {str(frame_count)})combining... stream processing: {ret_judge}")

            if self.show_result:
                output_frame_show = cv2.resize(output_frame.copy(), show_size)
                cv2.imshow("result", output_frame_show)
                wait_key = cv2.waitKey(1)
                if wait_key in [ord("Q"), ord("q")]:
                    break

        output_vid.release()


if __name__ == '__main__':
    CombineFrame()
