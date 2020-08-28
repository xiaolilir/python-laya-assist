import sys
import com.core.apps as apps
from PyQt5.QtWidgets import QApplication

from com.mvc.controller.notice import Notice


class Main:
    stage = None

    def __init__(self):
        apps.facade().startup(self)
        app = QApplication(sys.argv)
        apps.facade().sendNotification(Notice.EVENT_MAIN_INSTALL)
        sys.exit(app.exec_())
        pass


if __name__ == "__main__":
    Main()