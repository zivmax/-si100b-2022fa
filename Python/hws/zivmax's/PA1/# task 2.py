# task 2
# coding=utf-8


two_D_list = eval(input())

# convert 2D into 1D list
one_D_list = []

for i in two_D_list:

    for j in i:
        j = str(j)
        one_D_list.append(j)


# combine all the elements

length = len(one_D_list)

TWS = ""

for x in range(0, length):
    TWS += one_D_list[x]

print(TWS)
