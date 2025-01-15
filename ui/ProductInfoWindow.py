import os
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QLabel, QPushButton
from PyQt5.QtGui import QPixmap
from utils.tools import ConfigManager, CloseByShortkey

class Product_Info_Window(QMainWindow):
    """
    产品信息界面
    该页面所有组件UI在这进行(二次)封装
    """
    def __init__(self):
        super().__init__()
        self.setObjectName("Product_Info_Window")
        
        # 加载产品信息的yaml文件
        product_info_yaml_path = os.path.join(os.path.dirname(__file__), "../config/product_info.yaml")
        self.product_info = ConfigManager.get_yaml_config(product_info_yaml_path)

        CloseByShortkey(self) # 启动快捷键关闭

        self.UI_Init()

    def UI_Init(self):
        # 中央组件
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        layout = QVBoxLayout()
        layout.addStretch(10)

        # 产品名标签
        self.product_name_label = QLabel(self.product_info['product_name'])
        self.product_name_label.setObjectName("product_name_label")
        layout.addWidget(self.product_name_label, alignment=Qt.AlignCenter)
        layout.addStretch(4)
        
        # "进入"按钮
        self.enter_button = QPushButton("进入")
        self.enter_button.setObjectName("enter_button")
        layout.addWidget(self.enter_button, alignment=Qt.AlignCenter)
        layout.addStretch(4)

        # logo标签
        self.logo_label = QLabel()
        logo_path = os.path.join(os.path.dirname(__file__), "../resources/logo.png")
        logo_pixmap = QPixmap(logo_path)
        self.logo_label.setPixmap(logo_pixmap)
        self.logo_label.setScaledContents(True) # 自动缩放内容以适应部件大小
        self.logo_label.setObjectName("logo_label")
        layout.addWidget(self.logo_label, alignment=Qt.AlignCenter)
        layout.addStretch(3)

        # 公司名字标签
        self.company_name_label = QLabel(self.product_info['company_name'])        
        self.company_name_label.setObjectName("company_name_label")
        layout.addWidget(self.company_name_label, alignment=Qt.AlignCenter)
        layout.addStretch(0)

        # 产品软件版本
        self.software_version_label = QLabel(f"软件版本 : {self.product_info['software_version']}")
        self.software_version_label.setObjectName("software_version_label")
        layout.addWidget(self.software_version_label, alignment=Qt.AlignCenter)
        layout.addStretch(10)

        # 将layout布局应用到central_widget上
        self.central_widget.setLayout(layout)

        # 加载样式
        styles_qss_path = os.path.join(os.path.dirname(__file__), "../resources/styles.qss")
        self.setStyleSheet(ConfigManager.get_style(styles_qss_path))

    # 以下为该页面组件UI处理函数的封装，方便外部调用============================
    def connect_to_enter_button(self, callback):
        """封装连接"进入"按钮的槽函数"""
        self.enter_button.clicked.connect(callback)
    
    def connect_to_enter_button(self, callback):
        """封装连接"进入"按钮的槽函数"""
        self.enter_button.clicked.connect(callback)