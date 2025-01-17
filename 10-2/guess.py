from hangman import Hangman

class Guess:

    def __init__(self, word):
        # 데이터를 기록하기 위해 따로 변수를 설정
        self.secretWord = word

        self.set_word = set(self.secretWord)     # 답에 포함된 글자들의 집합
        self.guessedChars = set()    # 이미 추측에 이용된 글자들의 집합

        self.numTries = 0    # 추측 실패 횟수

        # 지금까지 알아낸 글자들과 그 위치를 가리키는 데이터를 초기화
        self.currentStatus = "_" * len(self.secretWord)


    def display(self):
        print(self.secretWord)
        print("Current: %s" %(self.currentStatus))
        print("Tries: %d \t Life: %d" %(self.numTries, Hangman().getLife()))


    def guess(self, character):
        # 추측에 사용된 글자를 guessedChars 집합에 추가
        self.guessedChars.add(character)
        # 정답에 같은 글자가 있는 개수가 1보다 클 때를 위해
        answer = self.secretWord

        # 정답에 character가 있다면,
        if character in self.secretWord:
            # 정답에 같은 글자가 있는 갯수만큼 for문
            for i in range(self.secretWord.count(character)):
                num = answer.find(character)   # character의 index값을 num 변수에 대입
                # character를 올바른 위치에 삽입
                self.currentStatus = self.currentStatus[:num] + character + self.currentStatus[num+1:]
                # answer에 character와 똑같은 부분 '_'로 바꾸기
                answer = answer[:num] + '_' + answer[num+1:]
        else:   # 실패했을 때 추측 실패 횟수 +1
            self.numTries += 1

        # 지금까지 알아낸 글자와 그 위치가 정답과 같다면 True 리턴, 그렇지 않다면 False 리턴
        if self.currentStatus == self.secretWord:
            return True
        else:
            return False
