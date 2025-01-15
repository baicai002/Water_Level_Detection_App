from PyQt5.QtCore import QObject, pyqtSignal

class EventBus(QObject):
    """事件总线，用于界面之间的通信"""

    ###########################################
    # 在这定义信号，必须是类属性的
    switch_to_MainWindow_signal = pyqtSignal()
    switch_to_ProductInfoWindow_signal = pyqtSignal()
    switch_to_SettingWindow_signal = pyqtSignal()
    ###########################################

    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(EventBus, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        super().__init__()
