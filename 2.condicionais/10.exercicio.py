print("=================Construindo a Tabela de Vendas===========================")
print("[1]==Morango||Preço até 5kg||R$ 2,50 por kg.||Acima de 5kg R$ 2,20 por kg.")
print("[2]==Maçã ||Preço até 5kg||R$2,50 por kg.||Acima de 5kg R$ 2,20 por kg.")

qntdkgmorangos=int(input("Digite a quantidade de morangos em kg:"))
qntdkgmacas=int(input("Digite a quantidade de maçãs em kg: "))
precoProduto=float(input("Digite o R$ do produto de acordo com a quantidade de kg:"))

if qntdkgmacas>=8 and precoProduto>25:
    desconto=0.1
