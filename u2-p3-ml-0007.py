import numpy as np
# Alexandro Aguilar NC 0007

n0007 = np.array([10, 20, 30, 40, 50])
print(n0007)
print(n0007[0])
print(n0007[3])
print(n0007[-1])
print(n0007[-2])
print("---------------------------")
n0007 = np.array([
    [10, 20, 30],
    [40, 50, 60]
])
print(n0007)
print(n0007[0, 0])
print(n0007[1, 2])
print(n0007[-1, -1])
print(n0007[-2, -2])
print("---------------------------")
# 3D array (2x2x3)
n0007 = np.array([
    [
        [10, 20, 30],
        [40, 50, 60]
    ],
    [
        [70, 80, 90],
        [100, 110, 120]
    ]
])

print(n0007)
print(n0007[0, 0, 0])
print(n0007[1, 1, 2])
print(n0007[1, -1, -2])
print("Alexandro Aguilar NC 0007")