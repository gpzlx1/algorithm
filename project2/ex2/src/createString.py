import random   

def createString(length):
    letter = [chr(i) for i in range(65, 91)]
    retString = ''
    for i in range(length):
        retString = retString + str(random.sample(letter, 1)[0])
    return retString

