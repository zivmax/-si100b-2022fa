import numpy as np


class Matrix:

    def __init__(self, input_=[]):
        self.mb = np.array(input_)
        self.m, self.n = self.mb.shape

    def rotate(self, times=0, direction=-1):
        if direction == 1:
            times = -times

        return np.rot90(self.mb, times)


    def crop(self):
        x = (self.m // 2) + 1
        y = (self.n // 2) + 1

        return self.mb[0:x, 0:y]


    def flip(self):
        return np.flip(self.mb, 1)


    def invert(self):
        arr255 = np.full_like(self.mb, 255)

        return np.substract(arr255, self.mb)


    def belist(self):

        return self.mb.tolist()


    @classmethod
    def get(cls):
        matrix_ = eval(input())

        return cls(matrix_)


def main():
    m = Matrix.get()

    m.mb = m.rotate(1, 1)

    m = m.belist()

    print(m)



if __name__ == "__main__":
    main()





[[2,4,5,3,2], [1,3,4,5,1], [1,3,2,4,5,]]