from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QPushButton
from utils.tools import ConfigManager, CloseByShortkey
import os
from PyQt5.QtCore import Qt

class Setting_Window(QMainWindow):
    """
    设置界面
    该页面所有组件UI在这进行(二次)封装
    """
    def __init__(self):
        super().__init__()
        self.setObjectName("Setting_Window")
                
        CloseByShortkey(self) # 启动快捷键关闭

        self.UI_Init()

    def UI_Init(self):
        # 中央组件
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        layout = QVBoxLayout()

        # "返回初页面"按钮
        self.product_info_button = QPushButton("返回初页面")
        self.product_info_button.setObjectName("product_info_button")
        layout.addWidget(self.product_info_button, alignment=Qt.AlignCenter)

        # "返回主页面"按钮
        self.main_button = QPushButton("返回主页面")
        self.main_button.setObjectName("main_button")
        layout.addWidget(self.main_button, alignment=Qt.AlignCenter)

        # 将layout布局应用到central_widget上
        self.central_widget.setLayout(layout)

        # 加载样式
        styles_qss_path = os.path.join(os.path.dirname(__file__), "../resources/styles.qss")
        self.setStyleSheet(ConfigManager.get_style(styles_qss_path))

    # 以下为该页面组件UI处理函数的封装，方便外部调用============================
    def connect_to_product_info_button(self, callback):
        """封装连接"返回初页面"按钮的槽函数"""
        self.product_info_button.clicked.connect(callback)
    
    def connect_to_main_button(self, callback):
        """封装连接"返回主页面"按钮的槽函数"""
        self.main_button.clicked.connect(callback)

