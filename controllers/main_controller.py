from .ui_controller import UI_Controller
import cv2
from PyQt5.QtCore import QTimer

# class VideoPlayer:
#     def __init__(self, ui_controller: UI_Controller):
#         self.ui_controller = ui_controller
#         self.cap = None  # 视频捕获对象
#         self.timer = QTimer()  # 定时器
#         self.timer.timeout.connect(lambda: self.update_frame(self.index))  # 定时器触发更新帧

#     def start_camera(self, camera_index, index):
#         """启动摄像头播放"""
#         self.index = index
#         self.cap = cv2.VideoCapture(camera_index)  # 使用摄像头
#         if not self.cap.isOpened():
#             print(f"Error: 无法打开摄像头 {camera_index}")
#             return
#         self.timer.start(30)  # 每隔30ms更新帧

#     def update_frame(self, index):
#         """更新摄像头帧并显示到界面"""
#         ret, frame = self.cap.read()
#         if not ret:
#             print("无法读取摄像头帧")
#             self.timer.stop()
#             self.cap.release()
#             return

#         # 将 OpenCV 格式的帧传递给界面
#         self.ui_controller.main_window.set_main_page_cam_frame(frame, index)

#     def stop_camera(self):
#         """停止摄像头播放"""
#         self.timer.stop()
#         if self.cap:
#             self.cap.release()

class Main_Controller:
    def __init__(self):
        self.ui_controller = UI_Controller()
        
        # # 创建 VideoPlayer 对象
        # self.video_player = VideoPlayer(self.ui_controller)
        
        # self.cam_show_slot()

    def start(self):
        self.ui_controller.run()

    # def cam_show(self, x):
    #     # 启动摄像头播放
    #     self.video_player.start_camera(0, x)  # 0 表示默认摄像头

    # def cam_show_slot(self):  # 测试传入手动抓拍按钮的槽函数
    #     self.ui_controller.main_window.connect_to_main_page_capture_manually_button(lambda: self.cam_show(0), 0)
    #     self.ui_controller.main_window.connect_to_main_page_capture_manually_button(lambda: self.cam_show(1), 1)
    #     self.ui_controller.main_window.connect_to_main_page_capture_manually_button(lambda: self.cam_show(2), 2)
    #     self.ui_controller.main_window.connect_to_main_page_capture_manually_button(lambda: self.cam_show(3), 3)
