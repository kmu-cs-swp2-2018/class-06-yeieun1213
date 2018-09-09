import pickle

dbfilename = 'assignment3.dat'

def readScoreDB():
    try:
        fH = open(dbfilename, 'rb')
    except FileNotFoundError as e:
        print("New DB: ", dbfilename)
        return []

    scdb = []
    try:
        scdb =  pickle.load(fH)
        for p in scdb:
            p['Age'] = int(p['Age'])
            p['Score'] = int(p['Score'])

    except:
        print("Empty DB: ", dbfilename)
    else:
        print("Open DB: ", dbfilename)
    fH.close()
    return scdb


# write the data into person db
def writeScoreDB(scdb):
    fH = open(dbfilename, 'wb')
    pickle.dump(scdb, fH)
    fH.close()


def doScoreDB(scdb):
    while(True):
        inputstr = (input("Score DB > "))
        if inputstr == "": continue
        parse = inputstr.split(" ")
        if parse[0] == 'add':
            # ㅇㅖㅇㅗㅣ ㅊㅓㄹㅣ
            try :
                record = {'Name':parse[1], 'Age':int(parse[2]), 'Score':int(parse[3])}
            except ValueError:
                print('ValueError : name must be str, age and score must be int')
            except IndexError:
                print('IndexError : input \"add name age score\"')
            else :
                scdb += [record]

        # del 'break'
        elif parse[0] == 'del':
            try:
                for p in scdb:
                    if p['Name'] == parse[1]:
                        scdb.remove(p)
            except IndexError:
                print('IndexError : input \"del name\"')
            else:
                if parse[1] not in p['Name']:
                    print('Does not exist')
        elif parse[0] == 'show':
            try:
                sortKey ='Name' if len(parse) == 1 else parse[1]
                showScoreDB(scdb, sortKey)
            except KeyError:
                print('KeyError :', sortKey)

        elif parse[0] == 'quit':
            break

        elif parse[0] == 'find':
            try:
                for p in scdb:
                    if p['Name'] == parse[1]:
                        for attr in p:
                                #must be str, not int
                                print(attr + "=" + str(p[attr]), end=' ')
                        print()
            except IndexError:
                print('IndexError : input \"find name\"')

        elif parse[0] == 'inc':
            try:
                name = str(parse[1])
                amount = int(parse[2])
            except ValueError:
                print('ValueError : name must be str, amount must be int')
            except IndexError:
                print('IndexError : input \"inc name amount\"')
            else:
                for p in scdb:
                    if p['Name'] == name:
                        p['Score'] += amount
                if name not in p['Name']:
                    print('name does not exist')

        else:
            print("Invalid command: " + parse[0])


def showScoreDB(scdb, keyname):
    for p in sorted(scdb, key=lambda person: person[keyname]):
        for attr in sorted(p):
            # must be str, not int
            print(attr + "=" + str(p[attr]), end=' ')
        print()


scoredb = readScoreDB()
doScoreDB(scoredb)
writeScoreDB(scoredb)
