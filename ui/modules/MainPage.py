from PyQt5.QtWidgets import QHBoxLayout, QWidget
from ui.modules import Video_Display, Water_Level_Info

class Main_Page:
    """主界面的中间的切换页面"""
    def __init__(self, page_name):
        self.page_name = page_name
        self.UI_Init()

    def UI_Init(self):
        """初始化UI"""
        self.widget = QWidget()
        self.widget.setObjectName("Main_Page")

        layout = QHBoxLayout()
        layout.setContentsMargins(10, 0, 10, 0) 
        layout.setSpacing(10) # 组件边距

        # 摄像头显示区域
        self.video_display = Video_Display(self.page_name)
        layout.addWidget(self.video_display.widget, 7)

        # 水位信息显示区域
        self.water_level_info = Water_Level_Info()
        layout.addWidget(self.water_level_info.widget, 3)

        self.widget.setLayout(layout)


    