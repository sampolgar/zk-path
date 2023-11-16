import numpy as np
import random

y = random.randint(1, 1000)
x = random.randint(1, 1000)
out = 5*x**3 - 4*y**2*x**2 + 13*x*y**2 + x**2 - 10*y

v1 = x * x  # x^2
v2 = 5 * x * v1  # 5x^3
v3 = y * y  # y^2
v4 = 4 * v1 * v3  # 4x^2y^2
v5 = 13 * x * v3  # 13xy^2
out2 = -10 * y + v1 + v2 - v4 + v5
w = np.array([1, x, y, v1, v2, v3, v4, v5, out])

#   1,x,y,v1,v2,v3,v4,v5,out
L = np.array([
    [0, 1, 0, 0, 0, 0, 0, 0, 0],  # x
    [0, 5, 0, 0, 0, 0, 0, 0, 0],  # 5x
    [0, 0, 1, 0, 0, 0, 0, 0, 0],  # y
    [0, 0, 0, 1, 0, 0, 0, 0, 0],  # 4v1
    [0, 13, 0, 0, 0, 0, 0, 0, 0],  # 13x
    [0, 0, -10, 0, 0, 0, 0, 0, 0],  # out
])

R = np.array([
    [0, 1, 0, 0, 0, 0, 0, 0, 0],  # x
    [0, 0, 0, 1, 0, 0, 0, 0, 0],  # v1
    [0, 0, 1, 0, 0, 0, 0, 0, 0],  # y
    [0, 0, 0, 0, 0, 1, 0, 0, 0],  # v3
    [0, 0, 0, 0, 0, 1, 0, 0, 0],  # v3
    [0, 0, 1, 1, 1, 0, -1, 1, 0],  # v1 + v2 - v4 + v5
])


O = np.array([
    [0, 0, 0, 1, 0, 0, 0, 0, 0],  # v1
    [0, 0, 0, 0, 1, 0, 0, 0, 0],  # v2
    [0, 0, 0, 0, 0, 1, 0, 0, 0],  # v3
    [0, 0, 0, 0, 0, 0, 1, 0, 0],  # v4
    [0, 0, 0, 0, 0, 0, 0, 1, 0],  # v5
    [0, 0, 0, 0, 0, 0, 0, 0, 1],  # out
])

result = O.dot(w) == np.multiply(L.dot(w), R.dot(w))
assert result.all(), "result contains an inequality"