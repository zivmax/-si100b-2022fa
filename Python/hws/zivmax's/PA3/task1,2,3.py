import numpy as np


def integrate(f, a, b, N):

    x = np.linspace(a+(b-a)/(2*N), b-(b-a)/(2*N), N)
    fx = f(x)
    area = np.sum(fx)*(b-a)/N
    return area


class Polynomial:
    #################### Task1 #######################
    def __init__(self, coeffs):

        self.coeffs = coeffs


    def __str__(self):

        s = ''
        j = 0
        for i in self.coeffs:
            match j:
                case 0:
                    s = s + f'{i} '
                case 1:
                    s = s + f'{i}x '
                case _:
                    s = s + f'{i}x^{j} '

            # add the '+' string
            if j < len(self.coeffs) - 1:
                s = s + '+ '

            j += 1

        return s.strip()


    def deg(self):

        return (len(self.coeffs) - 1)

    #################### Task2 #######################
    def __neg__(self):

        arr = np.array(self.coeffs)
        arr = np.multiply(arr, -1)
        
        return Polynomial(arr.tolist())


    def __add__(self, other):

        arr1 = np.array(self.coeffs)
        arr2 = np.array(other.coeffs)
        pol1 = np.polynomial.Polynomial(arr1)
        pol2 = np.polynomial.Polynomial(arr2)
        pol = (pol1 + pol2)

        nlist = list(map(int, list(pol)))
        return Polynomial(nlist)   


    def __sub__(self, other):

        arr1 = np.array(self.coeffs)
        arr2 = np.array(other.coeffs)
        pol1 = np.polynomial.Polynomial(arr1)
        pol2 = np.polynomial.Polynomial(arr2)
        pol = (pol1 - pol2)

        nlist = list(map(int, list(pol)))
        return Polynomial(nlist)       


    def __mul__(self, other):

        arr1 = np.array(self.coeffs)
        arr2 = np.array(other.coeffs)
        pol1 = np.polynomial.Polynomial(arr1)
        pol2 = np.polynomial.Polynomial(arr2)
        pol = (pol1 * pol2)

        nlist = list(map(int, list(pol)))
        return Polynomial(nlist)        


    def evaluate(self, x):

        r = 0
        j = 0
        for i in self.coeffs:
            match j:
                case 0:
                    r = r + i
                case 1:
                    r = r + (i * x)
                case _:
                    r = r + i * x**j
            
            j += 1

        return r

    #################### Task3 #######################
    def derivate(self, m):

        arr = np.array(self.coeffs)
        pol = np.polynomial.Polynomial(arr)
        
        d = pol.deriv(m)

        nlist = list(map(int, list(d)))

        return  Polynomial(nlist)

    def integral(self,m):

        arr = np.array(self.coeffs)
        pol = np.polynomial.Polynomial(arr)
        
        d = pol.integ(m)

        x = lambda a : round(a,1)
        
        nlist = list(map(x, list(d)))

        return  Polynomial(nlist)
    
    def definite_integral(self,m,x1,x2):
        
        arr = np.array(self.coeffs)
        pol = np.poly1d(arr)

        result = integrate(pol, x2, x1, 1)


        return result

########## DON'T MODIFY THE CODE BELOW ##########
if __name__ == "__main__":
    print(eval(input()))