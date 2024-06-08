import os 
import time 
prato=""
preco=0
somarPreco=0
lista_Prato=0
valorTotalPagar=0

while True:
    print("===MENU DO RESTAURANTE====")
    print("[1]-Picanha-R$25,00")
    print("[2]-Lasanha-R$20,00")
    print("[3]-Strogonoff-R$18.50")
    print("[4]-Ensopado de Carne com Batata-R$15,00")
    print("[5]- Misto Quente com Suco de Laranja-R$8,00")
    print("[6]-Salada com Hambúrguer Batata Frita e Milkshake-R$11.50")
    print("[7]-Torta de Morango-R$7,00")
    opcao=int(input("Digite uma opçao do prato para ser adicionadopu finalize:"))
    if opcao>7 or opcao<0:
        os.system("cls||clear")
    print("Opção Inválida!")
    match(opcao)
        case 1:
            prato="1-Picanha"
            preco=25.00
            somarPreco+=preco
            lista_Prato.append(prato)
        
        case 2:
            prato="2-Lasanha"
            preco=20.00
            somarPreco+=preco
            lista_Prato.append(prato)
            
        
        case 3:
            prato="3-Strogonoff":
            preco=18.50
            somarPreco+=preco
            lista_Prato.append(prato)
            
        case 4:
            prato="4-Ensopado de Carne com Batata"
            preco=15.00
            somarPreco+=preco
            lista_Prato.append(prato)
            
        case 5:
            prato="5-Misto Quente com Suco de Laranja"
            preco=8.00
            somarPreco+=preco
            lista_Prato.append(prato)
            
        case  6:
            prato="6-Salada com  Hambúrguer e Milkshake"
            preco=11.50
            somarPreco+=preco
            lista_Prato.append(prato)
            
        case 7:
            prato="7 Torta de Morango"
            preco=7.00
            somarPreco+=preco
            lista_Prato.append(prato)
            
        case 0:
        if prato==""
            print("Nenhum prato adicionado.")
            break 
        else:
        formaPagamentoEscolhida=int(input("Forma de Pagamento:1-à vista ou 2 cartão de crédito:"))
        if formaPagamentoEscolhida==1:
            formaPagamentoEscolhida=="à vista"
            desconto=somarPreco*0.1
            valorTotalPagar=somarPreco-desconto
            tipoPagamento="Desconto"
        
    
        elif formaPagamentoEscolhida==2:
            formaPagamentoEscolhida=="cartão de crédito"
            desconto=somarPreco*0.1
            valorTotalPagar=somarPreco+desconto
            tipoPagamento="acréscimo"
        
        os.system("cls||clear")
            print("===Exibindo Os Resultados======")
            print(f"Opção Escolhida:"{prato})
            print(f"Forma de Pagamento:"{formaPagamentoEscolhida})
            print(f"Valor do {tipoPagamento}:{desconto:}") 
            print(f"Subtotal:"{somarPreco})
            print(f"Total a Pagar:"{valorTotalPagar:})
            break 
    case _:
        time.sleep(2)
    tenteNovamente=str(input("Deseja adicionar outra opção?(S/N):"))
    tenteNovamente=tenteNovamente.upper()
    if tenteNovamente!="S":
        time.sleep(2)
        continue
        
