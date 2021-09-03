entrada = open("bacteria.fasta").readlines()
saida = open("bacteria.html","w")

cont = {}

for i in ['A', 'T', 'C', 'G']:
    for j in ['A', 'T', 'C', 'G']:
        cont[i+j] = 0

entrada = entrada.replace("\n", "")

for k in range(len(entrada)-1):
    cont[entrada[k] + entrada[k+1]] += 1

# HTML 

i = 1
for k in cont:
    saida.write("<div style='width:100px; border:1px solid #111; height:110px; float:left; background-color:rga(0, 0, 255)'> </div>")

    if i%4 == 0:
        aida.write("<div style='clear: both;'> </div>")
        
saida.close()