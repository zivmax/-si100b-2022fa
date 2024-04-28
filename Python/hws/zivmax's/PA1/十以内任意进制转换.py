# coding=utf-8


x = int(input("System of Numeration: "))
dec = int(input("Input: "))

i = 0
o = 0
y = x**i

while True:
    i = 0
    y = x**i

    while y < dec:
        i += 1
        y = x**i

    if y == dec:
        o += 1 * 10**i
        break

    i -= 1
    y = x**i
    dec -= y

    if dec < 0:
        break

    o += 1 * 10**i

print("Output:", o)
