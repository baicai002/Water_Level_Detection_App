from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel
from PyQt5.QtCore import Qt

class QHBoxLayout_Two_Label():
    """包含一个 QHBoxLayout 布局，并且布局中的左右两部分是 QLabel"""
    def __init__(self, left_text, right_text, left_style=Qt.AlignLeft, right_style=Qt.AlignRight):
        self.left_text = left_text
        self.right_text = right_text
        self.left_style = left_style
        self.right_style = right_style

        self.UI_Init()
        
    def UI_Init(self):
        self.widget = QWidget()
        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)

        # 创建左边的标签
        self.left_label = QLabel(self.left_text)
        self.left_label.setAlignment(Qt.AlignVCenter | self.left_style)
        layout.addWidget(self.left_label)

        # 创建右边的标签
        self.right_label = QLabel(self.right_text)
        self.right_label.setAlignment(Qt.AlignVCenter | self.right_style) 
        layout.addWidget(self.right_label)

        # 设置布局到widget窗口
        self.widget.setLayout(layout)
