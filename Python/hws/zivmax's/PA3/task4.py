import numpy as np


class Matrix:

    def __init__(self, input_=[]):

        self.m = np.array(input_)
        self.r, self.c = self.m.shape

    def rotate(self, times=0, direction=-1):
        
        if direction == 1:
            times = -times

        return np.rot90(self.m, times)


    def crop(self):

        # get the size
        x = (self.r + 1) // 2
        y = (self.c + 1) // 2

        return self.m[0:x, 0:y]


    def flip(self):

        return np.flip(self.m, 1)


    def invert(self):

        # get the matrix_255 in the same size
        arr255 = np.full_like(self.m, 255)

        return np.subtract(arr255, self.m)


    @classmethod
    def get(cls):

        matrix_ = eval(input())

        return cls(matrix_)


def main():
    m = Matrix.get()

    print(m.rotate(1, 1).tolist())
    print(m.crop().tolist())
    print(m.flip().tolist())
    print(m.invert().tolist())


if __name__ == "__main__":
    main()
