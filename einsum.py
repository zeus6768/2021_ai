import numpy as np

a = np.arange(8).reshape(2, 4)
b = np.arange(8).reshape(4, 2)

#print(np.dot(a, b))

# tensors
x = np.arange(24).reshape(2, 3, 4)
#print(x)

c = np.dot(a, b)
#print(c)

d = np.einsum('ik, kj -> ij', a, b)
#print(d)

aa = np.arange(9).reshape(3, 3)
#print(aa)
#e = np.einsum('ii->i', aa)
e = np.einsum('ij->i', aa)
f = np.einsum('ij->ji', aa)     # aa.T == F
#print(e)
#print(f)

a2 = np.arange(60.).reshape(3, 4, 5)
b2 = np.arange(24.).reshape(4, 3, 2)
c2 = np.einsum('ijk, jil -> kl', a2, b2)
# print(a2)
# print(b2)
# print(c2)

# Norm
u = np.array([3, -4])
# print(np.linalg.norm(u))
# print(np.abs(u).sum())


a3 = np.arange(8).reshape(2, 2, 2)
b3 = np.arange(6).reshape(1, 3, 2)

print(np.dot(b3, a3))

