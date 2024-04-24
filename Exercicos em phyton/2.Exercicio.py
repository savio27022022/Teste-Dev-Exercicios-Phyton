import os

os.system("cls||clear")

nome:str
idade:int
primeiraNota:float
segundaNota:float
print("\n===Solicitando os dados do Usuário==\n")
primeiraNota=float(input("Digite a sua 1ª nota:"))
segundaNota=float(input("Digite a sua 2ª nota:"))
nome=input("Digite o seu nome:")
media=(primeiraNota+segundaNota)/2


print("\n===Exibindo os Resultados==\n")
print(f"Nome:{nome}")
print(f"primeira nota:{primeiraNota}")
print(f"segunda nota:{}")