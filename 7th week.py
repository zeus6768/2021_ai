import numpy as np

# 1) scalar
a = np.array(3)

# 2) vector
b = np.array([1, 2])

# 3) 2 matrices
c1 = np.arange(1, 5).reshape(2, 2)
c2 = np.arange(-2, 2).reshape(2, 2)

# 4) 2 tensors
d1 = np.arange(1, 13).reshape(2, 2, 3)
d2 = np.arange(-5, 7).reshape(2, 3, 2)

# 5) a * b
print(f"a * b={a * b}")
print(f"a * b={np.dot(a, b)}")

# 6) b * c1, b * c2
print(f"b * c1={b * c1}")
print(f"b * c1={np.dot(b, c1)}")

print(f"b * c2={b * c2}")
print(f"b * c2={np.dot(b, c2)}")

# 7) c1 * c2
print(f"c1 * c2={c1 * c2}")
print(f"c1 * c2={np.dot(c1, c2)}")

# 8) c1 * d1
print(f"c1 * d1={c1 * d1}")
print(f"c1 * d1=\n{np.dot(c1, d1)}")

np.einsum(c1, d1)