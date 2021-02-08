import re

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QDialog, QPushButton, QLabel

from com.mvc.model.modellocator import ModelLocator
from com.mvc.view.component.gulib import GuLib
from com.mvc.view.component.max_component import MaxComponent
from com.mvc.view.component.poly import Poly
from ui.stage_ui import Ui_Form


class Stage(QMainWindow, Ui_Form):
    def __init__(self):
        super(Stage, self).__init__()
        self.setupUi(self)

        self.poly = Poly()
        self.maxMc = MaxComponent()
        self.guLib = GuLib()

        self.__init_event()

    def __init_event(self):
        self.polyBtn.clicked.connect(self.__open_poly_handler)
        self.pathBtn.clicked.connect(self.__path_click_handler)
        self.maxBtn.clicked.connect(self.__max_click_handler)  # LayaMaxUI
        self.libraryBtn.clicked.connect(self.__library_click_handler)  # 库导入
        self.pathTxt.textChanged.connect(self.__path_changed_handler)
        pass

    def __path_click_handler(self):
        directory = QFileDialog.getExistingDirectory(self, "请选择文件夹路径", "./")
        self.pathTxt.setText(directory)

    def __max_click_handler(self):
        if not self.__has_project():
            self.__dialog()
            return

        self.hide()
        self.maxMc.show()

    def __library_click_handler(self):
        if not self.__has_project():
            self.__dialog()
            return

        self.hide()
        self.guLib.show()

    def __open_poly_handler(self):
        self.hide()
        self.poly.show()

    def __path_changed_handler(self):
        ModelLocator.project = self.pathTxt.text()

    def back(self):
        self.show()

    @staticmethod
    def __has_project() -> bool:
        total = re.findall(r"[^\/]+$", ModelLocator.project)  # 项目名称
        return len(total) > 0

    @staticmethod
    def __dialog():
        dialog = QDialog()
        label = QLabel("请先选择Laya项目", dialog)
        label.move(10, 10)
        btn = QPushButton('关闭', dialog)
        btn.clicked.connect(dialog.close)
        btn.move(40, 40)
        dialog.setWindowTitle('提示')
        # dialog.setWindowFlags(Qt.MS)
        dialog.setFixedSize(140, 80)
        dialog.setWindowModality(Qt.ApplicationModal)  # 当对话框显示时，主窗口的所有控件都不可用
        dialog.exec()  # 显示对话框
