"""
preencher um vetor A com 10 números. logo em
seguida, ler mais um número e guardar em uma
variável X.
Armazenar em um vetor M o resultado de cada elemento
de A multiplicado pelo valor X.
no final imprimir o vetor M.
"""



x = [""] * 10
for i in range(10):
    x[i] = int(input(f"Digite o {i+1}º número para o vetor A: "))

X = int(input("\nDigite o valor de X: "))

y = [0] * 10
for i in range(10):
    y[i] = x[i] * X

print("\nVetor M (A[i] * X):")
for i in range(10):
    print(f"M[{i}] = {y[i]}")
