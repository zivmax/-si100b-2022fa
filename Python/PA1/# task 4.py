# task 4
# coding=utf-8


a_list = list(map(int, input().split()))

n = len(a_list)
X = 0
Y = a_list[-1]

###
for i in range(1, n + 1):

    X = 1 / Y

    if i + 1 <= n:

        Y = a_list[-i - 1] + X

###


Z = 10**15

A = Y * Z

B = A % Z

A1 = A

Z1 = Z

BC = 1

while True:

    while B != 0:

        A = Z
        Z = B
        B = A % Z
        BC = Z

    B = A % Z

    A1 /= BC
    Z1 /= BC
    A = A1
    Z = Z1

    if B == 0:
        break


print(int(A1), int(Z1))
