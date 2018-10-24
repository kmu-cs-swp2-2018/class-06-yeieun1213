from math import factorial as fact

def factorial(numStr):
    try:
        n = int(numStr)
        r = str(fact(n))
        if n != numStr:
            r = 'Error!'
            return r
    except:
        r = 'Error!'
    return r

def decToBin(numStr):
    try:
        n = int(numStr)
        r = bin(n)[2:]
    except:
        r = 'Error!'
    return r

def binToDec(numStr):
    try:
        n = int(numStr, 2)
        r = str(n)
    except:
        r = 'Error!'
    return r

def decToRoman(numStr):
    return 'dec -> Roman'

def calc(i, numStr):
    list = [factorial(numStr), decToBin(numStr), binToDec(numStr), decToRoman(numStr)]
    answer = list[i]
    return answer

if __name__ == '__main__':
    print(factorial(5),
    factorial(0),
    factorial(-1),
    factorial(3.5))
