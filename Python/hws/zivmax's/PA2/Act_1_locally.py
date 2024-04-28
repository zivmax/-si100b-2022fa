# coding = utf-8


key1 = {
    "2": 1,
    "3": 2,
    "4": 3,
    "5": 4,
    "6": 5,
    "7": 6,
    "8": 7,
    "9": 8,
    "T": 9,
    "J": 10,
    "Q": 11,
    "K": 12,
    "A": 13,

}

key2 = {
    "D": 1,
    "C": 2,
    "H": 3,
    "S": 4,
}


f = open("D:\CS_learning\SI 100\PA2\sample1.csv", "r")


def get_raw_list():

    global rawl

    rawl = f.read()

    rawl = rawl.replace("\n", ',').split(',')



def clear():

    global rawlc

    rawlc = set(rawl)

    rawlc = list(rawlc)


def pack_into_list_of_dict():

    global rawlod

    rawlod = []

    for i in rawlc:
        tmpd = {"card": 0, "sequence_main": 0, "sequence_vice": 0}

        tmpd["card"] = i
        tmpd["sequence_main"] = key1[i[1:2]]
        tmpd["sequence_vice"] = key2[i[0:1]]

        rawlod.append(tmpd)


def sort():

    global sortedl

    rawlod.sort(key=lambda n: n["sequence_vice"])
    rawlod.sort(key=lambda n: n["sequence_main"])

    sortedl = rawlod


get_raw_list()


clear()


pack_into_list_of_dict()


sort()


[print(x) for x in sortedl]
