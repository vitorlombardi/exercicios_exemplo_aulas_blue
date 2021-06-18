from pessoa import pessoa
#herança

class Pessoa_Advogado(pessoa):
    
    def __init__(self,oab, nome, idade, cpf, telefone):
        self.__oab=oab
        super().__init__(nome, idade, cpf, telefone)


    def get_oab(self):
        return self.__oab

    def set_oab(self,oab):
        self.__oab=oab

