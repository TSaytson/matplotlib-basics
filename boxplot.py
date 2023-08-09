import matplotlib.pyplot as plt
import random

vetor = []

for i in range(10):
  randomNumber = random.randint(0, 500)
  vetor.append(randomNumber)

plt.title("Boxplot")
plt.boxplot(vetor)
plt.show()