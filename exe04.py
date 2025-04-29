"""
4.Escreva um código que permita a leitura das notas
de uma turma de 5 alunos e guarde num vetor,
Calcular a média da turma e contar quantos
alunos obtiveram nota acima desta média
calculada Escrever a média da turma e o
resultado da contagem
"""

notas = [""]*5
somaNotas = 0

for x in range(len(notas)):
    notas[x]= float(input("Digite as notas dos alunos: \n"))

for y in range(len(notas)):
    somaNotas = somaNotas + notas[y]

media = somaNotas /5

for z in range(len(notas)):
    if notas >= 7:
        print(f"{notas}")
    elif notas<7:
        print(f"{notas}")
