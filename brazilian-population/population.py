# Crescimento da população brasileira de 1980 até 2016 
# utilizando com o base o arquivo CSV da pasta 

data = open("brazilian_population.csv").readlines()

x = []
y = []

for i in range(len(data)):
    if i != 0:
        line = data[i].split(";")
        x.append(int(line[0]))
        y.append(int(line[1]))

plt.plot(x, y)
plt.title("Crescimento da população brasileira de 1980 até 2016 ")
plt.xlabel("Ano")
plt.ylabel("População x100.000.000")
plt.show()