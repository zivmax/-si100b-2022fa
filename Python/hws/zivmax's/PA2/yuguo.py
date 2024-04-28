n2 = input().replace(" ", "").strip().split(",")
list1 = []
list2 = []
faces = ["D", "C", 'H', 'S']
num = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
row = ["D1", "C1", "H1", "S1",
       "D2", "C2", "H2", "S2",
       "D3", "C3", "H3", "S3",
       "D4", "C4", "H4", "S4",
       "D5", "C5", "H5", "S5",
       "D6", "C6", "H6", "S6",
       "D7", "C7", "H7", "S7",
       "D8", "C8", "H8", "S8",
       "D9", "C9", "H9", "S9",
       "DT", "CT", "HT", "ST",
       "DJ", "CJ", "HJ", "SJ",
       "DQ", "CQ", "HQ", "SQ",
       "DK", "CK", "HK", "SK",
       "DA", "CA", "HA", "SA"]


for i in range(0, 56):
    for k in n2:
        if row[i] == k:
            list1.append(row[i])


for i in range(0, len(n2)):
    list2.append([])


for j in faces:
    for k in range(0, len(list1)):
        if list1[k][0] == j:
            list2[faces.index(j)].append(list1[k])
res = []
for ele in list2:
    if ele != []:
        res.append(ele)


def judge(res):
    p = 0
    for i in res:
        if len(i) >= 5:
            Q = 0
            for k in range(0, len(i)-1):
                if num.index(i[k][1]) + 1 == num.index(i[k + 1][1]):
                    Q += 1
                    if Q >= 4:
                        return 1
                else:
                    return 0

        if len(i) < 5:
            p += 1
        if p >= len(res):
            return 0


if judge(res) == 0:
    print("False")
if judge(res) == 1:
    print("True")
