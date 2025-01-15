from PyQt5.QtWidgets import QHBoxLayout, QWidget, QPushButton

class Bottom_Menu_Bar:
    """底部菜单栏"""
    def __init__(self):
        self.UI_Init()

    def UI_Init(self):
        """初始化UI"""
        self.widget = QWidget()
        self.widget.setObjectName("Bottom_Menu_Bar")

        layout = QHBoxLayout()
        layout.setContentsMargins(0, 5, 0, 5)

        layout.addStretch(1)

        self.visual_buttons = [QPushButton("视角1数据"), QPushButton("视角2数据"), QPushButton("视角3数据"), QPushButton("视角4数据")]
        for visual_button in self.visual_buttons:
            visual_button.setObjectName("visual_button")
            layout.addWidget(visual_button)
            layout.addStretch(1)

        self.widget.setLayout(layout)

    def turn_visual_button_UI(self, flag, index):
        """
        视觉数据按钮UI状态更改
        Args:
            flag==1 为选中当前页面状态,flag==0 为未选中当前页面状态;
            index: 第index个按钮
        """
        self.visual_buttons[index].setStyleSheet(
            "background-color: #040F51;" if flag else "background-color: #00469D;"
        )

    def connect_to_visual_button(self, callback, index):
        """封装连接第index个"视觉数据"按钮的槽函数"""
        self.visual_buttons[index].clicked.connect(callback)
    
    