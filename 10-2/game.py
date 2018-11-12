from hangman import Hangman
from guess import Guess
from word import Word

def gameMain():
    word = Word('words.txt')
    guess = Guess(word.randFromDB())

    hangman = Hangman()
    maxTries = hangman.getLife()

    while(maxTries - guess.numTries):

        display = hangman.get(maxTries - guess.numTries)
        print(display)
        guess.display()

        guessedChar = input("Select a letter:")
        if len(guessedChar) != 1:
            print("One character at a time!")
            continue
        if guessedChar in guess.guessedChars:
            print("You already guessed \' %c \' " %(guessedChar))
            continue

        if guess.guess(guessedChar) == True:
            print("Success!")
            break

    if guess.guess(guessedChar) == False:
        print(hangman.get(0))
        print("word [ %s ]" %(guess.secretWord))
        print("guess [ %s ]" %(guess.currentStatus))
        print('Fail')

if __name__ == '__main__':
    gameMain()