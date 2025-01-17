from hangmanGUI import Hangman
from guessGUI import Guess
from word import Word

from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QGridLayout, QLayout
from PyQt5.QtWidgets import QTextEdit, QLineEdit, QToolButton
from PyQt5.QtCore import Qt


class HangmanGame(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.word = Word('words.txt')

        # hangman Layout : 그림
        hangmanLayout = QGridLayout()
        self.hangmanWindow = QTextEdit()
        self.hangmanWindow.setReadOnly(True)
        # 원래 왼쪽 정렬인데 중앙으로 바꾸고 싶음
        # 근데 안바꿔지는디?
        self.hangmanWindow.setAlignment(Qt.AlignCenter)
        font = self.hangmanWindow.font()
        font.setFamily('Courier New') # 고정 폭 글꼴
        self.hangmanWindow.setFont(font)
        hangmanLayout.addWidget(self.hangmanWindow, 0, 0)

        # status Layout : 현재까지 맞춘 글자, 사용한 글자 등등
        statusLayout = QGridLayout()
        self.currentWord = QLineEdit()
        self.currentWord.setReadOnly(True)
        self.currentWord.setAlignment(Qt.AlignCenter)
        font = self.currentWord.font()
        font.setPointSize(font.pointSize() + 8)
        self.currentWord.setFont(font)#다른 창들보다 조금 큰 글꼴로

        self.guessedChars = QLineEdit()
        self.guessedChars.setReadOnly(True)
        self.guessedChars.setAlignment(Qt.AlignLeft)
        # 알파벳 26개
        # 근데 띄어쓰기까지 생각하면 51개도 되지 않을까?
        self.guessedChars.setMaxLength(52)

        self.message = QLineEdit()
        self.message.setReadOnly(True)
        self.message.setAlignment(Qt.AlignLeft)
        # message 창의 setMaxLength 가 굳이 필요할까요?

        self.guessButton = QToolButton()
        self.guessButton.setText("Guess!")
        self.guessButton.clicked.connect(self.guessClicked)

        self.charInput = QLineEdit()
        self.charInput.setMaxLength(1)

        self.guessButton = QToolButton()
        self.guessButton.setText('Guess')
        self.guessButton.clicked.connect(self.guessClicked)

        self.newGameButton = QToolButton()
        self.newGameButton.setText('New Game')
        self.newGameButton.clicked.connect(self.startGame)

        # 레이아웃 배치인데
        # 0,0,1,2 뭔지 모르겠다.
        statusLayout.addWidget(self.currentWord, 0, 0, 1, 2)
        statusLayout.addWidget(self.guessedChars, 1, 0, 1, 2)
        statusLayout.addWidget(self.message, 2, 0, 1, 2)
        statusLayout.addWidget(self.guessButton, 3, 1)
        statusLayout.addWidget(self.charInput, 3, 0)
        statusLayout.addWidget(self.guessButton, 3, 1)
        statusLayout.addWidget(self.newGameButton, 4, 0)

        # 전체 Layout
        mainLayout = QGridLayout()
        mainLayout.addLayout(hangmanLayout, 0, 0)
        mainLayout.addLayout(statusLayout, 0, 1)

        self.setLayout(mainLayout)
        self.setWindowTitle('Hangman Game')

        #게임 시작
        self.startGame()

    def startGame(self):
        self.guessedChars.clear()
        self.message.clear()

        self.hangman = Hangman()
        self.guess = Guess(self.word.randFromDB(8))
        # self가 없으면 다른 함수에서 사용을 못하는 것 같음
        # startGame함수에서만 사용 가능
#        self.gameOver = False

        self.hangmanWindow.setPlaceholderText(self.hangman.currentShape())
        self.currentWord.setText(self.guess.displayCurrent())
        self.guessedChars.setText(self.guess.displayGuessed())


    def guessClicked(self):
        guessedChar = self.charInput.text()
        self.charInput.clear()
        self.message.clear()

#        if self.gameOver == True:
#            self.message.setText('GAME OVER!')
        try:

            if guessedChar in self.guess.guessedChars:
                self.message.setText("You already guessed \' %c \' " %(guessedChar))

            if self.currentWord == self.guess.secretWord:
                self.message.setText("Success!")
#                self.gameOver = True
            # 틀렸을 때 목숨 줄이기
            if not self.guess.guess(guessedChar):
                self.hangman.decreaseLife()
                self.message.setText("Remaining Life: " + str(self.hangman.getRemainingLives()))

            # self.guess.guess(guessedChar)를 호출하면서
            # guessedChars set에 사용된 character를 넣기 때문에
            # 방금 사용한 character까지 보고 싶으면 함수가 호출 된 후에 넣어야 함
            # 나머지도 비슷한 이유
            self.hangmanWindow.setText(self.hangman.currentShape())
            self.guessedChars.setText(self.guess.displayGuessed())
            self.currentWord.setText(self.guess.displayCurrent())

        except TypeError:
            self.message.setText("One character at a time!")

        # 목숨이 0일 때 게임 끝
        if self.hangman.getRemainingLives() == 0:
            self.guessedChars.setText("")
            self.message.setText("Fail! Secret Word: " + self.guess.secretWord)
            # 남은 목숨이 0개 일 때 GAME OVER랑 정답까지 한번에 다 나오게
            self.guessedChars.setText("GAME OVER!")
#            self.gameOver = True



if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    game = HangmanGame()
    game.show()
    sys.exit(app.exec_())