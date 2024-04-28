import numpy as np
def integrate(f, a, b, N):
    x = np.linspace(a+(b-a)/(2*N), b-(b-a)/(2*N), N)
    fx = f(x)
    area = np.sum(fx)*(b-a)/N
    return area

x = integrate(np.sin, 0, np.pi/2, 100)

print(x)



        h = lambda x : np.polyval(pol, x)
        x = np.linspace(start, stop, length)
        y = list(map(h, x))
        result = sum(y)*(stop-start)/length