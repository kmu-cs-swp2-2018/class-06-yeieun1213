from math import factorial as fact

def factorial(numStr):
    try:
        n = int(numStr)
        r = str(fact(n))
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
    try:
        n = int(numStr)
    except:
        return 'Error!'
    
    if n>= 4000:
        return 'Error!'
    
    romans = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
         (100, 'C'),  (90, 'XC'),  (50, 'L'),  (40, 'XL'),
          (10, 'X'),   (9, 'IX'),   (5, 'V'),   (4, 'IV'),
           (1, 'I')
    ]

    result = ''
    for value, letters in romans:
        while n >= value:
            result += letters
            n -= value
    
    return result

def romanToDec(numStr):
    try:
        s = str(numStr)
    except:
        return 'Error!_!'
    if s.isalpha() == False:
        return 'Error!_!'

    romans = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'),
        (1, 'I')
    ]

    result = 0
    for value, letters in romans:
        if s == '':
            break

        while(True):
            n = s.find(letters)
            if (n == -1) or (n >= 1):
                break

            result += value

            if len(letters) == 1:
                s = s[n+1::]
            elif len(letters) == 2:
                s = s[n+2::]
            else:
                return 'Error!'

    return str(result)

if __name__ == '__main__':
    #1900
    print(romanToDec('MCM'))
    #555
    print(romanToDec('DLV'))
    #300
    print(romanToDec('CCC'))
    #23
    print(romanToDec('XXIII'))

