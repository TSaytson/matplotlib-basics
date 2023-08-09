import matplotlib.pyplot as plt

x1 = [1, 3, 5, 7, 9]
x2 = [2, 4, 6, 8, 10]
y1 = [5, 1, 3, 7, 4]
y2 = [2, 3, 7, 1, 0]
title = "bars graphics"
xAxis = "X axis"
yAxis = "Y axis"


plt.title(title)

plt.xlabel(xAxis)
plt.ylabel(yAxis)

plt.bar(x1, y1, label = "Group 1")
plt.bar(x2, y2, label = "Group 2")
plt.legend()

plt.show()