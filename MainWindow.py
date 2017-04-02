# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.8.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(515, 177)
        MainWindow.setMinimumSize(QtCore.QSize(515, 177))
        MainWindow.setMaximumSize(QtCore.QSize(515, 177))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lblChoice = QtWidgets.QLabel(self.centralwidget)
        self.lblChoice.setGeometry(QtCore.QRect(104, 44, 139, 19))
        self.lblChoice.setObjectName("lblChoice")
        self.pushButtonRock = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonRock.setGeometry(QtCore.QRect(22, 76, 88, 27))
        self.pushButtonRock.setObjectName("pushButtonRock")
        self.pushButtonPaper = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonPaper.setGeometry(QtCore.QRect(120, 76, 88, 27))
        self.pushButtonPaper.setObjectName("pushButtonPaper")
        self.pushButtonScissors = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonScissors.setGeometry(QtCore.QRect(218, 76, 88, 27))
        self.pushButtonScissors.setObjectName("pushButtonScissors")
        self.lblIcon = QtWidgets.QLabel(self.centralwidget)
        self.lblIcon.setGeometry(QtCore.QRect(346, 20, 128, 128))
        self.lblIcon.setText("")
        self.lblIcon.setPixmap(QtGui.QPixmap("icon_question.png"))
        self.lblIcon.setObjectName("lblIcon")
        self.lblYourScoreText = QtWidgets.QLabel(self.centralwidget)
        self.lblYourScoreText.setGeometry(QtCore.QRect(28, 12, 93, 19))
        self.lblYourScoreText.setObjectName("lblYourScoreText")
        self.lblYourScore = QtWidgets.QLabel(self.centralwidget)
        self.lblYourScore.setGeometry(QtCore.QRect(118, 12, 35, 19))
        self.lblYourScore.setObjectName("lblYourScore")
        self.lblCPUScoreText = QtWidgets.QLabel(self.centralwidget)
        self.lblCPUScoreText.setGeometry(QtCore.QRect(164, 12, 85, 19))
        self.lblCPUScoreText.setObjectName("lblCPUScoreText")
        self.lblCPUScore = QtWidgets.QLabel(self.centralwidget)
        self.lblCPUScore.setGeometry(QtCore.QRect(260, 12, 68, 19))
        self.lblCPUScore.setObjectName("lblCPUScore")
        self.lblWonText = QtWidgets.QLabel(self.centralwidget)
        self.lblWonText.setGeometry(QtCore.QRect(86, 142, 183, 19))
        self.lblWonText.setText("")
        self.lblWonText.setObjectName("lblWonText")
        self.lblCPUChoice = QtWidgets.QLabel(self.centralwidget)
        self.lblCPUChoice.setGeometry(QtCore.QRect(112, 114, 133, 19))
        self.lblCPUChoice.setText("")
        self.lblCPUChoice.setObjectName("lblCPUChoice")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Rock-paper-scissors 1.0"))
        self.lblChoice.setText(_translate("MainWindow", "Pick your choice :"))
        self.pushButtonRock.setText(_translate("MainWindow", "Rock"))
        self.pushButtonPaper.setText(_translate("MainWindow", "Paper"))
        self.pushButtonScissors.setText(_translate("MainWindow", "Scissors"))
        self.lblYourScoreText.setText(_translate("MainWindow", "Your score:"))
        self.lblYourScore.setText(_translate("MainWindow", "0"))
        self.lblCPUScoreText.setText(_translate("MainWindow", "CPU score:"))
        self.lblCPUScore.setText(_translate("MainWindow", "0"))

