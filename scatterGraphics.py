import matplotlib.pyplot as plt

x1 = [1, 3, 5, 7, 9]
x2 = [2, 4, 6, 8, 10]
y1 = [5, 1, 3, 7, 4]
y2 = [2, 3, 7, 1, 0]
z = [200, 50, 400, 330, 100]
title = "scatterplot: dispersion graphics"
xAxis = "X axis"
yAxis = "Y axis"


plt.title(title)

plt.xlabel(xAxis)
plt.ylabel(yAxis)

plt.plot(x1, y2, color='#bbaa80', linestyle='-.')
plt.scatter(x1, y2, label = "my dots", color = "green", marker='.', s=z)
plt.legend()

plt.savefig("figura1.pdf")
plt.savefig("highDPI", dpi=1200)
plt.show()
