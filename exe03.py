"""
altere o exercício anterior para permitir
achar o nome de um aluno na lista
"""

nomes=[""]*5
for x in range (len(nomes)):
    nomes [x]=(input("Digite um nome: \n"))

for j in range(len(nomes)):
    print(nomes[j],j)

meunome= input("Digite seu nome\n")

for x in range(len(nomes)):
    if meunome == nomes[x]:
        print(f"{meunome} esta na posição {x}\n")