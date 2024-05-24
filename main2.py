import matplotlib.pyplot as plt

data = [1, 2, 2, 3, 4, 4, 4, 5, 6, 6, 6, 6, 6]

plt.hist(data, bins=6)

plt.xlabel("x ось")
plt.ylabel("y ось")
plt.title("Тестовая гистограма")

plt.show()