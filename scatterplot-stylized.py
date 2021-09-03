import matplotlib.pyplot as plt

x = [1, 3, 5, 7, 9]
y = [2, 3, 7, 1, 0]
z = [20, 5, 400, 33, 20]

titulo = "Scatterplot: gráfico de dispersão"
eixox = "Eixo X"
eixoy = "Eixo Y"

# Legendas 
plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)

plt.plot(x, y, color="#000000", linestyle="--")
plt.scatter(x, y, label ="Meus pontos", color="k", marker=".", s=z)
plt.legend()
plt.show()