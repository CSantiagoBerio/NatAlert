# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'event-handler.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(346, 577)
        self.commentBox = QtWidgets.QTextEdit(Dialog)
        self.commentBox.setGeometry(QtCore.QRect(60, 290, 221, 201))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.commentBox.setFont(font)
        self.commentBox.setObjectName("commentBox")
        self.Comment_Box = QtWidgets.QLabel(Dialog)
        self.Comment_Box.setGeometry(QtCore.QRect(60, 270, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Comment_Box.setFont(font)
        self.Comment_Box.setObjectName("Comment_Box")
        self.locationBox = QtWidgets.QComboBox(Dialog)
        self.locationBox.setGeometry(QtCore.QRect(60, 170, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.locationBox.setFont(font)
        self.locationBox.setEditable(False)
        self.locationBox.setObjectName("locationBox")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(60, 150, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(60, 210, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.Title = QtWidgets.QLabel(Dialog)
        self.Title.setGeometry(QtCore.QRect(100, 20, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Title.setFont(font)
        self.Title.setObjectName("Title")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(60, 90, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.sendToBox = QtWidgets.QComboBox(Dialog)
        self.sendToBox.setGeometry(QtCore.QRect(60, 230, 221, 31))
        self.sendToBox.setObjectName("sendToBox")
        self.eventComboBox = QtWidgets.QComboBox(Dialog)
        self.eventComboBox.setGeometry(QtCore.QRect(60, 110, 221, 31))
        self.eventComboBox.setObjectName("eventComboBox")
        self.notificationButton = QtWidgets.QPushButton(Dialog)
        self.notificationButton.setGeometry(QtCore.QRect(100, 510, 141, 31))
        self.notificationButton.setObjectName("notificationButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.Comment_Box.setText(_translate("Dialog", "Comment Box:"))
        self.label.setText(_translate("Dialog", "Location:"))
        self.label_2.setText(_translate("Dialog", "Send To:"))
        self.Title.setText(_translate("Dialog", "Event Handler"))
        self.label_4.setText(_translate("Dialog", "Event: "))
        self.notificationButton.setText(_translate("Dialog", "Send Notification"))

