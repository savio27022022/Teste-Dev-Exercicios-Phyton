import os
os.system("cls||clear")

nome=input("Digite o seu nome:")
idade=int(input("Digite a sua idade:"))

primeiraNota=float(input("Digite a sua 1ª nota:"))
segundaNota=float(input("Digite a sua 2ª nota:"))
terceiraNota=float(input("Digite a sua 3ª nota:"))

media=(primeiraNota+segundaNota+terceiraNota)/3

print("===Exibindo Resultados==")
print(f"Nome:{nome}")
print(f"Idade:{idade}")
print(f"Primeira nota:{primeiraNota}")
print(f"Segunda nota:{segundaNota}")
print(f"Terceira nota:{terceiraNota}")
print(f"Média:{media}")

print("===FIM===")

if media >= 7:
    print("Aluno(a) Aprovado(a):")
else:
    print("Aluno(a) Reprovado(a):")


