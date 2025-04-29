"""1.Criar um array tamanho 5 e preencher com
os nomes dos 5 alunos, informados pelo
usuário"""

nomes=[""]*5
for x in range (len(nomes)):
    nomes [x]=(input("Digite um nome: \n"))

print(nomes)