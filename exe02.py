"""
2.altere o exercício anterior e mostre na tela,
ao final, o nome de cada aluno e sua
respectiva posição no array.
"""

nomes=[""]*5
for x in range (len(nomes)):
    nomes [x]=(input("Digite um nome: \n"))

for j in range(len(nomes)):
    print(nomes[j],j)