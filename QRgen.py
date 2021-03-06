# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\panther\Desktop\qrgen.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_EasyQR_main(object):
    def setupUi(self, EasyQR_main):
        EasyQR_main.setObjectName("EasyQR_main")
        EasyQR_main.resize(728, 309)
        self.centralwidget = QtWidgets.QWidget(EasyQR_main)
        self.centralwidget.setObjectName("centralwidget")
        self.data_textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.data_textEdit.setGeometry(QtCore.QRect(30, 100, 371, 61))
        self.data_textEdit.setObjectName("data_textEdit")
        self.data_label = QtWidgets.QLabel(self.centralwidget)
        self.data_label.setGeometry(QtCore.QRect(30, 60, 131, 31))
        self.data_label.setObjectName("data_label")
        self.Button_data_qr = QtWidgets.QPushButton(self.centralwidget)
        self.Button_data_qr.setGeometry(QtCore.QRect(30, 180, 131, 31))
        self.Button_data_qr.setCheckable(False)
        self.Button_data_qr.setObjectName("Button_data_qr")
        self.Button_clipbd_qr = QtWidgets.QPushButton(self.centralwidget)
        self.Button_clipbd_qr.setGeometry(QtCore.QRect(190, 180, 211, 31))
        self.Button_clipbd_qr.setObjectName("Button_clipbd_qr")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(30, 90, 118, 3))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.qr_show = QtWidgets.QLabel(self.centralwidget)
        self.qr_show.setGeometry(QtCore.QRect(440, 20, 231, 231))
        self.qr_show.setObjectName("qr_show")
        EasyQR_main.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(EasyQR_main)
        self.statusbar.setObjectName("statusbar")
        EasyQR_main.setStatusBar(self.statusbar)
        self.actionabout = QtWidgets.QAction(EasyQR_main)
        self.actionabout.setObjectName("actionabout")

        self.retranslateUi(EasyQR_main)
        QtCore.QMetaObject.connectSlotsByName(EasyQR_main)

    def retranslateUi(self, EasyQR_main):
        _translate = QtCore.QCoreApplication.translate
        EasyQR_main.setWindowTitle(_translate("EasyQR_main", "EasyQR"))
        self.data_label.setText(_translate("EasyQR_main", "Some Data:"))
        self.Button_data_qr.setText(_translate("EasyQR_main", "Generate!"))
        self.Button_clipbd_qr.setText(_translate("EasyQR_main", "Generate from clipboard"))
        self.qr_show.setText(_translate("EasyQR_main", "qr_show"))
        self.actionabout.setText(_translate("EasyQR_main", "about"))



import qrcode
from PIL import Image,ImageQt
import pyperclip
from PyQt5 import QtCore,QtGui,uic,QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
# from ui import Ui_EasyQR_main
import sys


class myapp(QtWidgets.QMainWindow,Ui_EasyQR_main):
    def __init__(self,parent=None):
        super(myapp,self).__init__(parent)
        self.setupUi(self)
        self.Button_data_qr.clicked.connect(self.data_qr)
        self.Button_clipbd_qr.clicked.connect(self.clipbd_qr)
    
    def data_qr(self):
        data = self.data_textEdit.toPlainText()
        print(data)
        # self.qr_show.setPixmap(QPixmap(self.makeqr(data)))
        qpix = QPixmap.fromImage(self.makeqr(data))
        self.qr_show.setScaledContents(True)
        self.qr_show.setPixmap(qpix)

    def clipbd_qr(self):
        data = pyperclip.paste()
        print(data)
        qpix = QPixmap.fromImage(self.makeqr(data))
        self.qr_show.setScaledContents(True)
        self.qr_show.setPixmap(qpix)

    def makeqr(self,data):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=2
        )
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill_color = "black",back_color = "white")
        qimg = ImageQt.ImageQt(img)
        return qimg
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = myapp()
    window.show()
    sys.exit(app.exec_())
