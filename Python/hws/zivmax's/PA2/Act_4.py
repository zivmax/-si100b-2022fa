# build standard database
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


# put the same_sequence_vice_card into one list
def integrate(cardset_list):
    # count number of the kind of card_faces
    face_count = 1
    for i in range(len(cardset_list) - 1):

        if cardset_list[i + 1]['sequence_vice'] != cardset_list[i]['sequence_vice']:
            face_count += 1

    # get integrated database
    list_integrated = []
    indi = 0
    for i in range(face_count):
        list_integrated.append([])

        list_integrated[i].append(cardset_list[indi])
        while indi < len(cardset_list) - 1 and cardset_list[indi + 1]['sequence_vice'] == cardset_list[indi]['sequence_vice']:
            list_integrated[i].append(cardset_list[indi + 1])

            indi += 1

        indi += 1

    return list_integrated


# convert 2D_1D_hybrid list into 1D list
def converter(two_D_list):
    one_D_list = []

    for i in two_D_list:
        if type(i) == list:
            for j in i:
                one_D_list.append(j)
        else:
            one_D_list.append(i)

    return one_D_list


def make_dict(cardset_list):
    lod = []

    for i in cardset_list:
        tmpd = {"card": 0, "sequence_main": 0, "sequence_vice": 0}

        tmpd["card"] = i
        tmpd["sequence_main"] = key1[i[1:2]]
        tmpd["sequence_vice"] = key2[i[0:1]]

        lod.append(tmpd)

    return lod


def check_sequence(i):
    for j in range(len(i) - 1):
        if i[j]["sequence_main"] != i[j + 1]["sequence_main"] + 1:
            return False
    return True


def check_flush(lod):
    cliff_count = 1
    for i in range(len(lod) - 1):

        if lod[i + 1]['sequence_main'] != lod[i]['sequence_main'] - 1:
            cliff_count += 1

    lod_integrated = []
    indi = 0
    for i in range(cliff_count):
        lod_integrated.append([])

        lod_integrated[i].append(lod[indi])

        while indi < len(lod) - 1 and lod[indi + 1]['sequence_main'] == lod[indi]['sequence_main'] - 1:
            lod_integrated[i].append(lod[indi + 1])

            indi += 1

        indi += 1

    for i in lod_integrated:
        if len(i) >= 5:
            return True
        else:
            pass

    return False


###############################################################################
raw = input().replace(" ", "").strip().split(",")

rawlod = make_dict(raw)

rawlod.sort(key=lambda n: n["sequence_main"])
rawlod.sort(key=lambda n: n["sequence_vice"])
rawlod.reverse()


###############################################################################


integrated_lod = integrate(rawlod)

for i in integrated_lod:

    if len(i) >= 5:

        if check_flush(i):
            print("True")
            exit()
else:
    print("False")
    exit()
