class mamifero():
    def som(self):
        print('superclass: emitir som')

class homem(mamifero):
    def som(self):
        print('humano: pao de batata')


class cachorro(mamifero):
    def som(self):
        print('cachorro: au! au! wuuf!')



class gato(mamifero):
    def som(self):
        print('gato: miau')



print("polimorfismo na pratica\n")


Mamifero=mamifero()
Mamifero.som


animais=[homem(),cachorro(),gato()]

for a in animais:
    a.som()




