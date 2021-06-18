# classe -> molde para criar objetos
# objetos-> intancias da minha classe(partre funcional)
# atributos-> caracteristicas dos objetos
# metodos->ações que os objetos executam

#exelplo:
# classe:heroi
# objeto: miranha
# atibutos: nome, idade, peso, altura
# metodos: engordar

class herói():
    def __init__(self,nome, idade, peso, altura):
        self.nome=nome
        self.idade=idade
        self.peso=peso
        self.altura=altura


    def engordar(self,peso):
        self.peso+=peso

heroi=herói('miranha',20,75,1.80)
print(heroi.nome)
print(heroi.idade)
print(heroi.peso)
print(heroi.altura)
print (vars(heroi))
heroi.engordar(10)
print(vars(heroi))

at=dict(vars(heroi))
for k,v in at.items():
    print(f'{k} : {v} ')

