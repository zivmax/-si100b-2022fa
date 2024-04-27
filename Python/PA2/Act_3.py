

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


# build tool cardset reader
def make_dict(cardset_list):
    lod = []

    for i in cardset_list:
        tmpd = {"card": 0, "sequence_main": 0, "sequence_vice": 0}

        tmpd["card"] = i
        tmpd["sequence_main"] = key1[i[1:2]]
        tmpd["sequence_vice"] = key2[i[0:1]]

        lod.append(tmpd)

    return lod


# put the same_sequence_main_card into one list
def integrate(cardset_list):
    # count number of the kind of card_faces
    face_count = 1
    for i in range(len(cardset_list) - 1):

        if cardset_list[i + 1]['sequence_main'] != cardset_list[i]['sequence_main']:
            face_count += 1

    # get integrated database
    list_integrated = []
    indi = 0
    for i in range(face_count):
        list_integrated.append([])

        list_integrated[i].append(cardset_list[indi])
        while indi < len(cardset_list) - 1 and cardset_list[indi + 1]['sequence_main'] == cardset_list[indi]['sequence_main']:
            list_integrated[i].append(cardset_list[indi + 1])

            indi += 1

        indi += 1

    return list_integrated


# convert 2D list into 1D list
def converter(two_D_list):
    one_D_list = []

    for i in two_D_list:
        if type(i) == list:
            for j in i:
                one_D_list.append(j)
        else:
            one_D_list.append(i)

    return one_D_list


# check whether Fullhouses or normal
def format_check(attack):
    attack = integrate(attack)

    if len(attack) == 2:

        if len(attack[0]) == 3 or len(attack[1]) == 3:

            return True

        else:
            return False

    else:
        return False


def reverse(fullhouse):
    if len(fullhouse[0]) > len(fullhouse[1]):

        return fullhouse

    else:
        fullhouses = [0, 1]
        fullhouses[1], fullhouses[0] = fullhouse

        return fullhouses


###############################################################################
# get input data
n, m = map(int, input().replace(" ", "").strip().split(","))

lines = [[]]

for i in range(n + 1):
    raw = input().replace(" ", "").strip().split(",")

    rawlod = make_dict(raw)

    rawlod.sort(key=lambda n: n["sequence_vice"])
    rawlod.sort(key=lambda n: n["sequence_main"])
    rawlod.reverse()

    lines.append(rawlod)


# get HP & rounds
HP = m

rounds = n


# get defender data
defender = {
    "HP": 0,
    "cardset": {}
}

defender['HP'] = HP

defender['cardset'] = lines[1]


# get attacks data
attacks = []

for i in lines[2:]:
    attacks.append(i)


###############################################################################


round = 1


while round <= rounds:
    # integrate defender's cardset
    integrated_cardset = integrate(defender["cardset"])

    # cardset_attack_input
    attack1 = attacks[round - 1]

    # check_cardset_format and choose the path
    if format_check(attack1):
        integrated_attack1 = reverse(integrate(attack1))

        y = 3

        list_repulse = []


        for item in integrated_attack1:
            pointer_ = False

            # searching_overcard_in_defender_cardset_in_corresponding_format
            list_tmp = []
            for x in integrated_cardset:
                if x[-1]["sequence_main"] > item[0]["sequence_main"] and len(x) >= y:
                    list_tmp.append(x)

                elif x[-1]["sequence_main"] == item[0]["sequence_main"] and len(x) >= y:
                    for i in x:
                        if i["sequence_vice"] > item[0]["sequence_vice"]:
                            list_tmp.append(i)

                else:
                    pass

            # remove format_ircorrect elements
            if len(list_tmp) > 0:
                list_tmp = integrate(converter(list_tmp))

            for i in list_tmp:
                if len(i) < y:
                    list_tmp.remove(i)

            # check whether could hit back or been hit
            if len(list_tmp) < 1:
                defender['HP'] -= 1
                print("Pass")
                round += 1
                pointer_ = True

                if defender["HP"] <= 0:
                    print("Twisted Fate lost all his HP and lost.")
                    exit()

                break

            # copy_overcard_into_list_repulse
            list_repulse.extend(converter(list_tmp)[-y:])

            list_repulse_output = []

            y -= 1

        if pointer_:
            continue

        for x in list_repulse:
            list_repulse_output.append(x['card'])

        print(list_repulse_output)

        # delete_the_corresponding_item_in_defender_cardset
        for i in list_repulse:
            defender["cardset"].remove(i)

        if len(defender["cardset"]) <= 0:
            break

        round += 1

    else:
        format = len(attack1)

        # searching_overcard_in_defender_cardset_in_corresponding_format
        list_tmp = []
        for x in integrated_cardset:
            if x[0]["sequence_main"] > attack1[0]["sequence_main"] and len(x) >= format:
                list_tmp.append(x)

            elif x[0]["sequence_main"] == attack1[0]["sequence_main"] and len(x) >= format:
                for i in x:
                    if i["sequence_vice"] > attack1[0]["sequence_vice"]:
                        list_tmp.append(i)

            else:
                pass

        # remove format_ircorrect elements
        if len(list_tmp) > 0:
            list_tmp = integrate(converter(list_tmp))

        for i in list_tmp:
            if len(i) < format:
                list_tmp.remove(i)

        # check whether could hit back or been hit
        if len(list_tmp) < 1:
            defender['HP'] -= 1
            print("Pass")
            round += 1

            if defender["HP"] <= 0:
                print("Twisted Fate lost all his HP and lost.")
                exit()

            continue

        # copy_overcard_into_list_repulse
        list_repulse = converter(list_tmp)[-format:]

        list_repulse_output = []
        for x in list_repulse:
            list_repulse_output.append(x['card'])

        # hit back
        print(list_repulse_output)

        # delete_the_corresponding_item_in_defender_cardset
        for i in list_repulse:
            defender["cardset"].remove(i)

        if len(defender["cardset"]) <= 0:
            break

        round += 1


hp = defender["HP"]
print(f"Twisted Fate won with {hp}HP left.")
