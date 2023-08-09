import matplotlib.pyplot as plt

dados = open("populacao_brasileira.csv").readlines()

ano = []
populacao = []

for i in range(len(dados)):
  if i != 0:
    linha = dados[i].split(";")
    ano.append(int(linha[0]))
    populacao.append(int(linha[1]))

title = "Crescimento da População Brasileira 1980-2016"
xAxis = "Ano"
yAxis = "População x100.000.000"

plt.title(title)
plt.xlabel(xAxis)
plt.ylabel(yAxis)

plt.bar(ano, populacao, color='#e4e4e4')
plt.plot(ano, populacao, color='k', linestyle='--')

plt.savefig("population_growth", dpi=300)
plt.show()