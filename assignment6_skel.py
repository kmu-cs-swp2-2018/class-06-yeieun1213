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


    def initUI(self):
        hbox_item = QHBoxLayout()

        itemList = ["Name:", "Age", "Score:", "Amount:"]
        self.nameLine = QLineEdit()
        self.ageLine = QLineEdit()
        self.scoreLine = QLineEdit()
        self.amountLine = QLineEdit()
        lineList = [self.nameLine, self.ageLine, self.scoreLine, self.amountLine]

        for label, line in zip(itemList, lineList):
            label = QLabel(label)
            hbox_item.addWidget(label)
            hbox_item.addWidget(line)

        ########################
        hbox_function = QHBoxLayout()

        buttonList = ["Add", "Del", "Find", "Inc", "Show"]
        connectList = [self.addButtonClicked, self.delButtonClicked, self.findButtonClicked, self.incButtonClicked, self.showButtonClicked]
        for b, c in zip(buttonList, connectList):
            button = QPushButton(b)
            hbox_function.addWidget(button)
            if b == "Inc":
                hbox_function.addStretch(1)
            button.clicked.connect(c)

        keyLabel = QLabel("key")
        self.keycombo = QComboBox()
        self.keycombo.addItems(["Name","Score"])
        hbox_function.addWidget(keyLabel)
        hbox_function.addWidget(self.keycombo)

        #######################
        resultLabel = QLabel("Result:")
        ran_vbox = QVBoxLayout()
        ran_vbox.addWidget(resultLabel)
        ran_vbox.addStretch(1)
        self.resultText = QTextEdit()
        hbox_result = QHBoxLayout()
        hbox_result.addLayout(ran_vbox)
        hbox_result.addWidget(self.resultText)

        ########################
        self.errorText = QLabel()

        vbox = QVBoxLayout()
        vbox.addLayout(hbox_item)
        vbox.addLayout(hbox_function)
        vbox.addLayout(hbox_result)
        vbox.addWidget(self.errorText)

        self.setLayout(vbox)
        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('20181710 황예은')    
        self.show()


    def addButtonClicked(self):
        self.errorText.setText('')
        try :
            record = {'Name':self.nameLine.text(), 'Age':self.ageLine.text(), 'Score':int(self.scoreLine.text())}
        except ValueError:
            result = 'ValueError : name must be str, age and score must be int'
            self.errorText.setText(result)
        except IndexError:
            result = 'IndexError : input \"add name age score\"'
            self.errorText.setText(result)
        else :
            self.scoredb += [record]
            self.showScoreDB(self.scoredb)

    def delButtonClicked(self):
        self.errorText.setText('')
        try:
            for p in self.scoredb[:]:
                if p['Name'] == self.nameLine.text():
                    self.scoredb.remove(p)
        except ValueError:
            result = 'ValueError : name must be str'
            self.errorText.setText(result)
        except IndexError:
            result = 'IndexError : input \"del name\"'
            self.errorText.setText(result)
        else:
            self.showScoreDB(self.scoredb)

    def findButtonClicked(self):
        self.errorText.setText('')
        try:
            self.showScoreDB(self.scoredb)
        except IndexError:
            result = 'IndexError : input \"find name\"'
            self.errorText.setText(result)

    def incButtonClicked(self):
        self.errorText.setText('')
        try:
            for p in self.scoredb:
                if p['Name'] == self.nameLine.text():
                    p['Score'] += int(self.amountLine.text())
        except ValueError:
            result = 'ValueError : name must be str, amount must be int'
            self.errorText.setText(result)
        except IndexError:
            result = 'IndexError : input \"inc name amount\"'
            self.errorText.setText(result)
        else:
            self.showScoreDB(self.scoredb)

    def showButtonClicked(self):
        self.errorText.setText('')
        try:
            sortKey = self.keycombo.currentText()
        except KeyError:
            result = '\'KeyError :\'' + sortKey
            self.errorText.setText(result)
        else:
            self.showScoreDB(self.scoredb, sortKey)

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

    def showScoreDB(self, scoredb, keyname=None):
        self.errorText.setText('')
        self.resultText.clear()


#        if keyname == None:
#            for p in scoredb:
#                if p['Name'] == self.nameLine.text():
#                    for attr in sorted(p):
#                        self.resultText.insertPlainText("%s = %s     " %(attr, str(p[attr])))
#                    self.resultText.insertPlainText("\n")
#            if self.resultText.toPlainText() == '':
#                result = 'we can\'t find \'%s\'' % (self.nameLine.text())
#                self.errorText.setText(result)
#            if self.nameLine.text() == '':
#                result = 'input name'
#                self.errorText.setText(result)
#        else:
##            for p in sorted(scoredb, key = lambda person: person[keyname]):
#                for attr in sorted(p):
#                    self.resultText.insertPlainText("%s = %s     " %(attr, str(p[attr])))
#                self.resultText.insertPlainText("\n")

    def showResult(self, result):
        self.resultText.clear()
        self.resultText.insertPlainText(result)


if __name__ == '__main__':    
    app = QApplication(sys.argv)
    ex = ScoreDB()
    sys.exit(app.exec_())

