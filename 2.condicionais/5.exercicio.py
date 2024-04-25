import os
os.system("cls||clear")

primeiroNumero=int(input("Digite o 1º número:"))
segundoNumero=int(input("Digite o 2º número:"))

soma=primeiroNumero+segundoNumero
media=soma/2
produto=primeiroNumero*segundoNumero

if primeiroNumero>segundoNumero:
    maiorNumero=primeiroNumero

else:
    maiorNumero=segundoNumero

if primeiroNumero<segundoNumero:
    menorNumero=primeiroNumero
else:
    menorNumero=segundoNumero

print("===Exibindo os Resultados===")
print(f"Primeiro número:{primeiroNumero}")
print(f"Segundo número:{segundoNumero}")
print(f"Soma:{soma}")
print(f"Média:{media}")
print(f"Produto:{produto}")
print(f"Maior número:{maiorNumero}")
print(f"Menor Número:{menorNumero}")








