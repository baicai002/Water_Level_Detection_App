from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QWidget, QLabel, QSizePolicy
from .QHBoxLayoutTwoLabel import QHBoxLayout_Two_Label
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QImage, QPixmap
import cv2

class Video_Display:
    """摄像头显示区域"""
    def __init__(self, page_name):
        self.page_name = page_name
        self.UI_Init()

    def UI_Init(self):
        """初始化UI"""
        self.widget = QWidget()
        self.widget.setObjectName("Video_Display")

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)
        layout.setContentsMargins(15, 15, 15, 10) 
        
        # 视频流显示标签
        self.cam_show_label = QLabel(self.page_name)
        self.cam_show_label.setAlignment(Qt.AlignCenter)
        self.cam_show_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.cam_show_label.setObjectName("cam_show_label")
        layout.addWidget(self.cam_show_label)

        # 摄像头控制区域QWidget=====================================
        self.cam_contrller_widget = QWidget()
        self.cam_contrller_widget.setObjectName("cam_contrller_widget")
        cam_contrller_layout = QHBoxLayout()
        cam_contrller_layout.setContentsMargins(0, 0, 0, 0) 

        cam_contrller_layout.addStretch(1)
        
        # 旋转角度
        self.cam_rotation = QHBoxLayout_Two_Label("旋转角度:", "XXXX", left_style=Qt.AlignRight, right_style=Qt.AlignLeft)
        self.cam_rotation.left_label.setObjectName("cam_param_label")
        self.cam_rotation.right_label.setObjectName("cam_param_label")
        self.cam_rotation.widget.setObjectName("cam_param_widget")
        cam_contrller_layout.addWidget(self.cam_rotation.widget)
        cam_contrller_layout.addStretch(1)

        # 俯仰角度
        self.cam_pitch = QHBoxLayout_Two_Label("俯仰角度:", "XXXX", left_style=Qt.AlignRight, right_style=Qt.AlignLeft)
        self.cam_pitch.left_label.setObjectName("cam_param_label")
        self.cam_pitch.right_label.setObjectName("cam_param_label")
        self.cam_pitch.widget.setObjectName("cam_param_widget")
        cam_contrller_layout.addWidget(self.cam_pitch.widget)
        cam_contrller_layout.addStretch(1)

        # 放大倍率
        self.cam_magnification =  QHBoxLayout_Two_Label("放大倍率:", "XXXX", left_style=Qt.AlignRight, right_style=Qt.AlignLeft)
        self.cam_magnification.left_label.setObjectName("cam_param_label")
        self.cam_magnification.right_label.setObjectName("cam_param_label")
        self.cam_magnification.widget.setObjectName("cam_param_widget")
        cam_contrller_layout.addWidget(self.cam_magnification.widget)

        cam_contrller_layout.addStretch(1)

        self.cam_contrller_widget.setLayout(cam_contrller_layout)

        layout.addWidget(self.cam_contrller_widget)
        # 摄像头控制区域QWidget=====================================

        self.widget.setLayout(layout)

    def set_cam_frame(self, frame):
        """
        将视频帧显示到 QLabel
        :param frame: OpenCV 格式的 BGR 图像 (numpy.ndarray)
        """
        if frame is not None:
            # 将 BGR 图像转换为 RGB 格式
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # 获取 QLabel 的大小
            label_size = self.cam_show_label.size()
            # label_width = label_size.width()
            # label_height = label_size.height()
            # 写死了，因为layout会更改size，但是这里假如自动获取，会导致
            # label_width和label_height和实际窗口不匹配，后面再考虑优化
            # 这里固定值根据1024*600px屏幕得到的
            label_width = 666 
            label_height = 420 

            # 调整图像大小以适应 QLabel
            frame_resized = cv2.resize(frame_rgb, (label_width, label_height))

            # 获取图像的高度、宽度和通道
            h, w, ch = frame_resized.shape
            bytes_per_line = ch * w

            # print(f"{label_height} {label_width} {h} {w}")

            # 创建 QImage
            q_image = QImage(frame_resized.data, w, h, bytes_per_line, QImage.Format_RGB888)

            # 设置到 QLabel
            self.cam_show_label.setPixmap(QPixmap.fromImage(q_image))

    def set_cam_rotation_text(self, text):
        """
        更新旋转角度标签的文本
        格式为: 待定
        """
        self.cam_rotation.right_label.setText(text)

    def set_cam_pitch_text(self, text):
        """
        更新俯仰角度标签的文本
        格式为: 待定
        """
        self.cam_pitch.right_label.setText(text)

    def set_cam_magnification_text(self, text):
        """
        更新放大倍率标签的文本
        格式为: 待定
        """
        self.cam_magnification.right_label.setText(text)