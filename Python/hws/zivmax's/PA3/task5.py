import numpy as np


class Matrix:

    def __init__(self, input_=[]):

        self.m = np.array(input_)
        self.r, self.c = self.m.shape


    @classmethod
    def get(cls):

        matrix_ = eval(input())

        return cls(matrix_)


def main():

    x = Matrix.get()

    n = sample(x)

    y = convolution(x)

    z = histogram(x)

    print(n.tolist())
    print(y.tolist())
    print(z.tolist())


def sample(n):

    # pick the element every 2 steps and doing so every two rows.
    n = n.m[::2, ::2]

    return n


def convolution(x):

    # create a raw array as the container.
    y = np.zeros((x.r - 2, x.c - 2), dtype=int)

    # caculate
    for i in range(x.r - 2):
        for j in range(x.c - 2):
            y[i][j] = int((x.m[i][j] + x.m[i][j + 1] + x.m[i][j + 2]
                + x.m[i + 1][j] + x.m[i + 1][j + 1 ] + x.m[i + 1][j + 2] + x.m[i + 2][j]
                + x.m[i + 2][j + 1 ] + x.m[i + 2][j + 2]) / 9)

    return y


def histogram(x):

    # create a raw array as the container.
    t = np.full(16, 0)

    for i in range(16):

        t[i] = count(i, x)

    return t
    

def count(k, x):

    x = x.m.flatten()

    # filter element in range.
    s1 = x >= 16 * k
    s2 = x < 16 * k + 16

    # filter out the truth table
    s3 = s1[s2]
    s3 = s3[s3]

    # count the amount of element
    a = s3.shape

    return a[0]





if __name__ == "__main__":
    main()




