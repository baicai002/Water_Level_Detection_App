import os
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QStackedWidget
from utils.tools import ConfigManager, CloseByShortkey
from ui.modules import Bottom_Menu_Bar, Top_Menu_Bar, Main_Page
from PyQt5.QtCore import QTimer, QDateTime

class Main_Window(QMainWindow):
    """
    主界面
    该页面所有组件UI在这进行(二次)封装
    """
    def __init__(self):
        super().__init__()
        self.setObjectName("Main_Window")
                
        CloseByShortkey(self) # 启动快捷键关闭

        self.UI_Init()

        # 时间更新
        self.start_time_update()

    def UI_Init(self):
        # 中央组件
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        layout = QVBoxLayout()
        layout.setSpacing(10) # 组件边距
        layout.setContentsMargins(0, 0, 0, 0) # 内边距：左、上、右、下

        # 顶部菜单栏
        self.top_menu_bar = Top_Menu_Bar()
        layout.addWidget(self.top_menu_bar.widget) 

        # 中间的切换页面
        self.stacked_pages = QStackedWidget()
        self.main_pages = [Main_Page("视角1数据"), Main_Page("视角2数据"), Main_Page("视角3数据"), Main_Page("视角4数据")]
        for page in self.main_pages:
            self.stacked_pages.addWidget(page.widget)

        layout.addWidget(self.stacked_pages) 
        
        # 底部菜单栏
        self.bottom_menu_bar = Bottom_Menu_Bar()
        layout.addWidget(self.bottom_menu_bar.widget)

        # 将layout布局应用到central_widget上
        self.central_widget.setLayout(layout)

        # 加载样式
        styles_qss_path = os.path.join(os.path.dirname(__file__), "../resources/styles.qss")
        self.setStyleSheet(ConfigManager.get_style(styles_qss_path))

        # 初始默认第0页
        self.switch_visual_page(0)
        # 连接切换页面的槽函数
        self.connect_to_visual_buttons()

    def start_time_update(self):
        """启动定时器以更新时间"""
        timer = QTimer(self)
        timer.timeout.connect(self.update_time)
        timer.start(1000)  # 每隔1秒更新一次时间

    def update_time(self):
        """更新时间标签"""
        current_time = QDateTime.currentDateTime()
        formatted_time = current_time.toString("yyyy年MM月dd日 HH:mm:ss")
        self.set_time_text(formatted_time)

    def switch_visual_page(self, index):
        """切换页面并高亮选中的按钮"""
        self.stacked_pages.setCurrentIndex(index)
        for i in range(len(self.main_pages)):
            self.turn_visual_button_UI(i == index, i)
    
    def switch_visual_handler(self, index):
        """返回一个函数用于处理页面切换按钮点击事件"""
        # lambda 捕获了变量 index 的引用，而不是值。如果不加这个直接循环会导致index永远是最后的值
        return lambda: self.switch_visual_page(index)

    def connect_to_visual_buttons(self):
        for i in range(len(self.main_pages)):
            self.connect_to_visual_button(self.switch_visual_handler(i), i)

    # 以下为该页面组件UI处理函数的封装，方便外部调用============================
    
    def set_time_text(self, text):
        """
        更新时间标签的文本
        格式为: 1970年01月01日 00:00:00
        """
        self.top_menu_bar.set_time_text(text)

    def set_network_status_text(self, text):
        """
        更新公网状态标签的文本
        格式为: 待定
        """
        self.top_menu_bar.set_network_status_text(text)

    def set_RSSI_text(self, text):
        """
        更新信号RSSI标签的文本
        格式为: 待定
        """
        self.top_menu_bar.set_RSSI_text(text)

    def connect_to_setting_button(self, callback):
        """封装连接"设置"按钮的槽函数"""
        self.top_menu_bar.connect_to_setting_button(callback)

    def turn_visual_button_UI(self, flag, index):
        """
        视觉数据按钮UI状态更改
        Args:
            flag==1 为选中当前页面状态,flag==0 为未选中当前页面状态;
            index: 第index个按钮
        """
        self.bottom_menu_bar.turn_visual_button_UI(flag, index)

    def connect_to_visual_button(self, callback, index):
        """封装连接第index个"视觉数据"按钮的槽函数"""
        self.bottom_menu_bar.connect_to_visual_button(callback, index)
    
    def set_main_page_cam_frame(self, frame, index):
        """
        将视频帧显示到 QLabel
        arg:
            frame: OpenCV 格式的 BGR 图像 (numpy.ndarray)
            index: 第index个页面
        """
        self.main_pages[index].video_display.set_cam_frame(frame)

    def set_main_page_cam_rotation_text(self, text, index):
        """
        更新旋转角度标签的文本
        格式为: 待定
        """
        self.main_pages[index].video_display.set_cam_rotation_text(text)

    def set_main_page_cam_pitch_text(self, text, index):
        """
        更新俯仰角度标签的文本
        格式为: 待定
        """
        self.main_pages[index].video_display.set_cam_pitch_text(text)

    def set_main_page_cam_magnification_text(self, text, index):
        """
        更新放大倍率标签的文本
        格式为: 待定
        """
        self.main_pages[index].video_display.set_cam_magnification_text(text)

    def connect_to_main_page_capture_manually_button(self, callback, index):
        """封装连接第index个main_page页面的"手动抓拍"按钮的槽函数"""
        self.main_pages[index].water_level_info.connect_to_capture_manually_button(callback)

    def set_main_page_identify_water_level_text(self, text, index):
        """
        更新第index个main_page页面"识别水位"标签的文本
        格式为: 待定
        """
        self.main_pages[index].water_level_info.set_identify_water_level_text(text)

    def set_main_page_calculate_water_level_text(self, text, index):
        """
        更新第index个main_page页面"计算水位"标签的文本
        格式为: 待定
        """
        self.main_pages[index].water_level_info.set_calculate_water_level_text(text)

    def set_main_page_base_value_of_water_level_text(self, text, index):
        """
        更新第index个main_page页面"水位基值"标签的文本
        格式为: 待定
        """
        self.main_pages[index].water_level_info.set_base_value_of_water_level_text(text)

    def set_main_page_fix_setting_text(self, text, index):
        """
        更新第index个main_page页面"修正设定"标签的文本
        格式为: 待定
        """
        self.main_pages[index].water_level_info.set_fix_setting_text(text)

    def turn_main_page_camera_status_text_and_UI(self, flag, index):
        """
        更新第index个main_page页面"摄像头状态"标签的文本和UI
        arg:
        flag: 1 显示 绿色"正常" 文本
        flag: 0 显示 白色"关闭" 文本
        """
        self.main_pages[index].water_level_info.turn_camera_status_text_and_UI(flag)

    def turn_main_page_AI_recognition_status_text_and_UI(self, flag, index):
        """
        更新第index个main_page页面"AI识别状态"标签的文本和UI
        arg:
        flag: 1 显示 绿色"正常" 文本
        flag: 0 显示 白色"关闭" 文本
        """
        self.main_pages[index].water_level_info.turn_AI_recognition_status_text_and_UI(flag)

    def turn_main_page_fill_light_status_text_and_UI(self, flag, index):
        """
        更新第index个main_page页面"补光灯状态"标签的文本和UI
        arg:
        flag: 1 显示 绿色"开启" 文本
        flag: 0 显示 白色"关闭" 文本
        """
        self.main_pages[index].water_level_info.turn_fill_light_status_text_and_UI(flag)

    def turn_main_page_infrared_status_text_and_UI(self, flag, index):
        """
        更新第index个main_page页面"红外状态"标签的文本和UI
        arg:
        flag: 1 显示 绿色"开启" 文本
        flag: 0 显示 白色"关闭" 文本
        """
        self.main_pages[index].water_level_info.turn_infrared_status_text_and_UI(flag)