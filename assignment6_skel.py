import pickle
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton,
    QHBoxLayout, QVBoxLayout, QApplication, QLabel,
    QComboBox, QTextEdit, QLineEdit)
from PyQt5.QtCore import Qt


class ScoreDB(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.dbfilename = 'assignment6.dat'
        self.scoredb = []
        self.readScoreDB()
        self.showScoreDB()

    def initUI(self):

        nameLabel = QLabel("Name:")
        nameLine = QLineEdit(self)
        ageLabel = QLabel("age:")
        ageLine = QLineEdit(self)
        scoreLabel = QLabel("score:")
        scoreLine = QLineEdit(self)
        amountLabel = QLabel("Amount:")
        amountLine = QLineEdit(self)
        list_1 = [nameLabel, nameLine, ageLabel, ageLine,
                  scoreLabel, scoreLine, amountLabel, amountLine]

        hbox_1 = QHBoxLayout()
        for s in list_1:
            hbox_1.addWidget(s)

        ###
        addButton = QPushButton("Add")
        delButton = QPushButton("Del")
        findButton = QPushButton("FInd")
        incButton = QPushButton("Inc")
        showButton = QPushButton("Show")

        keyLabel = QLabel("key")
        keycombo = QComboBox(self)
        keycombo.addItem("Name")
        keycombo.addItem("Score")
        list_2 = [addButton, delButton, findButton, incButton,
                  showButton, keyLabel, keycombo]

        hbox_2 = QHBoxLayout()
        for s in list_2:
            hbox_2.addWidget(s)
            if s == incButton:
                hbox_2.addStretch(1)
        """for i in range(0,5):
            list_2[i].clicked.connect(self.buttonClicked)
        """
        addButton.clicked.connect(self.buttonClicked)
        self.statusBar()

        ###
        resultLabel = QLabel("Result:")
        resultText = QTextEdit(self)
        hbox_3 = QHBoxLayout()
        hbox_3.addWidget(resultLabel)
        hbox_3.addWidget(resultText)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox_1)
        vbox.addLayout(hbox_2)
        vbox.addLayout(hbox_3)

        self.setLayout(vbox)
        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('20181710 황예은')    
        self.show()


    def buttonClicked(self):
        sender = self.sender()
        self.statusBar().showMessage(sender.text())



    def closeEvent(self, event):
        self.writeScoreDB()

    def readScoreDB(self):
        try:
            fH = open(self.dbfilename, 'rb')
        except FileNotFoundError as e:
            self.scoredb = []
            return

        try:
            self.scoredb =  pickle.load(fH)
        except:
            pass
        else:
            pass
        fH.close()


    # write the data into person db
    def writeScoreDB(self):
        fH = open(self.dbfilename, 'wb')
        pickle.dump(self.scoredb, fH)
        fH.close()

    def showScoreDB(self):
        pass


if __name__ == '__main__':    
    app = QApplication(sys.argv)
    ex = ScoreDB()
    sys.exit(app.exec_())

