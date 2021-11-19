def f(x):
	return 3 * x ** 2 - 4 * x

def numerical_lim(f, x, h):
	return (f(x + h) - f(x)) / h

h = 0.1
for i in range(5):
	print(f'h={h:.5f}, numerical_limit={numerical_lim(f, 1, h):.5f}')
	h *= 0.1

from matplotlib.colors import LinearSegmentedColormap
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


x = [1, 2, 3]
y = [1, 2, 3]

# plt.plot(x, y)
# plt.title("My Plot")
# plt.xlabel("X")
# plt.ylabel("Y")
# plt.show()
# plt.savefig("test.png")

# x = np.linspace(0, np.pi * 10, 500)
# fig, axes = plt.subplots(2, 1)
# axes[0].plot(x, np.sin(x))
# axes[1].plot(x, np.cos(x))
# fig.savefig("sin and cos.png")

# x = np.arange(-9, 10)
# y = x ** 2
# plt.plot(x, y, linestyle=":", marker="*", color="red", label="y=x*x")
# plt.show()

x = np.linspace(0, 10, 1000)
y = np.power(x, 2)
plt.plot(x, y)
plt.show()