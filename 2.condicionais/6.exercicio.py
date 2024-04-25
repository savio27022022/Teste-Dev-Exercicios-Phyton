import os
os.system("cls||clear")

loginUsuario=input("Digite o seu login:\n")
senhaUsuario=input("Digite a sua senha:\n")

loginCadastrado=input("Digite o seu login cadastrado:\n")
senhaCadastrada=input("Digite a sua senha:\n")

if loginCadastrado==loginUsuario and senhaCadastrada==senhaUsuario:
    print("Bem-Vindo!")
else:
    print("Login ou senha inválidos!")

