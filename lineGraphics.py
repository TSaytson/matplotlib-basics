import matplotlib.pyplot as plt

x = [1, 2, 5]
y = [2, 3, 7]
title = "line graphics"
xAxis = "X axis"
yAxis = "Y axis"


plt.title(title)

plt.xlabel(xAxis)
plt.ylabel(yAxis)

plt.plot(x, y)
plt.show()