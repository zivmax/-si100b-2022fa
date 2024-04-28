# coding = utf-8
path = input()

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

f = open(path, "r")

rawl = f.read()

rawl = rawl.replace(",", " ").split()

f.close()

rawlc = set(rawl)

rawlc = list(rawlc)

rawlod = []

for i in rawlc:
    tmpd = {"card": 0, "sequence_main": 0, "sequence_vice": 0}
    tmpd["card"] = i
    tmpd["sequence_main"] = key1[i[1:2]]
    tmpd["sequence_vice"] = key2[i[0:1]]

    rawlod.append(tmpd)

rawlod.sort(key=lambda n: n["sequence_vice"])
rawlod.sort(key=lambda n: n["sequence_main"])

sortedl = rawlod

output = [x["card"] for x in sortedl]

output.reverse()

print(output)
