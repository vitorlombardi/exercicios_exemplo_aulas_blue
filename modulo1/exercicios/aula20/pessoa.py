from telefone import Telefone


class pessoa():
    def __init__(self, nome, idade, cpf, telefone):
        self.__nome = nome
        self.__cpf = cpf
        self.__idade = idade
        self.__telefone = Telefone(telefone)


#gets

    def get_nome(self):
        return self.__nome

    def get_idade(self):
        return self.__idade

    def get_cpf(self):
        return self.__cpf

    def get_telefone(self):
        return self.__telefone


#set

    def set_nome(self, nome):
        self.__nome = nome

    def set_idade(self, idade):
        self.__idade = idade

    def set_cpf(self, cpf):
        self.__cpf = cpf

    def set_telefone(self, telefone):
        self.telefone = Telefone().setTelefonr(telefone)
