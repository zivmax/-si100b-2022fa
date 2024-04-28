from random import randint
num = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
cardSet = {"D2", "C2", "H2", "S2", "D3", "C3", "H3", "S3", "D4", "C4", "H4", "S4", "D5", "C5", "H5", "S5", "D6", "C6", "H6", "S6", "D7", "C7", "H7", "S7", "D8", "C8", "H8", "S8", "D9", "C9", "H9", "S9", "DT", "CT", "HT", "ST", "DJ", "CJ", "HJ", "SJ", "DQ", "CQ", "HQ", "SQ", "DK", "CK", "HK", "SK", "DA", "CA", "HA", "SA"}

def sltCardWithCTNum(Num:str):
    isNumAvailable = False
    for i in cardSet:
        if i[1] == Num: isNumAvailable = True; break
    if not isNumAvailable: raise RuntimeError("No Availiable Card!")
    while True:
        tempOutput = cardSet.pop()
        if tempOutput[1] != Num: cardSet.add(tempOutput)
        else: return tempOutput

def main():
    with open("geninput2.txt", 'w') as f:
        a, b = randint(1, 10), randint(1, 10)
        f.write(str(a)+', '+str(b)+'\n')
        tCardNum = randint(1, 20)
        tCardList = []
        for i in range(tCardNum):
            tCardList.append(cardSet.pop())
        for i in range(len(tCardList)):
            f.write(tCardList[i])
            if i < len(tCardList)-1:
                f.write(', ')
        f.write('\n')
        i = 0
        for j in range(a):
            tCardNum = randint(1, 4)
            Num = num[randint(0, 12)]
            for i in range(tCardNum):
                f.write(sltCardWithCTNum(Num))
                if i < tCardNum-1:
                    f.write(',')
            if i < a-1:
                f.write('\n')

while True:
    try:
        main()
    except RuntimeError as e:
        print(e)
        cardSet = {"D2", "C2", "H2", "S2", "D3", "C3", "H3", "S3", "D4", "C4", "H4", "S4", "D5", "C5", "H5", "S5", "D6", "C6", "H6", "S6", "D7", "C7", "H7", "S7", "D8", "C8", "H8", "S8", "D9", "C9", "H9", "S9", "DT", "CT", "HT", "ST", "DJ", "CJ", "HJ", "SJ", "DQ", "CQ", "HQ", "SQ", "DK", "CK", "HK", "SK", "DA", "CA", "HA", "SA"}
    except KeyError as e_1:
        print(e_1)
        cardSet = {"D2", "C2", "H2", "S2", "D3", "C3", "H3", "S3", "D4", "C4", "H4", "S4", "D5", "C5", "H5", "S5", "D6", "C6", "H6", "S6", "D7", "C7", "H7", "S7", "D8", "C8", "H8", "S8", "D9", "C9", "H9", "S9", "DT", "CT", "HT", "ST", "DJ", "CJ", "HJ", "SJ", "DQ", "CQ", "HQ", "SQ", "DK", "CK", "HK", "SK", "DA", "CA", "HA", "SA"}
    else: break
print("Generate Success.")