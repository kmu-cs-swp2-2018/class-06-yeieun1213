import random

class Word:

    def __init__(self, filename):
        # 단어 사전
        self.words = []
        f = open(filename, 'r')
        lines = f.readlines()
        f.close()

        for line in lines:
            word = line.rstrip()
            self.words.append(word)

    def test(self):
        return 'default'

    def ramFromDB(self):
    # len(self.words) : 단어 사전의 길이
    # 그 길이 숫자까지의 범위안에서 랜덤으로 임의의 수 하나를 선택
    # 사전에서 그 임의의 수에 해당하는 인덱스 값을 지닌 단어 return
        return self.words[random.randrange(len(self.words))]
