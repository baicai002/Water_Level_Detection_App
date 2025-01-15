from PyQt5.QtWidgets import QGridLayout, QWidget, QLabel, QVBoxLayout, QPushButton
from .QHBoxLayoutTwoLabel import QHBoxLayout_Two_Label
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
import os

class Water_Level_Info:
    """水位信息显示区域"""
    def __init__(self):
        self.UI_Init()

    def UI_Init(self):
        """初始化UI"""
        self.widget = QWidget()
        self.widget.setObjectName("Water_Level_Info")

        layout = QGridLayout()
        layout.setContentsMargins(10, 5, 10, 10) 

        # 波浪icon
        self.wave_icon_label = QLabel()
        wave_icon_path = os.path.join(os.path.dirname(__file__), "../../resources/wave_ico.png")
        logo_pixmap = QPixmap(wave_icon_path) 
        self.wave_icon_label.setPixmap(logo_pixmap)
        self.wave_icon_label.setScaledContents(True)
        self.wave_icon_label.setObjectName("wave_icon_label")
        layout.addWidget(self.wave_icon_label, 0, 1, 1 ,1)
        
        # 水位识别信息标题label
        self.water_level_title_label = QLabel("水位识别信息")
        self.water_level_title_label.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        self.water_level_title_label.setObjectName("water_level_title_label")
        layout.addWidget(self.water_level_title_label, 0, 2, 1, 3)

        # 识别水位
        self.identify_water_level = QHBoxLayout_Two_Label("识别水位:", "XXXXm", left_style=Qt.AlignLeft, right_style=Qt.AlignRight)
        self.identify_water_level.left_label.setObjectName("identify_and_calculate_left_label")
        self.identify_water_level.right_label.setObjectName("identify_and_calculate_right_label")
        self.identify_water_level.widget.setObjectName("identify_and_calculate_widget")
        layout.addWidget(self.identify_water_level.widget, 1, 0, 1, 6)

        # 计算水位
        self.calculate_water_level = QHBoxLayout_Two_Label("计算水位:", "XXXXm", left_style=Qt.AlignLeft, right_style=Qt.AlignRight) 
        self.calculate_water_level.left_label.setObjectName("identify_and_calculate_left_label")
        self.calculate_water_level.right_label.setObjectName("identify_and_calculate_right_label")
        self.calculate_water_level.widget.setObjectName("identify_and_calculate_widget")
        layout.addWidget(self.calculate_water_level.widget, 2, 0, 1, 6)

        # 水位信息其他部分，用一个QWidget装载==============
        self.other_info_widget = QWidget() 
        self.other_info_widget.setObjectName("other_info_widget")
        other_info_widget_layout = QVBoxLayout()
        other_info_widget_layout.setContentsMargins(15, 2, 15, 5)

        # 水位基值
        self.base_value_of_water_level = QHBoxLayout_Two_Label("水位基值:", "XXXXm", left_style=Qt.AlignLeft, right_style=Qt.AlignRight) 
        self.base_value_of_water_level.left_label.setObjectName("other_info_left_label")
        self.base_value_of_water_level.right_label.setObjectName("other_info_right_label")
        self.base_value_of_water_level.widget.setObjectName("other_info_label_widget")
        other_info_widget_layout.addWidget(self.base_value_of_water_level.widget)

        # 修正设定
        self.fix_setting = QHBoxLayout_Two_Label ("修正设定:", "XXXXm", left_style=Qt.AlignLeft, right_style=Qt.AlignRight) 
        self.fix_setting.left_label.setObjectName("other_info_left_label")
        self.fix_setting.right_label.setObjectName("other_info_right_label")
        self.fix_setting.widget.setObjectName("other_info_label_widget")
        other_info_widget_layout.addWidget(self.fix_setting.widget)

        # 摄像头状态
        self.camera_status = QHBoxLayout_Two_Label("摄像头状态:", "关闭", left_style=Qt.AlignLeft, right_style=Qt.AlignRight) 
        self.camera_status.left_label.setObjectName("other_info_left_label")
        self.camera_status.right_label.setObjectName("other_info_right_label")
        self.camera_status.widget.setObjectName("other_info_label_widget")
        other_info_widget_layout.addWidget(self.camera_status.widget)

        # AI识别状态
        self.AI_recognition_status = QHBoxLayout_Two_Label("AI识别状态:", "关闭", left_style=Qt.AlignLeft, right_style=Qt.AlignRight) 
        self.AI_recognition_status.left_label.setObjectName("other_info_left_label")
        self.AI_recognition_status.right_label.setObjectName("other_info_right_label")
        self.AI_recognition_status.widget.setObjectName("other_info_label_widget")
        other_info_widget_layout.addWidget(self.AI_recognition_status.widget)

        # 补光灯状态
        self.fill_light_status = QHBoxLayout_Two_Label("补光灯状态:", "关闭", left_style=Qt.AlignLeft, right_style=Qt.AlignRight) 
        self.fill_light_status.left_label.setObjectName("other_info_left_label")
        self.fill_light_status.right_label.setObjectName("other_info_right_label")
        self.fill_light_status.widget.setObjectName("other_info_label_widget")
        other_info_widget_layout.addWidget(self.fill_light_status.widget)

        # 红外状态
        self.infrared_status = QHBoxLayout_Two_Label("红外状态:", "关闭", left_style=Qt.AlignLeft, right_style=Qt.AlignRight) 
        self.infrared_status.left_label.setObjectName("other_info_left_label")
        self.infrared_status.right_label.setObjectName("other_info_right_label")
        self.infrared_status.widget.setObjectName("other_info_label_widget")
        other_info_widget_layout.addWidget(self.infrared_status.widget)

        # "手动抓拍"按钮
        self.capture_manually_button = QPushButton("手动抓拍")
        self.capture_manually_button.setObjectName("capture_manually_button")
        other_info_widget_layout.addWidget(self.capture_manually_button)

        self.other_info_widget.setLayout(other_info_widget_layout)
        layout.addWidget(self.other_info_widget, 3, 0, 7, 6)
        # 水位信息其他部分，用一个QWidget装载=============

        self.widget.setLayout(layout)

    def set_identify_water_level_text(self, text):
        """
        更新"识别水位"标签的文本
        格式为: 待定
        """
        self.identify_water_level.right_label.setText(text)

    def set_calculate_water_level_text(self, text):
        """
        更新"计算水位"标签的文本
        格式为: 待定
        """
        self.calculate_water_level.right_label.setText(text)

    def set_base_value_of_water_level_text(self, text):
        """
        更新"水位基值"标签的文本
        格式为: 待定
        """
        self.base_value_of_water_level.right_label.setText(text)

    def set_fix_setting_text(self, text):
        """
        更新"修正设定"标签的文本
        格式为: 待定
        """
        self.fix_setting.right_label.setText(text)

    def turn_camera_status_text_and_UI(self, flag):
        """
        更新"摄像头状态"标签的文本和UI
        arg:
        flag: 1 显示 绿色"正常" 文本
        flag: 0 显示 白色"关闭" 文本
        """
        self.camera_status.right_label.setText("正常" if flag else "关闭")
        self.camera_status.right_label.setStyleSheet(
            "color: green;" if flag else "background-color: white;"
        )

    def turn_AI_recognition_status_text_and_UI(self, flag):
        """
        更新"AI识别状态"标签的文本和UI
        arg:
        flag: 1 显示 绿色"正常" 文本
        flag: 0 显示 白色"关闭" 文本
        """
        self.AI_recognition_status.right_label.setText("正常" if flag else "关闭")
        self.AI_recognition_status.right_label.setStyleSheet(
            "color: lightgreen;" if flag else "background-color: white;"
        )

    def turn_fill_light_status_text_and_UI(self, flag):
        """
        更新"补光灯状态"标签的文本和UI
        arg:
        flag: 1 显示 绿色"开启" 文本
        flag: 0 显示 白色"关闭" 文本
        """
        self.fill_light_status.right_label.setText("正常" if flag else "关闭")
        self.fill_light_status.right_label.setStyleSheet(
            "color: lightgreen;" if flag else "background-color: white;"
        )

    def turn_infrared_status_text_and_UI(self, flag):
        """
        更新"红外状态"标签的文本和UI
        arg:
        flag: 1 显示 绿色"开启" 文本
        flag: 0 显示 白色"关闭" 文本
        """
        self.infrared_status.right_label.setText("正常" if flag else "关闭")
        self.infrared_status.right_label.setStyleSheet(
            "color: green;" if flag else "background-color: white;"
        )

    def connect_to_capture_manually_button(self, callback):
        """封装连接"手动抓拍"按钮的槽函数"""
        self.capture_manually_button.clicked.connect(callback)
    