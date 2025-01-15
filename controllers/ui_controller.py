from ui import Product_Info_Window, Main_Window, Setting_Window
from utils.event_bus import EventBus

class UI_Controller:
    def __init__(self):
        self.UI_Init()
        self.set_event_bus()
        self.set_connect_slot()

    def UI_Init(self):
        # 产品信息界面
        self.product_info_window = Product_Info_Window()
        # 主界面        
        self.main_window = Main_Window()
        # 设置界面
        self.setting_window = Setting_Window()

    def set_event_bus(self):
        # 实例化事件总线（注意：事件总线的信号得去EventBus里面添加，只能定义为类属性）
        self.event_bus = EventBus()

        # 绑定总线信号到槽函数
        self.event_bus.switch_to_MainWindow_signal.connect(self.switch_to_MainWindow)
        self.event_bus.switch_to_ProductInfoWindow_signal.connect(self.switch_to_ProductInfoWindow)
        self.event_bus.switch_to_SettingWindow_signal.connect(self.witch_to_SettingWindow)
    
    def set_connect_slot(self):
        # 绑定UI信号到槽函数(product_info_window)
        self.product_info_window.connect_to_enter_button(lambda: self.event_bus.switch_to_MainWindow_signal.emit())
        
        # 绑定UI信号到槽函数(main_window)
        self.main_window.connect_to_setting_button(lambda: self.event_bus.switch_to_SettingWindow_signal.emit())
        
        # 绑定UI信号到槽函数(setting_window)
        self.setting_window.connect_to_main_button(lambda: self.event_bus.switch_to_MainWindow_signal.emit())
        self.setting_window.connect_to_product_info_button(lambda: self.event_bus.switch_to_ProductInfoWindow_signal.emit())

    def run(self):
        """启动"""
        self.switch_to_ProductInfoWindow()

    def switch_to_ProductInfoWindow(self):
        """切换到产品信息界面"""
        self.product_info_window.showFullScreen()
        if self.main_window:
            self.main_window.close()
        if self.setting_window:
            self.setting_window.close()
        
    def switch_to_MainWindow(self):
        """切换到主界面"""
        self.main_window.showFullScreen()
        if self.product_info_window:
            self.product_info_window.close()
        if self.setting_window:
            self.setting_window.close()      

    def witch_to_SettingWindow(self):
        """切换到设置"""
        self.setting_window.showFullScreen()
        if self.product_info_window:
            self.product_info_window.close()
        if self.main_window:
            self.main_window.close()

    


