#Crie um programa, utilizando dicionário, que simule a baixa de estoque das vendas de um supermercado. Não esqueça de fazer as seguintes validações:
#Produto Indisponível
#Produto Inválido
#Quantidade solicitada não disponível 
#O programa deverá mostrar para o cliente a quantidade de itens comprados e o total.





'''estoque={'batata':[1000, 2.50],'tomate':[400, 1.20],'cenoura':[200, 2.00],'chocolate':[100,5.00]}
opc= True
carrinho={}
total= 0
valor=0

while opc == True:
    produto= input('qual produto dejesa comprar ? ')
    if produto not in estoque.keys():
        print('produto invalido')
    else:
        quantidade = int(input('digite a quantidade ? '))
        if quantidade > estoque[produto][0]:
            print(f'quantidade indisponivel, temos {estoque[produto][0]}')
        else:
            pre=estoque[produto][1]
            resul= quantidade*pre
            total += resul
            estoque[produto][0] -= quantidade
            print(f'o valor total do produto foi {total:.2f}')

    res=input('deseja conmtinuar comprando ? (s/n) ').upper()
    if res ==  'S':
        opc = True
    elif res == 'N':
        opc = False'''





#Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feito em cada partida. No final tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

    
'''nome=input('qual o nome do jogador ? ') 
p=int(input('quantas partidasd ele jogou ? '))    
camp={}
total=0



for cont in range(p):
    a=int(input(f'quantos gols ele fez na {cont+1} partida ?'))
    camp[cont+1]=a
    total+=a        
        
print(total)            
print(camp)   '''  








