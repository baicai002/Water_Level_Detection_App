import sys
from PyQt5.QtWidgets import QApplication
from controllers import Main_Controller

if __name__ == "__main__":
    app = QApplication(sys.argv)

    main_controller = Main_Controller()
    
    main_controller.start()
    
    sys.exit(app.exec_())
