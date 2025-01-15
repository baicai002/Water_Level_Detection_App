from PyQt5.QtWidgets import QShortcut
from PyQt5.QtGui import QKeySequence
import yaml

class ConfigManager():
    # def __init__(self):
        
    @staticmethod
    def get_yaml_config(config_path):
        """读取yaml配置文件

        Args:
            config_path (str): YAML配置文件的路径

        Returns:
            Union[dict, list, None]: 解析后的YAML数据，以Python字典或列表形式返回，如果读取或解析失败则返回None
        """
        try:
            with open(config_path, 'r', encoding='utf-8') as file:
                return yaml.safe_load(file)
        except FileNotFoundError:
            print(f"配置文件 {config_path} 不存在。")
            return None
        except yaml.YAMLError as e:
            print(f"解析YAML文件 {config_path} 时出错: {e}")
            return None
        
    @staticmethod
    def get_style(style_path):
        """加载样式表"""
        with open(style_path, 'r', encoding='utf-8') as file:
            return file.read()


class CloseByShortkey:
    """
    CloseByShortkey 类用于通过快捷键关闭父窗口。

    Args:
        parent_window (QWidget): 需要绑定快捷键的父窗口。
        short_key (str): 用于触发关闭操作的快捷键字符串（默认值为 "Ctrl+Alt+0"）。

    """
    def __init__(self, parent_window, short_key="Ctrl+Alt+0"):
        """快捷键关闭窗口"""
        self.parent_window = parent_window
        # 创建快捷键 Ctrl + Alt + 0 并连接父窗口的关闭方法
        self.shortcut = QShortcut(QKeySequence(short_key), self.parent_window)
        self.shortcut.activated.connect(self.parent_window.close)  # 直接连接父窗口的 close 方法
