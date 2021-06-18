#01 - Utilizando estruturas condicionais faça um programa que pergunte ao usuário dois números e mostre:
#⦁	A soma deles;
#⦁	A multiplicação entre eles;
#⦁	A divisão  inteira deles;
#⦁	Mostre na tela qual é o maior;
#⦁	Verifique se o resultado da soma é par ou ímpar e mostre na tela;
#⦁	Se a multiplicação entre eles for maior que 40, divida pelo resultado da divisão inteira e mostre o resultado na tela. Se não, mostre que a multiplicação não foi maior que 40.


'''a=int(input('digite um numero : '))
b=int(input('digite outro numero : '))




soma=(a+b)
multplicação=(a*b)
divisão=(a//b)

maior=0
if a > b:
    maior = a
elif b > a:
    maior = b 

nu=0

if(soma%2 == 0):
    nu='par'
else:
    nu='ímpar'

mul=0
if (multplicação > 40):
    mul = f'o resultado da multiplicação dividido com o resultado da divisão é {multplicação/divisão}'
else:
    mul ='a multiplicação não e maior que 40 '




print(f'a soma é {soma}')
print(f'a multplicação é {multplicação}')
print(f'a divisão é {divisão}')
print(f'o maior é {maior}')
print(f'a soma é {nu}')
print(mul)'''


#02 e 03 - Utilizando estruturas de repetição com variável de controle,
#  faça um programa que receba uma string com uma frase informada pelo usuário
#  e conte quantas vezes aparece as vogais a,e,i,o,u e mostre na tela. Depois 
# mostre na tela essa mesma frase sem nenhuma vogal.

#Refatore o exercício2, para que uma função receba a frase,
#  faça todo o tratamento necessário e retorne o resultado.
#  Depois mostre na tela o resultado e a quantidade de letras
#  que foram retiradas da frase original.




'''frase=input('digite uma frase : ').lower
vogais=0

for letras in frase :
    if letras in 'aeiou':
        vogais += 1


  
def frase_1 (frase):
    resp=''
    for letras in frase :
        if letras not in 'aeiou':
            resp+=letras
    return resp
            

print()

print(f'existe {vogais} vogais nessa frase')
print(frase_1 (frase))'''

#03 - Utilizando estruturas de repetição com teste lógico, 
# faça um programa que peça uma senha para iniciar seu processamento. 
# Não deixe o usuário continuar se a senha estiver incorreta, 
# após entrar dê as boas-vindas a seu usuário e apresente a ele o jogo da adivinhação,
# onde o computador vai pensar em um número entre 0 e 10. 
# O jogador vai tentar adivinhar qual número foi escolhido até  acertar, 
# a cada palpite do usuário  diga a ele se o número escolhido pelo computador é maior ou menor ao que ele palpitou. 
# No final mostre quantos palpites foram necessários para vencer

'''from random import randint
print('inicio do programa ')

senha=input('defina sua senha : ')
resposta=input("digite sua senha ? ")

while resposta != senha:
  print('senha invalida\ntente de novo')
  resposta=input("digite sua senha ? ")  
else:
    print('-=-=-=-=-=bem vindo ao jogo de adivinhação-=-=-=-=-=')
    

computador=(randint(0,10))
jogador=int(input('tente adivinhar um numero entre 0 e 10 : '))
palpite=0
opc=True




while opc == True:
    if jogador <0 or jogador >10:
        print('erro numero invalido , tente novamente')
        jogador=int(input('tente adivinhar um numero entre 0 e 10 : '))
        opc=True
    elif jogador > computador:
        print('numero errado , tente novamente com um numero menor')
        palpite +=1
        opc=True
        jogador=int(input('tente adivinhar um numero entre 0 e 10 : '))
    elif jogador < computador:
        print('numero errado , tente novamente com um numero maior')
        palpite +=1
        opc=True
        jogador=int(input('tente adivinhar um numero entre 0 e 10 :'))
    else:
        print(f'parabens você acertou, foram necessários {palpite+1} tentativas')
        opc=False'''


#- Utilizando funções e listas faça um programa que receba uma data no formato 
# DD/MM/AAAA e devolva uma string no formato escrito por extenso. Valide a data e retorne 
# NULL caso a data seja inválida.


