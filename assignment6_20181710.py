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
        hbox_1 = QHBoxLayout()

        labelList = ["Name:", "Age:", "Score:", "Amount:"]
        for list in labelList:
            label = QLabel(list)
            hbox_1.addWidget(label)
            hbox_1.addWidget(QLineEdit(self))

        #try:
        #    nameLine.valuechanged.connect()

        ########################
        hbox_2 = QHBoxLayout()

        buttonList = ["Add", "Del", "Find", "Inc", "Show"]
        for list in buttonList:
            button = QPushButton(list)
            hbox_2.addWidget(button)
            if list == "Inc":
                hbox_2.addStretch(1)
            button.clicked.connect(self.buttonClicked)

        keyLabel = QLabel("key")
        keycombo = QComboBox(self)
        keycombo.addItems(["Name","Score"])
        hbox_2.addWidget(keyLabel)
        hbox_2.addWidget(keycombo)


        #######################3
        resultLabel = QLabel("Result:")
        resultText = QTextEdit(self)
        hbox_3 = QHBoxLayout()
        hbox_3.addWidget(resultLabel)
        hbox_3.addWidget(resultText)

        ########################
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
        if sender.text() == "Add":
            addScoreDB()

    def addScoreDB(self):


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

