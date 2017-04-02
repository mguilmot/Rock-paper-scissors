'''
    Let's play a game
    Information in README.txt
'''
import random,sys
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
from MainWindow import Ui_MainWindow

class runApplication(Ui_MainWindow):
    def __init__(self):
        self.choices=["rock","paper","scissors"]
        self._translate = QtCore.QCoreApplication.translate
        self.yourscore=0
        self.cpuscore=0
        self.run()
        self.Quit()
    def run(self):
        self.app=QApplication(sys.argv)
        self.window=QMainWindow()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.buttonactions()
        self.window.show()
        self.Quit()
    def Quit(self):
        sys.exit(self.app.exec_())
    def buttonactions(self):
        self.ui.pushButtonRock.clicked.connect(self.yourchoice_rock)
        self.ui.pushButtonPaper.clicked.connect(self.yourchoice_paper)
        self.ui.pushButtonScissors.clicked.connect(self.yourchoice_scissors)  
    def updatewon(self,who):
        if who=="you":
            self.yourscore+=1
            smiley=":-)"
            self.ui.lblIcon.setPixmap(QtGui.QPixmap("icon_won.png"))
        else:
            self.cpuscore+=1
            smiley=":-("
            self.ui.lblIcon.setPixmap(QtGui.QPixmap("icon_lost.png"))
        self.ui.lblWonText.setText(self._translate("MainWindow", who + " won this round. " + smiley))
        self.ui.lblYourScore.setText(self._translate("MainWindow", str(self.yourscore)))
        self.ui.lblCPUScore.setText(self._translate("MainWindow", str(self.cpuscore)))
    def tie(self):
        smiley=":-|"
        self.ui.lblIcon.setPixmap(QtGui.QPixmap("icon_won.png"))
        self.ui.lblWonText.setText(self._translate("MainWindow", "It's a tie ... No scores ..." + smiley))
    def cpuchoice(self):
        rand=random.randint(0,len(self.choices)-1)
        choice=self.choices[rand]
        self.ui.lblCPUChoice.setText(self._translate("MainWindow", "CPU chose: " + str(choice)))
        return choice
    def yourchoice_rock(self):
        other=self.cpuchoice()
        if other=="paper":
            self.updatewon("you")
        elif other=="rock":
            self.tie()
        else:
            self.updatewon("CPU")
    def yourchoice_paper(self):
        other=self.cpuchoice()
        if other=="paper":
            self.tie()
        elif other=="rock":
            self.updatewon("you")
        else:
            self.updatewon("CPU")
    def yourchoice_scissors(self):
        other=self.cpuchoice()
        if other=="paper":
            self.updatewon("you")
        elif other=="scissors":
            self.tie()
        else:
            self.updatewon("CPU")
if __name__=='__main__':
    runApplication()
