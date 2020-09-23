#Visualização de dados com Python

import matplotlib.pyplot as plt 

x = [1, 2, 5]
y = [3, 4, 6]

#Título
plt.title("Gráfico com Python")

#Eixos
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")

plt.plot(x, y)
plt.show()