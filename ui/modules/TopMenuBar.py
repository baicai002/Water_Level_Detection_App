from PyQt5.QtWidgets import QHBoxLayout, QWidget, QLabel, QPushButton
from .QHBoxLayoutTwoLabel import QHBoxLayout_Two_Label
from PyQt5.QtCore import Qt

class Top_Menu_Bar:
    """底部菜单栏"""
    def __init__(self):
        self.UI_Init()

    def UI_Init(self):
        """初始化UI"""
        self.widget = QWidget()
        self.widget.setObjectName("Top_Menu_Bar")

        layout = QHBoxLayout()
        layout.setContentsMargins(0, 5, 0, 5)

        layout.addStretch(1)

        # 时间显示
        self.time_label = QLabel("1970年01月01日 00:00:00")
        self.time_label.setObjectName("time_label")
        layout.addWidget(self.time_label)
        layout.addStretch(1)

        # 公网状态
        self.network_status = QHBoxLayout_Two_Label("公网状态:", "XXX", left_style=Qt.AlignRight, right_style=Qt.AlignLeft)
        self.network_status.left_label.setObjectName("network_status_label")
        self.network_status.right_label.setObjectName("network_status_label")
        self.network_status.widget.setObjectName("network_status_widget")
        layout.addWidget(self.network_status.widget)
        layout.addStretch(2)
        
        # 信号RSSI
        self.RSSI = QHBoxLayout_Two_Label("信号RSSI:", "XXX", left_style=Qt.AlignRight, right_style=Qt.AlignLeft)
        self.RSSI.left_label.setObjectName("RSSI_label")
        self.RSSI.right_label.setObjectName("RSSI_label")
        self.RSSI.widget.setObjectName("RSSI_widget")
        layout.addWidget(self.RSSI.widget)
        layout.addStretch(3)

        # "设置"按钮
        self.setting_button = QPushButton("设置")
        self.setting_button.setObjectName("setting_button")
        layout.addWidget(self.setting_button)
        layout.addStretch(1)

        self.widget.setLayout(layout)

    def connect_to_setting_button(self, callback):
        """封装连接"设置"按钮的槽函数"""
        self.setting_button.clicked.connect(callback)

    def set_time_text(self, text):
        """
        更新时间标签的文本
        格式为: 1970年01月01日 00:00:00
        """
        self.time_label.setText(text)

    def set_network_status_text(self, text):
        """
        更新公网状态标签的文本
        格式为: 待定
        """
        self.network_status.right_label.setText(text)

    def set_RSSI_text(self, text):
        """
        更新信号RSSI标签的文本
        格式为: 待定
        """
        self.RSSI.right_label.setText(text)