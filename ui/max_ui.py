# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'max_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(612, 352)
        self.checkAll = QtWidgets.QCheckBox(Form)
        self.checkAll.setGeometry(QtCore.QRect(30, 10, 101, 20))
        self.checkAll.setObjectName("checkAll")
        self.listView = QtWidgets.QListView(Form)
        self.listView.setGeometry(QtCore.QRect(30, 40, 551, 281))
        self.listView.setObjectName("listView")
        self.copyBtn = QtWidgets.QPushButton(Form)
        self.copyBtn.setGeometry(QtCore.QRect(460, 5, 120, 32))
        self.copyBtn.setObjectName("copyBtn")
        self.totalTxt = QtWidgets.QLabel(Form)
        self.totalTxt.setGeometry(QtCore.QRect(190, 10, 221, 20))
        self.totalTxt.setAlignment(QtCore.Qt.AlignCenter)
        self.totalTxt.setObjectName("totalTxt")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(30, 330, 551, 20))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.skinsTxt = QtWidgets.QLabel(self.widget)
        self.skinsTxt.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.skinsTxt.setObjectName("skinsTxt")
        self.horizontalLayout.addWidget(self.skinsTxt)
        self.resTxt = QtWidgets.QLabel(self.widget)
        self.resTxt.setAlignment(QtCore.Qt.AlignCenter)
        self.resTxt.setObjectName("resTxt")
        self.horizontalLayout.addWidget(self.resTxt)
        self.unpackTxt = QtWidgets.QLabel(self.widget)
        self.unpackTxt.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.unpackTxt.setObjectName("unpackTxt")
        self.horizontalLayout.addWidget(self.unpackTxt)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Laya - 路径拷贝"))
        self.checkAll.setText(_translate("Form", " 待定的文件"))
        self.copyBtn.setText(_translate("Form", "拷贝到剪切板"))
        self.totalTxt.setText(_translate("Form", "项目名称"))
        self.skinsTxt.setText(_translate("Form", "[skins] 0条记录"))
        self.resTxt.setText(_translate("Form", "[res] 0条记录"))
        self.unpackTxt.setText(_translate("Form", "[unpack] 0条记录"))