#depois de refazer o codigo e muito...muito tempo eu consegui fazer funcionar


'''data = (input('escreva uma data no formato DD/MM/AAAA : '))


def calendario(data):
    global mes
    

    meses = ['','janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho',
           'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
    me = meses[mes]
    
    return me
  
  
def vrifica(data):
    global dia
    global mes
    global ano
    bi=(ano % 4 == 0 and ano % 100 != 100 or ano % 400 == 0)

    if (len(data) < 10 or len(data) > 10):
        print('erro...data invalida')
    elif (data[2]) != '/' or (data[5]) != '/':
        print('erro...digite a data com barra')
    elif (mes < 1 or mes > 12):
        print('erro...mês invalido')
    elif(dia) < 1 or (dia) > 31:
        print('erro...dia invalido')
    elif (ano) < 1800 or (ano) > 2022:
        print('erro...ano invalido')
    
    else:
        print(f'{dia} de {calendario(data)} de {ano}')





dia = int(data[0:2])
mes = int(data[3:5])
ano = int(data[6:10])

vrifica(data)
calendario(data)'''



#6 - Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime.
 #As perguntas são:
#"Telefonou para a vítima?"
#"Esteve no local do crime?"
#"Mora perto da vítima?"
#"Devia para a vítima?"
#"Já trabalhou com a vítima?"
#O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se   a   pessoa   responder   positivamente   a   2   questões   ela   deve   ser   classificada   como "Suspeita",entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".



'''print('responda sim(s) ou não(n) as questoes a baixo : ')
p1 =input('Telefonou para a vítima? ').upper()
p2 =input('Esteve no local do crime? ').upper()
p3 = input('Mora perto da vítima? ').upper()
p4 =input('Devia para a vítima? ').upper()
p5 = input('Já trabalhou com a vítima? ').upper()

sim = 0

 
lista = [p1,p2,p3,p4,p5]


for cont in lista :  
  if cont == 'S':
      sim = sim + 1

if 'S' == 2:
    print("suspeito")   
elif sim == 3 or sim == 4:
    print('cumplice')
elif sim == 5:
  print('assasino')
else:
  print('inocente')'''


#07 - Crie um programa onde o usuário possa digitar sete valores numéricos  
# e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
#  No final, mostre os valores pares e ímpares  em ordem crescente.


'''numero=[]
lista1=[]
lista2=[]

for cont in range(7):
    nu= int(input(f'digite {cont+1}° numero : '))
    numero +=[nu]
print()

for cont in numero:
    if cont %2 == 0:
        lista1 +=[cont]
    else :
        lista2+=[cont]

lista1.sort()
lista2.sort()


lista1.extend(lista2)

print(lista1)'''


#8 - Crie um programa que leia nome, ano de nascimento e carteira de trabalho e 
# cadastre-os (com idade) em um dicionário. Se por acaso a CTPS for diferente de 0, o 
# dicionário receberá também o ano de contratação e o salário. Calcule e acrescente , além da idade ,
#  com quantos anos a pessoa vai se aposentar. Considere que o trabalhador deve contribuir por 35 anos 
# para se aposentar.​​ 


'''from datetime import date

dic={}

nome=input('digite seu nome : ')
nascimento=int(input('digite seu ano de nascimento : '))
carteira=int(input('digite sua carteira de trabalho (quaso não tenha digite 0) :'))

ano=date.today().year
idade = ano-nascimento



dic['nome']=nome
dic['nascimento']=nascimento
dic['idade']=f'{idade} anos'
dic['carteira de trabalho']=carteira



if carteira != 0:
    con=int(input('digite o ano de contratação : '))
    salario=float(input('digite seu salario : '))

    trabalho=ano-con
    aposentadoria=((35-trabalho)+idade)

    dic['ano de contratação']=con
    dic['salario']=f'R${salario}'
    dic['aposentadoria']=f'{aposentadoria} anos'

else:
    print('sem carteira de trabalho')

print()

print('-='*30)
print()

for k,v in dic.items():
    print(f'{k} : {v}')'''
