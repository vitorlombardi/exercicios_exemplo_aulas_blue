from random import randint
import sys
from time import sleep
import pygame

pygame.init()
pygame.mixer.music.load("rei.mp3")
pygame.mixer.music.play()
pygame.mixer.music.set_volume(0.01)

def nome_jogo(texto):
    tamanho  = 150
    print("═" * tamanho)
    print(f'    {texto}')
    print("═" * tamanho)

def introducao(texto2):
    tamanho  = 150
    print(f'    {texto2}')
    print("═" * tamanho)


nome_jogo('''
           _                          _           _                                                                       _                
          | |   ___    _ __    __ _  (_)  _ __   | |__     ___       ___       __ _   _   _    ___   _ __   _ __    ___  (_)  _ __    ___  
       _  | |  / _ \  | '__|  / _` | | | | '_ \  | '_ \   / _ \     / _ \     / _` | | | | |  / _ \ | '__| | '__|  / _ \ | | | '__|  / _ \ 
      | |_| | | (_) | | |    | (_| | | | | | | | | | | | | (_) |   | (_) |   | (_| | | |_| | |  __/ | |    | |    |  __/ | | | |    | (_) |
       \___/   \___/  |_|     \__, | |_| |_| |_| |_| |_|  \___/     \___/     \__, |  \__,_|  \___| |_|    |_|     \___| |_| |_|     \___/ 
                              |___/                                           |___/                                                               
''')

sleep(1)

introducao(f'''            

                   Jorginho é um rapaz comum que tinha um sonho de ser dev senior, estava tudo organizado em sua vida
            até começar a pandemia em 2020, quando foi demitido por corte de verbas dentro da empresa onde trabalhava como programador,
            o mesmo dia quando retornava para sua casa jorginho sofreu um acidente com sua pop 100, que resultou em um prejuizo de R$ 10,000.00
                Jorginho se viu desesperado sem dinheiro e resolveu pedir dinheiro a um agiota, que tinha como desfarce ser professor
            da blue ed tech seu nome era Gustavo, que lhe emprestou dando um prazo de três meses para o pagamento, 
            falta exatamente uma semana para o pagamento e jorginho só tem R$ 4,00 na carteira e um sonho, 
            você quer ajudar jorginho a sair desse buraco ? 
                                                  
                                                    Digite (S) ou (N) ''')      


entrada = "s"
entrada2 ="n"
entrada_classe = "" 
while entrada_classe != entrada:
    entrada_classe = input("Digite aqui :").lower()
    if entrada_classe == entrada:
        pass
    elif entrada_classe == entrada2:
        sys.exit()
    else :
        print('É para digitar (S) ou (N),tenta denovo vai !!!')    



class Relogio:
    def __init__(self):
        self.horas = 5
        self.minutos = 30

    def __str__(self):
        return f"{self.horas:02d}:{self.minutos:02d}"

    def avancaTempo(self, minutos):
        self.minutos += minutos
        while(self.minutos >= 60):
            self.minutos -= 60
            self.horas += 1

    def atrasado(self):
        return (self.horas > 7 or (self.horas == 7 and self.minutos > 0))


class agiota:
    def __init__(self):
        self.divida = 10.000
        self.juros = 10

class npcs:
    def __init__(self,nome,vida,ataque):
        self.nome=nome
        self.vida=vida
        self.ataque=ataque


npc1_0 = npcs('suspeito', 20, 5)
npc1 = npcs('velha', 20, 5)
npc2 = npcs('badido', 50, 20)
npc3 = npcs('gustavo', 150, 50)


class Casa:
    def __init__(self):
        self.jogar = False
        self.comida = 1

class Personagem():
    def __init__(self,sujo,fome,vida,poder,nivel,sanidade,jogar,dinheiro,salario,divida):
        self.sujo = sujo
        self.fome = fome
        self.vida = vida
        self.poder = poder
        self.nivel = nivel
        self.sanidade = sanidade
        self.jogar = jogar
        self.dinheiro = dinheiro
        self.salario = salario
        self.divida = 0

#encapsulamento

    def get_divida(self):
        return self.__divida

    def set_divida(self, divida):
        self.__divida = divida


    @property
    def divida(self):
        return self.__divida

    @divida.setter
    def divida(self, divida):
        self.__divida = divida

#polimorfismo

    def forcabruta(self):
        fb = 10 + self.poder
        return fb

    def louco(self):
        loc = 5 - self.sanidade
        return loc
    
    
    def energia(self):
        ener = 40 - self.vida
        return ener


    def __str__(self):
        return "jorginho está " + ("fedendo" if self.sujo else "cheirosinho")+", "+("cheio de" if self.fome else "sem")+" fome e "+'sua sanidade é '+str(self.sanidade)+" Você tem R$"+str(self.dinheiro)+" reais na sua conta,"+'seu nivel é '+str(self.nivel)+' sua divida é '+str(self.divida)

    def dormir(self):
        self.sujo = True
        self.fome = True
        self.sanidade -= 1
        self.vida=100


class JorginhoAstuto(Personagem):
    def __init__(self,sujo,fome,vida,poder,nivel,sanidade,jogar,dinheiro,salario,divida):
        Personagem.__init__(self,sujo,fome,vida,poder,nivel,sanidade,jogar,dinheiro,salario,divida)
    
    def forcabruta(self):
        fb = 10 + self.poder
        return fb

class JorginhoMalandro(Personagem):
    def __init__(self,sujo,fome,vida,poder,nivel,sanidade,jogar,dinheiro,salario,divida):
        Personagem.__init__(self,sujo,fome,vida,poder,nivel,sanidade,jogar,dinheiro,salario,divida)
    
    def louco(self):
        loc = 5 - self.sanidade
        return loc
    

class JorginhoCorinthiano(Personagem):
    def __init__(self,sujo,fome,vida,poder,nivel,sanidade,jogar,dinheiro,salario,divida):
        Personagem.__init__(self,sujo,fome,vida,poder,nivel,sanidade,jogar,dinheiro,salario,divida)
    
    def energia(self):
        ener = 40 - self.vida
        return ener

jorginhoastuto = JorginhoAstuto(True , True , 100 ,10 ,1 ,10 ,False,4 ,100,'divida')
jorginhomalandro = JorginhoMalandro(True , True , 100 ,10 ,1 ,10 ,False,4 ,100,'divida')
jorginhoicorinthiano = JorginhoCorinthiano(True , True ,100 ,10 ,1 ,10 ,False,4 ,100,'divida')           

print('''
        Jorginho    astuto    digite           (1)
        Jorginho    malandro    digite         (2)
        Jorginho    corinthiano    digite      (3)  ''' )
cla=0
c = input('''        Ola digite a classe que quer jogar com jorginho :''')
if c == '1':
    cla = jorginhoastuto
elif c == '2':
    cla = jorginhomalandro
elif c == "3":
     cla = jorginhoicorinthiano 

