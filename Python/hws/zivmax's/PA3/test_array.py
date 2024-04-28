import numpy as np

x = np.array([16, 5, 3, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

x = x.flatten()

s1 = x >= 100
s2 = x <= 200
print(s1)
print(s2)

s3 = s1[s2]

print(s3)

s3 = s3[s3]

print(s3)
a = s3.shape
print(a[0])