if(__name__ == "__main__"):
    dia = 1
    relogio = Relogio()
    personagem = cla
    personagem.set_divida(10000)
    personagem.louco()
    personagem.energia()
    personagem.forcabruta()    
    casa = Casa()
    agi=agiota()
    cafe_da_manha = False
    passagem = False
    jogar = False
    while True:
        sleep(1)
        print("São "+str(relogio)+" do dia "+str(dia) +
              ". Você tem que sair pro trabalho até às 07:00.")
        print(personagem)
        print("")
        sleep(1.5)
        print("Ações:")
        print("1 - tomar banho")
        print("2 - Fazer o rango")
        print("3 - Pedir um ifood")
        print("4 - Tomar café da manhã")
        print("5 - jogar ps5")
        print('6 - ir para o mercado')
        print("7 - Ir trabalhar")
        print("0 - Sair do jogo")
        opcao = input("Escolha sua ação:")
        sleep(1)
        print('~~~'*40)

        if relogio.horas >= 8 and relogio.minutos>=00:
            sleep(1)
            print('jorginho viu que ja era tarde de mais para ir trabalhar e descide ficar em casa jogando')
            print('como jorginho nao foi trabalhar ele não vai receber nada e o juros esta aumentando')
            sleep(0.5)
            print('~~~'*40)
            
            personagem.dormir()
            relogio = Relogio()
            dia += 1


        elif(opcao == "1"):
            personagem.sujo = False
            relogio.avancaTempo(15)
        elif(opcao == "2"):
            if(casa.comida > 0):
                casa.comida -= 1
                cafe_da_manha = True
            else:
                sleep(1)
                print("Não há comida em casa.")
            relogio.avancaTempo(15)
        elif(opcao == "3"):
            if(personagem.dinheiro >= 15):
                personagem.dinheiro -= 15
                cafe_da_manha = True
            else:
                sleep(1)
                print(
                    "O café da manhã custa 15 reais, você não tem dinheiro suficiente.")
            relogio.avancaTempo(5)
        elif(opcao == "4"):
            if(cafe_da_manha):
                personagem.fome = False
                cafe_da_manha = False
                relogio.avancaTempo(15)
            else:
                sleep(1)
                print("Não tem café da manhã na sua casa.")
                relogio.avancaTempo(5)
        elif(opcao == "5"):
            personagem.sanidade += 2
            relogio.avancaTempo(60)

        elif(opcao == '6'):
            sleep(1)
            print('jorginho vai ate o mercado na esquina da casa dele')
            it=input('opções: \n1=comprar comida(R$500)\n2=itens diferenciados(1500)')
            if (it == '1'):
                if personagem.dinheiro > 500:
                    personagem.dinheiro-=500
                    casa.comida+=15
                    relogio.avancaTempo(30)
                    print('jorginho faz a compra que teoricamente dura 15 dias')
                    sleep(0.5)
                    print('~~~'*40)
                elif personagem.dinheiro < 500:
                    sleep(1)
                    print('quando jorginho foi pagar a conta ele viu que não timha dinhero, entao\n ele largou as as coisas lá e saiu mais rapido que sua dignidade diminuindo ao londo dos dias ')
                    sleep(0.5)
                    print('~~~'*40)
                    personagem.sanidade-=2
                    relogio.avancaTempo(20)
            elif(it == '2'):
                if personagem.dinheiro > 1500:
                    personagem.dinheiro-=1500
                    personagem.vida+=50
                    personagem.poder+=20
                    sleep(1)
                    print('jorginho achou uma frasco com um liquido suspeito azul')
                    print('jorginho pebe o liquido e logo sente algo dentro dele diferente')
                    sleep(0.5)
                    print('~~~'*40)
                    relogio.avancaTempo(30)
                   
                elif personagem.dinheiro < 1500:
                    sleep(1)
                    print('jorginho achou uma frasco com um liquido suspeito azul, ele ate pensou\nem comprar mas sem dinhero ')
                    sleep(0.5)
                    print('~~~'*40)
                    personagem.sanidade-=1
                    relogio.avancaTempo(20)
            else:
                sleep(1)
                print("para você aprender a não ser besta e ficar digitando opções invalidas vai perde tempo)")
                sleep(0.5)
                print('~~~'*40)
                relogio.avancaTempo(10)
        elif(opcao == "7"):
            if dia == 7:
                sleep(1)
                print('emquanto jorginho saia de casa ele encontra Gustavo o agiota que ele pegou dinhero emprestado')
                print('Gustavo foi a encontro de jorginho para cobrar sua divida e ele nao parecia nada feliz')
                print('"jorginho... jorginho sabe que dia é hoje"')
                a=input('1=domingo... ?\n2=seu aniversario ?\nfala ? ')
                sleep(0.5)
                print('~~~'*40)
                opi=True
                while opi == True:
                    if (a == '1'):
                        sleep(1)
                        print('"sim idiota hoje e domingo dia do meu pagamento, agora passa logo o dinhero')
                        sleep(0.5)
                        print('~~~'*40)
                        sleep(1)
                        opi=False
                    elif (a == '2'):
                        sleep(1)
                        print('"como você sabia... agora para de ser engraçadinho e da o meu presente')
                        sleep(0.5)
                        print('~~~'*40)
                        opi=False    
                    else:
                        sleep(1)
                        print('estou começando a ter certeza que você e um idiota , escolha logo 1 ou 2')
                        opi=True
                        a=input('acão ? ')
                        sleep(0.5)
                        print('~~~'*40)
                        sleep(1)
                print('o que o jorginho pode fazer.\n1=lutar contra o agiota para guanhar mais tempo.\n2=ser um bundao e implorara para o agiota mais tempo')
                acao = (input('acão ? '))
                sleep(0.5)
                print('~~~'*40)
                op = True
                while op == True:
                    if (acao == '1'):
                        opc = 0
                        op = False
                        while opc == 0:
                            sleep(1)
                            print('jorginho esta confiate que pode descer o agiota na porrada e parte para cima dele acertando um ataque')
                            npc3.vida = npc3.vida-personagem.poder
                            
                            print('o agiota fica ainda mais furioso')
                            personagem.vida = personagem.vida-npc3.ataque
                            print()
                            print('o agiota ataca o jorginho com um taco de baseball coberto de arame farpado')
                            opc = 0
                            sleep(0.5)
                            print('~~~'*40)
                            sleep(1)
                            acao = (input('escolha : \n\n1=atacar \n2=se ajoelhar e se desculpar\n\nacão ? '))
                            if acao == '1':
                                sleep(1)
                                print()
                                print('jorginho acerta um ataque no safado')
                                npc2.vida = npc2.vida-personagem.poder
                                print()
                                sleep(1)
                                print('jorginho leva uma tacada gostosa')
                                personagem.vida = personagem.vida-npc2.ataque
                                opc = 0
                                sleep(0.5)
                                print('~~~'*40)
                                sleep(1)
                                acao = (input(
                                    'escolha : \n\natacar\n2=se ajoelhar e se desculpar\n\nacão ? '))
                                if npc2.vida <= 0:
                                    sleep(1)
                                    print('depos de jorginho e gustavo trocarem muitos golpes jorginho consegue finalmente acertar o ultimo ataque')
                                    print('com a maior felicidade do mundo jorginho saqueia o agiota')
                                    print('conseguindo :\n1-uma peruca\n2-um taco de baseball\n3-um charuto\n3-R$1.000\n4-uma carteira vip do club do corinthians')
                                    sleep(0.5)
                                    print('~~~'*40)
                                    print('\n')
                                    opc = 1
                                    sys.exit()
                                elif personagem.vida <= 0:
                                    sleep(1)
                                    print('jorginho cai nop chao, no frio, na chuva, com dor e individado ')
                                    print('depois do gustavo bricar de saco de pancadas com o jorginho ele pega sua carteira e fala :')
                                    print('voce lutou bem... eu quase suei para te dar uma surra\nvou pegar seu dinhero e te da um praso de mais um mes para voce me pagar, com um pequeno grande juros claro')
                                    sleep(0.5)
                                    print('~~~'*40)
                                    sleep(1)
                                    print()
                                    print('meus Parabéns você finalizou a beta do nosso jogo, espero que tenha\n gostado de controlar o jorginho e para constar esse e o final mediano')
                                    print('voce terminou o jogo com o seguinte atributos :\n', personagem )
                                    sleep(0.5)
                                    print('~~~'*40)
                                    sleep(1)
                                    print('"Parabéns, você não fez mais que sua obrigação, mas fique feliz\n esse e o melhor final que da para conseguir,eu ate poderia falar o que\n acontece com jorginho mas eu seu preguiçoso demais para isso, entao use a\n imaginação" ass-desenvolvedor 1')
                                    agi.divida += 7.000
                                    personagem.sanidade -= 10
                                    personagem.dinheiro = personagem.dinheiro-personagem.dinheiro
                                    opc = 1
                                    print(
                                        'meus Parabéns você finalizou a beta do nosso jogo, espero que tenha\n gostado de controlar o jorginho e para constar esse e o final ruim ')
                                    print('voce terminou o jogo com o seguinte atributos :\n', personagem )
                                    sleep(0.5)
                                    print('~~~'*40)
                                    sleep(1)
                                    print('"eu até poderia poderia te falar o que aconteceu com jorginho\n depois disso mas não vou, posso te garantir que o final poderia ser pior\n, então use a imaginação" ass-desenvolvedor 1')
                                    sys.exit()
                            elif acao == '2':
                                sleep(1)
                                print('"como você foi bonzinho eu vou te perdoar pelo ataque com um pequenos juros de 50 %"')
                                print('"e como você não me pagou hoje vai ter mais um juros tambem"')
                                print('mas pelo lado bom você vai ter mais tempo...talvez um mês')
                                sleep(0.5)
                                print('~~~'*40)
                                sleep(1)
                                personagem.sanidade -= 10
                                personagem.dinheiro = personagem.dinheiro-personagem.dinheiro
                                agi.divida+=10000
                                opc = 1
                                print(
                                    'meus Parabéns você finalizou a beta do nosso jogo, espero que tenha\n gostado de controlar o jorginho e para constar esse e o final muito ruim ')
                                print('voce terminou o jogo com o seguinte atributos :\n', personagem )
                                sleep(0.5)
                                print('~~~'*40)
                                sleep(1)
                                print('"parando para pensar não sei se te parabeniso por finalizar o jogo ou\n por ter conseguido o pior final,posso te garantir que o jorginho esta muito\n ferrado agora, mas não vou falr o que acontece com ele depois disso então use\n a imaginação" ass-desenvolvedor 1 ')
                                sys.exit()
                            else:
                                sleep(1)
                                opc = 0
                                print('eu sei que você e meio lerdo mas escolha 1 ou 2')
                                sleep(0.5)
                                print('~~~'*40)
                    elif acao == '2':
                        sleep(1)
                        personagem.dinheiro = personagem.dinheiro-personagem.dinheiro
                        print('"jorginho...jorginho como eu fui seu professor eu vou te dar mais tempo,com um\n pequeno juros de 50% o que acha" fala gustavo acendendo umn charuto')
                        print('"voce sabe que fazer um mestrado custa caro ne, entao o juros e valido"')
                        print('"como um adiantamento me passa tudo que voce tem ai"')
                        sleep(0.5)
                        print('~~~'*40)
                        sleep(1)
                        print('meus Parabéns você finalizou a beta do nosso jogo, espero que tenha gostado\n de controlar o jorginho e para constar esse e o final um pouco menos ruim')

                        print('voce terminou o jogo com o seguinte atributos :\n', personagem )
                        sleep(0.5)
                        print('~~~'*40)
                        sleep(1)
                        print('"dava para conseguir um final pior então fique feliz, não vou falar o que\n acontece com jorginho porque estou com preguiça de digitar então imagine"ass-desenvolvedor 1')
                        personagem.sanidade-=10 
                        agi.divida+=5.000
                        personagem.dinheiro = personagem.dinheiro-personagem.dinheiro
                        op = False
                        sys.exit()
                    else:
                        sleep(1)
                        print('eu sei que você e meio lerdo mas escolha 1 ou 2')
                        sleep(0.5)
                        print('~~~'*40)
                        op = True
                        acao = (input('acão ? '))


            opc = 0
            while opc == 0:
                sleep(1)
                print("1- ir trabalhar de onibus (custa R$5.00).")
                print("2- ir trabalhar na sola")
                op = input('escolha uma maneira de ir para o trabalho : ')
                sleep(0.5)
                print('~~~'*40)
                if(op == '1'):
                    sleep(1)
                    if (personagem.dinheiro >= 5):
                        personagem.dinheiro -= 5
                        print('perdeu 5 pila')
                        sleep(0.5)
                        print('~~~'*40)
                        relogio.avancaTempo(25)
                        opc = 1
                        if dia == 2:
                            sleep(1)
                            print(
                                'so tem um lugar vago no onibus...jorginho e uma velha se encaram por 1 minuto. ')
                            print('a velha sai correndo como se não tivesse amanha em direçao ao lugar vago')
                            print('o que fazer.\n1=atacar.\n2=ser um bundao e ir a viagem toda de pe')
                            print()
                            acao = (input('acão ? '))
                            sleep(0.5)
                            print('~~~'*40)
                            sleep(1)
                            op = True
                            while op == True:
                                if(acao == '1'):
                                    op = False
                                    opc = 0
                                    while opc == 0:
                                        npc1.vida = npc1.vida-personagem.poder
                                        print(
                                            'jorginho foi correndo e deu uma voadora de dois pés na velhinha \na velhinha cai no chao  ')
                                        opc = 0
                                        acao = (input('escolha entre \n1=terminar o serviço \n2=ser bondoso e ir sentar\nação ? '))
                                        sleep(0.5)
                                        print('~~~'*40)
                                        if acao == '1':
                                            sleep(1)
                                            npc1.vida = npc1.vida-personagem.poder
                                            print(
                                                'jorginho ja jogou muito RPG para saber que é hora de saquear\nele consegur : \nR$ 5,00\n1 passe livre para idosos\n3=uma foto do seu neto que esta assinada:ass-matheus')
                                            print('jorginho pisa na velhinha e vai sentar')
                                            print('\n\nemquanto jorginho esta sentado ele sente sua sanidade diminuindo , porem algo dentro dele mudou.')
                                            sleep(0.5)
                                            print('~~~'*40)
                                            opc = 1
                                            personagem.sanidade-=1 
                                            personagem.nivel+=1
                                            personagem.poder+=10
                                            personagem.vida+=50
                                        elif acao == '2':
                                            sleep(1)
                                            print('jorginho arruma o pentiado e vai se sentar') 
                                            print('emquanto jorginho esta sentado ele sente que algo dentro dele mudou')   
                                            sleep(0.5)
                                            print('~~~'*40)
                                            personagem.nivel+=1   
                                            personagem.vida+=50                                 
                                            opc = 1
                                        else:
                                            sleep(1)
                                            opc = 0
                                            print('você e burro ou se faz, escolha 1 ou 2')
                                elif(acao == '2'):
                                    sleep(1)
                                    print('jorginho vai a viagem a pé e triste, porem sente que fez algo bom')
                                    sleep(0.5)
                                    print('~~~'*40)
                                    op = False
                                    personagem.sanidade+=1
                                else:
                                    sleep(1)
                                    op = True
                                    print('voce e burro ou se faz, escolha 1 ou 2')
                                    acao = (input('acão ? '))
                                    sleep(0.5)
                                    print('~~~'*40)
                        
                        if dia == 3:
                            sleep(1)
                            print("jorginho estava andando para chegar no trabalho\ne encontra um pedaço de papel no chão  ")
                            print('ao olhar para o papel ele percebe que e um mapa')
                            mapa=input('o que jorginho vai fazer :\n1=seguir o mapa\n2=ignorar o mapa e ir trabalhar\nação ?')
                            sleep(0.5)
                            print('~~~'*40)
                            pa=True
                            colar=False
                            while pa == True:
                                if mapa == '1':
                                    pa=False
                                    sleep(1)
                                    print('jorginhoa segue o mapa e chega em uma arvore gigante')
                                    print('a terra perto da arvore parece ter cido revirada ')
                                    print('jorginho como não e besta de seguir um mapa atoa ele cava perto da arvore')
                                    print('depois de cava jorginho acha um colar feito de safira ')
                                    print('jorginho vai feliz para o trabalho')
                                    personagem.vida+=50
                                    relogio.avancaTempo(50)
                                    sleep(0.5)
                                    print('~~~'*40)
                                    colar=True
                        if dia == 4:
                            print('quando jorginho sai do onibus ele encontra uma pessoa de capuz')
                            print('a pessoa de capuz fala para jorginho ')
                            print('"se você quiser continuar andando passa a carteira"')
                            print('logo depois de terminar de falar ele saca uma faca')
                            sleep(1)
                            print('~~~'*40)
                            sleep(0.5)
                            print('o que fazer.\n1=ser corajoso uma vez na vida e atacar.\n2=ser um bundao e passar a grana para o assaltante')
                            
                            acao = (input('acão ? '))
                            sleep(0.5)
                            print('~~~'*40)
                            op = True
                            while op == True:
                                if (acao == '1'):
                                    opc = 0
                                    op = False
                                    while opc == 0:
                                        sleep(1)
                                        print('jorginho lembra dos anime que asistiu pela madrugada e pensa que\né um protagonista e parte para cima do assaltante')
                                        npc2.vida = npc2.vida-personagem.poder
                                        print()
                                        print('assaltante olha com cara de curiosidade para jorginho e contra ataca ele com um chute na barriga')
                                        personagem.vida = personagem.vida-npc2.ataque
                                        print()
                                        print('jorginho perde o ar mas continua em pé')
                                        sleep(1)
                                        opc = 0
                                        aci = (input(
                                            'escolha : \n\n1=ser idiota e atacar novamente\n2=ser um bundao e passar a carteira\n\nacão ? '))
                                        sleep(0.5)
                                        print('~~~'*40)
                                        if aci == '1':
                                            sleep(1)
                                            print(
                                                'jorginho lembra que um protagonista nunca desiste vai atacar o assaltante de novo')
                                            npc2.vida = npc2.vida-personagem.poder
                                            print()
                                            print('jorginho leva um ataque')
                                            sleep(1)
                                            personagem.vida = personagem.vida-npc2.ataque
                                            opc = 0
                                            acio = input('escolha : \n\n1=ser idiota e atacar\n2=ser um bundao\n\nacão ?')
                                            sleep(0.5)
                                            print('~~~'*40)
                                            if npc2.vida <= 0:
                                                sleep(1)
                                                print(
                                                    'jorginho quase perdendo a consciência mas consegue dar o ataque final em seu inimigo')
                                                sleep(1)
                                                personagem.sanidade += 2
                                                print(
                                                    'jorginho como um bom jogador de RPG saqueia o corpo do assaltante\nitens adiquiridos :\n1-faca\n2-R$300\n3-um maço de derbi')
                                                sleep(0.5)
                                                print('~~~'*40)
                                                personagem.nivel += 1
                                                personagem.poder += 20
                                                personagem.vida += 100
                                                opc = 1
                                            elif personagem.vida <= 0:
                                                sleep(1)
                                                print('depos de apanhar muito jorginho desmaia')
                                                sleep(0.5)
                                                print('~~~'*40)
                                                sleep(1)
                                                personagem.sanidade -= 4
                                                personagem.dinheiro = personagem.dinheiro-personagem.dinheiro
                                                opc = 1
                                                relogio.avancaTempo(30)
                                                print(
                                                    'depois de um tempo jorginho acorda ,com seu copo dolorido e sem sua carteira mesmo com dificuldade ele vai para o trampo')
                                                relogio.avancaTempo(50)
                                                sleep(0.5)
                                                print('~~~'*40)
                                                
                                        elif aci == '2':
                                            sleep(1)
                                            print('jorginho viu que não tinha como vencer e entraga a carteira para o assaltante')
                                            print('"você fez uma boa escolha"')
                                            print('o assaltante pega a carteira e sai andando em diresão a um beco')
                                            print('mesmo depois de jorginho ser assaltado ele descide ir trabalhar ')
                                            relogio.avancaTempo(10)
                                            sleep(0.5)
                                            print('~~~'*40)
                                            personagem.dinheiro = personagem.dinheiro-personagem.dinheiro
                                            personagem.sanidade -= 4
                                            opc = 1
                                            relogio.avancaTempo(20)
                                        else:
                                            sleep(1)
                                            opc = 0
                                            print('voce e burro ou se faz, escolha 1 ou 2')
                                            aci=input('ação ? ')
                                            sleep(0.5)
                                            print('~~~'*40)
                                elif acao == '2':
                                    sleep(1)
                                    personagem.dinheiro = personagem.dinheiro-personagem.dinheiro
                                    print('jorginho passa a carteira para o assaltante e perde todo seu dinhero e sua dignidade')
                                    print()
                                    print('como jorginho foi assatado ele sente mais vontade de ir trabalhar , porque sua divida estava bem alta')
                                    sleep(0.5)
                                    print('~~~'*40)
                                    relogio.avancaTempo(15)
                                    op = False
                                else:
                                    sleep(1)
                                    print('voce e burro ou se faz, escolha 1 ou 2')
                                    op = True
                                    acao = (input('acão ? '))
                                    sleep(0.5)
                                    print('~~~'*40)

                        if dia  == 5:
                            if colar == True:
                                sleep(1)
                                print('jorginho estava quase chegando no trabalho quando uma mulher para ele')
                                print('"esse colar eu reconheço, ele é meu, minha filha pegou ele para brincar"')
                                print('"ela falou que timha deixado pistas para eu achar, mas ja faz dois dias que eu to procurando"')
                                print('"acho que você achou primeiro, será que pode me devolver ?"')
                                escolha=input('escolhas :\n1=ser bom e devolver\n2=correr muito\nação ?')
                                sleep(0.5)
                                print('~~~'*40)

                                esc=True
                                while esc == True:
                                    if escolha == '1':
                                        esc=False
                                        print('jorginho logo pensando na reconpença entrga o colar para a mulher')
                                        personagem.vida-=50
                                        personagem.dinhero+=700
                                        relogio.avancaTempo(10)

                                        print('"obrigado por devolver, esse colar e muito inportante para mim"')
                                        print('"fiuque com isso como agradecimento"ela fala entregando R$1000 reais para jorginho')
                                        print('depois disso jorginho vai todpo feliz para o trabalho')
                                        sleep(0.5)
                                        print('~~~'*40)
                                    elif escolha == '2':
                                        esc=False
                                        print('jorginho corre o mais rapido que pode')
                                        print('depois de 10 minutos correndo ele consegue dispistar ela e chegar no trabalho')
                                        sleep(0.5)
                                        print('~~~'*40)
                                        relogio.avancaTempo(10)
                                    else:
                                        print('para de frescura e digite 1 ou 2 logo')
                                        esc=False
                                        escolha=input('ação ?')
                                        sleep(0.5)
                                        print('~~~'*40)
                        if dia == 6:
                            sleep(0.5)
                            print('~~~'*40)
                            sleep(1)
                            print('na entrada do serviço de jorginho tinha uma barraca que ele nunca tinha visto antes')
                            print('"barraca da sorte \nentre e se divirta"')
                            sleep(0.5)
                            print('~~~'*40)
                            sleep(1)
                            aca = input('oque fazer :\n1=entrar e testar a sorte\n2=ir trabalhar logo')
                            sleep(0.5)
                            print('~~~'*40)

                            pp=True
                            while pp == True:
                                if aca == '1':
                                    pp = False
                                    sleep(1)
                                    print('jorginho entra na barraca que incrivelmente parece muito maior por dentro')
                                    print('"chege mais perto meu caro otar...digo pessoa de sorte " dis um velho que esta atrás de uma mesa')
                                    print('"vejo que veio testar sua sorte, e bem simples eu vou jogar um dado e você tenta adivinhar se ele e par ou inpar"')
                                    print('"se você acertar guanha um item se errar não guanha nada o que acha ?"')
                                    print('"mas é claro que isso por uma pequena taxa de R$500 reais "')
                                    sleep(0.5)
                                    print('~~~'*40)
                                    sleep(1)
                                    aa=input('oque fazer :\n1=ser um otar...bom cliente\n2=sair e ir trabalhar\nação ? ')
                                    sleep(0.5)
                                    print('~~~'*40)
                                    pci=0
                                    while pci == 0:
                                        nu=''
                                        dado=randint(1,6)
                                        if(dado % 2 == 0):#par
                                            nu = '1'
                                        else:
                                            nu = '2'#impar
                                            if aa == '1':
                                                personagem.dinheiro -= 500
                                                pci=1
                                                sleep(1)
                                                jogador = input('1=par\n2=impar\nescolha : ')
                                                sleep(0.5)
                                                print('~~~'*40)
                                                if jogador == nu :
                                                    sleep(0.5)
                                                    print('~~~'*40)
                                                    sleep(1)
                                                    print('você acertou')
                                                    print('"não era para nimguem acertar, nunca confie nos desenvolvedores...digo que coisa otima, agora voce pode escolher um premio eu acho ')
                                                    print('o velho tira uma caixa de baixo da mesa ')
                                                    print('"eu tenho otimos premios aqui você vai ADORAR"')
                                                    sleep(0.5)
                                                    print('~~~'*40)
                                                    sleep(1)
                                                    itens=input('dento da caixa tem dois itens :\n1-liquido suspeito vermelho\n2-liquido suspeito verde')
                                                    sleep(0.5)
                                                    print('~~~'*40)
                                                    con=0
                                                    relogio.avancaTempo(15)
                                                    while con == 0:
                                                        if (itens == '1'):
                                                            sleep(1)
                                                            print('jorginho pega o frasco vermelho e da uma golada')
                                                            print('jorginho sente a energia de 1.000 marombeiros dentro dele...')    
                                                            print('depos disso jorginho vai para o trabalho')
                                                            sleep(0.5)
                                                            print('~~~'*40)
                                                            personagem.poder+=20   
                                                            con=1    
                                                            relogio.avancaTempo(15)
                                                        elif (itens == '2'):
                                                            sleep(0.5)
                                                            print('~~~'*40)
                                                            sleep(1)
                                                            print('jorginho pega o frasco verde e da uma golada')
                                                            print('jorginho sente a energia de um monge belga dentro dele')
                                                            print('depos disso jorginho vai para o trabalho')
                                                            sleep(0.5)
                                                            print('~~~'*40)
                                                            personagem.vida+=50
                                                            con=1
                                                elif jogador != nu:
                                                    sleep(1)
                                                    print('errou...errou feio...errou rudi')
                                                    print( 'jorginho sai triste da cabana cabana e vai para a emoresa' )
                                                    sleep(0.5)
                                                    print('~~~'*40)
                                                    pci=1
                                                else:
                                                    sleep(1)
                                                    pci = 0
                                                    print('eu sei que voce é idiota mas escolhe logo 1 ou 2')
                                                    jogador = input('ação ?')
                                                    sleep(0.5)
                                                    print('~~~'*40)
                                            elif aa == '2':
                                                sleep(1)
                                                pci = 1
                                                print('jorginho logo percebe que isso e uma cilada e vasa da li e continua seu rumo para o trampo')
                                                relogio.avancaTempo(10)
                                                personagem.sanidade+=1   
                                            else:
                                                sleep(1)
                                                pci = 0
                                                print('eu sei que voce é idiota mas escolhe logo 1 ou 2')
                                                aa = input('ação ? ')
                                                sleep(0.5)
                                                print('~~~'*40)
                                elif aca == '2':
                                    sleep(1)
                                    print('jorginho ignora a barraca e entra na empresa')
                                    pp=False
                                else:   
                                    sleep(1)        
                                    print('eu sei que voce é idiota mas escolhe logo 1 ou 2')
                                    aca=input('ação ?')
                                    sleep(0.5)
                                    print('~~~'*40)
                                    pp=True

                    else:
                        sleep(1)
                        print('jorginho esta liso, não tem dinheiro para a passagem e vai correndo')
                        print('')
                        opc = 1
                elif (op == '2'):
                    sleep(1)
                    relogio.avancaTempo(60)
                    print('como jorginho esva economizando ele decide ir a pé para o trampo')
                    opc = 1
                    personagem.sanidade -= 1
                    if dia == 2:
                        sleep(0.5)
                        print('~~~'*40)
                        sleep(1)
                        print('jorginho estava correndo e encontrou uma pessoa suspeita com um sobre tudo. ')
                        print('a pesssoa suspeita se aproxima de jorginho e fala enquanto coloca a mão dentro do sobre tudo:')
                        print('"ola queridinho você quer um docinho"')
                        sleep(1)
                        ac = input('1=que tipo de doce ?\n2=hummm...minha mãe me ensinou a não pegar doces de estranos\n fala ? ')
                        sleep(0.5)
                        print('~~~'*40)
                        cpo = True
                        while cpo == True:
                            if (ac == '1'):
                                cpo = False
                                sleep(1)
                                print('"você vai adorar eu garanto" a pessoa suspeita fala enquanto abre o sobre tudo e sai correndo para cima do jorginho com um biquine de baixo do sobre tudo')
                                sleep(0.5)
                                print('~~~'*40)
                            elif (ac == '2'):
                                cpo = False
                                sleep(1)
                                print('"não seja timido voce vai adorar" a pessoa suspeita fala enquanto abre o sobre tudo e sai correndo para cima do jorginho com um biquine de baixo do sobre tudo')
                                sleep(0.5)
                                print('~~~'*40)
                            else:
                                print('serio quer que eu desenhe, escolhe logo 1 ou 2')
                                cpo = True
                                ac = input('ação ? ')
                                sleep(0.5)
                                print('~~~'*40)
                        sleep(1)
                        print('o que fazer.\n1=atacar com toda sua força.\n2=esperar a pessoa suspeita chegar perto para ganhar um doce\n')
                        print()
                        acao = (input('acão ? '))
                        sleep(0.5)
                        print('~~~'*40)
                        op = True
                        while op == True:
                            if (acao == '1'):
                                opc = 0
                                op = False
                                while opc == 0:
                                    npc1.vida = npc1.vida-personagem.poder
                                    sleep(1)
                                    print('jorginho deu um chute nas partes baixar do homem suspeito \na pessoa suspeita cai de joelhos no chao ')
                                    sleep(0.5)
                                    print('~~~'*40)
                                    opc = 0
                                    sleep(1)
                                    acao = (input('escolha : \n\n1=terminar o serviço\n2=ser bondoso e terminar o serviço\n\nacão ? '))
                                    sleep(0.5)
                                    print('~~~'*40)
                                    if acao == '1':
                                        npc1.vida = npc1.vida-personagem.poder
                                        opc = 1
                                        if npc1.vida <= 0:
                                            sleep(1)
                                            print(
                                                'jorginho chuta o o queixo de seu inimigo que logo depois desmaia')
                                            sleep(0.5)    
                                            print('~~~'*40)
                                            opc = 1
                                            personagem.sanidade -= 2
                                            personagem.nivel += 1
                                            personagem.poder += 10
                                            sleep(1)
                                            print('jorginho mesmo ganhando a luta sente que perdeu algo...talvez sua sanidade.\nmas pelo lado bom jorginho subiu de nivel seja la o que isso significa')
                                            sleep(0.5)
                                            print('~~~'*40)
                                            sleep(1)
                                            print(
                                                'como um bom jogador de RPG mesmo não querendo jorginho saqueia seu inimigo')
                                            print('ele pega : \n1-um biquine\n2-um objeto longo de borracha com um cheiro ruim(talvez de para usar como arma)')
                                            sleep(0.5)
                                            print('~~~'*40)
                                            personagem.poder += 5
                                        elif npc1.vida != 0:
                                            opc = 0
                                            sleep(1)
                                            acao = ('escolha : \n\n1=terminar o serviço\n2=ser bondoso e terminar o serviço\n\nacão ? ')
                                            sleep(0.5)
                                            print('~~~'*40)
                                    elif acao == '2':
                                        sleep(1)
                                        print('jorginho chuta o o queixo de seu inimigo que logo depois desmaia')
                                        opc = 1
                                        personagem.sanidade -= 2
                                        personagem.nivel += 1
                                        personagem.poder += 10
                                        print('jorginho mesmo ganhando a luta sente que perdeu algo...talvez sua sanidade.\nmas pelo lado bom jorginho subiu de nivel seja la o que isso significa')
                                        print(
                                            'como um bom jogador de RPG mesmo não querendo jorginho saqueia seu inimigo')
                                        print(
                                            'ele pega : \n1-um biquine\n2-um objeto longo de borracha com um cheiro ruim(talvez de para usar como arma)')
                                        sleep(0.5)
                                        print('~~~'*40)
                                        personagem.poder += 5
                                    else:
                                        opc = 0
                                        sleep(1)
                                        print('serio quer que eu desenhe, escolhe logo 1 ou 2')
                                        sleep(0.5)
                                        print('~~~'*40)
                            elif acao == '2':
                                sleep(1)
                                print('jorginho não lembra muito bem o que aconteceu... mas ele tem certeza que não ganhou nem um doce so dificuldades para andar e ficar sentado')
                                print('jorginho vai andando com dificuldades par a empresa')
                                sleep(0.5)
                                print('~~~'*40)
                                op = False
                                personagem.sanidade -= 5
                                relogio.avancaTempo(15)
                            else:
                                sleep(1)
                                print('serio quer que eu desenhe, escolhe logo 1 ou 2')
                                op = True
                                acao = (input('acão ? '))
                                sleep(0.5)
                                print('~~~'*40)
                    if dia == 3:
                        sleep(1)
                        print("depois que o jorginho saiu do onibus e estava andando para chegar no trabalho\ne encontra um pedaço de papel no chão  ")
                        print('ao olhar para o papel ele percebe que e um mapa')
                        mapa=input('o que jorginho vai fazer :\n1=seguir o mapa\n2=ignorar o mapa e ir trabalhar\nação ?')
                        sleep(0.5)
                        print('~~~'*40)
                        pa=True
                        colar=False
                        while pa == True:
                            if mapa == '1':
                                pa=False
                                sleep(1)
                                print('jorginhoa segue o mapa e chega em uma arvore gigante')
                                print('a terra perto da arvore parece ter cido revirada ')
                                print('jorginho como não e besta de seguir um mapa atoa ele cava perto da arvore')
                                print('depois de cava jorginho acha um colar feito de safira ')
                                personagem.vida+=50
                                relogio.avancaTempo(50)
                                sleep(0.5)
                                print('~~~'*40)
                                colar=True
                            elif mapa == '2':
                                pa = False
                                sleep(1)
                                print('jorginho percebe que o mapa foi feito por uma criança e pensa que e uma brincadeira\ne volta ao seu rumo para o trabalho')
                                sleep(0.5)
                                print('~~~'*40)
                            else:
                                pa = True
                                sleep(1)
                                print('serio mesmo digita logo 1 ou 2')
                                mapa=input('ação ?')
                                sleep(0.5)
                                print('~~~'*40)
                    if dia == 4:
                        sleep(0.5)
                        print('~~~'*40)
                        sleep(1)
                        print('quando jorginho  estava correno para não chegar atrasado no trampo ele encontra uma pessoa de capuz')
                        print('a pessoa de capuz fala para jorginho ')
                        print('"se você quiser continuar andando passa a carteira"')
                        print('logo depois de terminar de falar ele saca uma faca')
                        print('o que fazer.\n1=ser corajoso uma vez na vida e atacar.\n2=ser um bundao e passar a grana para o assaltante')
                        acao = (input('acão ? '))
                        sleep(0.5)
                        print('~~~'*40)
                        op = True
                        while op == True:
                            if (acao == '1'):
                                opc = 0
                                op = False
                                while opc == 0:
                                    sleep(1)
                                    print('jorginho lembra dos anime que asistiu pela madrugada e pensa que é um protagonista e parte para cima do assaltante')
                                    print()
                                    npc2.vida = npc2.vida-personagem.poder
                                    print('assaltante olha com cara de curiosidade para jorginho e contra ataca ele com um chute na barriga')
                                    print()
                                    sleep(1)
                                    personagem.vida = personagem.vida-npc2.ataque
                                    print('jorginho perde o ar mas continua em pé')
                                    sleep(0.5)
                                    print('~~~'*40)
                                    sleep(1)
                                    opc = 0
                                    aci = (input(
                                        'escolha : \n\n1=ser idiota e atacar novamente\n2=ser um bundao e passar a carteira\n\nacão ? '))
                                    sleep(0.5)
                                    print('~~~'*40)
                                    if aci == '1':
                                        sleep(1)
                                        print(
                                            'jorginho lembra que um protagonista nunca desiste vai atacar o assaltante de novo')
                                        
                                        sleep(1)
                                        npc2.vida = npc2.vida-personagem.poder
                                        print('jorginho leva um ataque')
                                        personagem.vida = personagem.vida-npc2.ataque
                                        opc = 0
                                        acai = (input(
                                            'escolha : \n\n1=ser idiota e atacar\n2=ser um bundao\n\nacão ? '))
                                        
                                        if npc2.vida <= 0:
                                            sleep(1)
                                            print(
                                                'jorginho quase perdendo a consciência mas consegue dar o ataque final\n em seu inimigo')
                                            sleep(0.5)
                                            print('~~~'*40)
                                            sleep(1)
                                            personagem.sanidade += 2
                                            print(
                                                'jorginho como um bom jogador de RPG saqueia o corpo do assaltante\nitens adiquiridos :\n1-faca\n2-R$300\n3-um maço de derbi')
                                            print('depois de dar uma surra no assaltante jorginho vai para a empresa')
                                            sleep(0.5)
                                            print('~~~'*40)
                                            personagem.nivel += 1
                                            personagem.poder += 20
                                            personagem.vida += 100
                                            opc = 1
                                        elif personagem.vida <= 0:
                                            sleep(1)
                                            print('depos de apanhar muito jorginho desmaia')
                                            sleep(0.5)
                                            print('~~~'*40)
                                            sleep(1)
                                            personagem.sanidade -= 4
                                            personagem.dinheiro = personagem.dinheiro-personagem.dinheiro
                                            opc = 1
                                            relogio.avancaTempo(30)
                                            print(
                                                'depois de um tempo jorginho acorda ,com seu copo dolorido e sem sua\n carteira mesmo com dificuldade ele vai para o trampo')
                                            sleep(0.5)
                                            print('~~~'*40)
                                            
                                    elif aci == '2':
                                        sleep(1)
                                        print('jorginho viu que não tinha como vencer e entraga a carteira para o assaltante')
                                        print('"você fez uma boa escolha"')
                                        print('o assaltante pega a carteira e sai andando em diresão a um beco')
                                        print('como jorginho foi assatado ele sente mais vontade de ir trabalhar\n , porque sua divida estava bem alta')
                                        sleep(0.5)
                                        print('~~~'*40)
                                        relogio.avancaTempo(15)
                                        sleep(0.5)
                                        print('~~~'*40)
                                        personagem.dinheiro = personagem.dinheiro-personagem.dinheiro
                                        personagem.sanidade -= 4
                                        opc = 1
                                        relogio.avancaTempo(20)
                                    else:
                                        sleep(1)
                                        opc = 0
                                        print('voce e burro ou se faz, escolha 1 ou 2')
                                        aci=input('ação ?')
                                        sleep(0.5)
                                        print('~~~'*40)
                            elif acao == '2':
                                sleep(1)
                                personagem.dinheiro = personagem.dinheiro-personagem.dinheiro
                                print(f'jorginho passa a carteira para o assaltante e perde todo seu dinhero e sua dignidade')
                                relogio.avancaTempo(15)
                                op = False
                            else:
                                sleep(1)
                                print('voce e burro ou se faz, escolha 1 ou 2')
                                op = True
                                acao = (input('acão ? '))

                    if dia  == 5:
                        if colar == True:
                            sleep(1)
                            print('jorginho estava quase chegando no trabalho quando uma mulher para ele')
                            print('"esse colar eu reconheço, ele é meu, minha filha pegou ele para brincar"')
                            print('"ela falou que timha deixado pistas para eu achar, mas ja faz dois dias que eu to procurando"')
                            print('"acho que você achou primeiro, será que pode me devolver ?"')
                            escolha=input('escolhas :\n1=ser bom e devolver\n2=correr muito\nação ?')
                            sleep(0.5)
                            print('~~~'*40)

                            esc=True
                            while esc == True:
                                if escolha == '1':
                                    esc=False
                                    print('jorginho logo pensando na reconpença entrga o colar para a mulher')
                                    personagem.vida-=50
                                    personagem.dinhero+=700
                                    print('"obrigado por devolver, esse colar e muito inportante para mim"')
                                    print('"fiuque com isso como agradecimento"ela fala entregando R$1000 reais para jorginho')
                                    print('depois disso jorginho vai todpo feliz para o trabalho')
                                    sleep(0.5)
                                    relogio.avancaTempo(15)
                                    print('~~~'*40)
                                elif escolha == '2':
                                    esc=False
                                    print('jorginho corre o mais rapido que pode')
                                    print('depois de 10 minutos correndo ele consegue dispistar ela e chegar no trabalho')
                                    sleep(0.5)
                                    relogio.avancaTempo(10)
                                    print('~~~'*40)
                                else:
                                    print('para de frescura e digite 1 ou 2 logo')
                                    esc=False
                                    escolha=input('ação ?')
                                    sleep(0.5)
                                    print('~~~'*40)

                    if dia == 6:
                        sleep(0.5)
                        print('~~~'*40)
                        sleep(1)
                        print('na entrada do serviço de jorginho tinha uma barraca que ele nunca tinha visto antes')
                        print('"barraca da sorte \nentre e se divirta"')
                        sleep(0.5)
                        print('~~~'*40)
                        sleep(1)
                        aca = input(
                            'oque fazer :\n1=entrar e testar a sorte\n2=ir trabalhar logo')
                        sleep(0.5)
                        print('~~~'*40)
                        pp = True
                        while pp == True:
                            if aca == '1':
                                pp = False
                                sleep(1)
                                print(
                                    'jorginho entra na barraca que incrivelmente parece muito maior por dentro')
                                print(
                                    '"chege mais perto meu caro otar...digo pessoa de sorte " dis um velho que esta atrás de uma mesa')
                                print(
                                    '"vejo que veio testar sua sorte, e bem simples eu vou jogar um dado e você tenta adivinhar se ele e par ou inpar"')
                                print(
                                    '"se você acertar guanha um item se errar não guanha nada o que acha ?"')
                                print(
                                    '"mas é claro que isso por uma pequena taxa de R$500 reais "')
                                sleep(0.5)
                                print('~~~'*40)
                                sleep(1)
                                aa = input(
                                    'oque fazer :\n1=ser um otar...bom cliente\n2=sair e ir trabalhar\nação ? ')
                                sleep(0.5)    
                                print('~~~'*40)
                                pci = 0
                                while pci == 0:
                                    nu = ''
                                    dado = randint(1, 6)
                                    if(dado % 2 == 0):  # par
                                        nu = '1'
                                    else:
                                        nu = '2'  # impar
                                        if aa == '1':
                                            personagem.dinheiro -= 500
                                            pci = 1
                                            jogador = input(
                                                '1=par\n2=impar\nescolha : ')
                                            sleep(0.5)
                                            print('~~~'*40)
                                            if jogador == nu:
                                                sleep(0.5)
                                                print('~~~'*40)
                                                sleep(1)
                                                print('você acertou')
                                                print(
                                                    '"não era para nimguem acertar, nunca confie nos desenvolvedores...digo que coisa otima, agora voce pode escolher um premio eu acho ')
                                                print(
                                                    'o velho tira uma caixa de baixo da mesa ')
                                                print(
                                                    '"eu tenho otimos premios aqui você vai ADORAR"')
                                                sleep(0.5)
                                                print('~~~'*40)
                                                sleep(1)
                                                itens = input(
                                                    'dento da caixa tem dois itens :\n1-liquido suspeito vermelho\n2-liquido suspeito verde')
                                                sleep(0.5)    
                                                print('~~~'*40)
                                                con = 0
                                                while con == 0:
                                                    if (itens == '1'):
                                                        sleep(1)

                                                        print(
                                                            'jorginho pega o frasco vermelho e da uma golada')
                                                        print(
                                                            'jorginho sente a energia de 1.000 marombeiros dentro dele...')
                                                        print(
                                                            'depos disso jorginho vai para o trabalho')
                                                        sleep(0.5)
                                                        print('~~~'*40)
                                                        personagem.poder += 20
                                                        con = 1
                                                    elif (itens == '2'):
                                                        sleep(0.5)
                                                        print('~~~'*40)
                                                        sleep(1)
                                                        print(
                                                            'jorginho pega o frasco verde e da uma golada')
                                                        print(
                                                            'jorginho sente a energia de um monge belga dentro dele')
                                                        print(
                                                            'depos disso jorginho vai para o trabalho')
                                                        sleep(0.5)
                                                        print('~~~'*40)
                                                        personagem.vida += 50
                                                        con = 1
                                            elif jogador != nu:
                                                sleep(1)
                                                print(
                                                    'errou...errou feio...errou rudi')
                                                sleep(0.5)
                                                print('~~~'*40)
                                                pci = 1
                                            else:
                                                pci = 0
                                                sleep(1)
                                                print(
                                                    'eu sei que voce é idiota mas escolhe logo 1 ou 2')
                                                jogador = input('ação ?')
                                                sleep(0.5)
                                                print('~~~'*40)
                                        elif aa == '2':
                                            pci = 1
                                            sleep(1)
                                            print(
                                                'jorginho logo percebe que isso e uma cilada e vasa da li e continua seu rumo para o trampo')
                                            personagem.sanidade += 1
                                        else:
                                            pci = 0
                                            print(
                                                'eu sei que voce é idiota mas escolhe logo 1 ou 2')
                                            aa = input('ação ? ')
                                            sleep(0.5)
                                            print('~~~'*40)
                            elif aca == '2':
                                sleep(1)
                                print(
                                    'jorginho ignora a barraca e entra na empresa')
                                pp = False
                            else:
                                print(
                                    'eu sei que voce é idiota mas escolhe logo 1 ou 2')
                                aca = input('ação ?')
                                sleep(0.5)
                                print('~~~'*40)
                                pp = True
                else:
                    sleep(1)
                    print('escolha umas das duas opçoes validas')
                    opc = 0

            
            recebido = personagem.salario
            if(personagem.sanidade < 1):
                sleep(1)
                print("jorgimho esta de saco cheio da vida e decide voltar para casa e jogar o dia todo")
                sleep(0.5)
                print('~~~'*40)
                recebido = 0

            elif(relogio.atrasado()):
                sleep(1)
                print("alem do jorginho chegar atrasado teve que escutar muitas reclamações do seu chefe.ele produziu menos do que de costume.")
                sleep(0.5)
                personagem.sanidade -= 1
                recebido *= 0.3
            elif(personagem.sujo):
                sleep(1)
                print(
                    "jorginho estava sujo, o seu chefe não aguentou o seu cheiro e descontou do salario dele .")
                sleep(0.5)
                print('~~~'*40)
                recebido *= 0.4
            elif(personagem.fome):
                sleep(1)
                print("jorginho estava morrendo de fome, e não teve um rendimento bom no trampo.")
                sleep(0.5)
                print('~~~'*40)
                recebido *= 0.5
            
            print("jorginho recebeu "+str(recebido) +
                  " reais merecidos pelo seu trabalho hoje.")
            print()
            print('depois de trabalhar muito jorginho decide ir para casa dormi ')
            sleep(1)
            print('~~~'*40)

            personagem.dinheiro += recebido
            personagem.dormir()
            relogio = Relogio()
            dia += 1
        elif(opcao == "0"):
            break
        else:
            sleep(1)
            print("para de ser sem infancia e escolha logo uma opção valida")
            
