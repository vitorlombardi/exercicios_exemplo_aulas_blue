from pessoa import pessoa



class pessoa_medico(pessoa):
    def __init__(self,crm, nome, idade, cpf, telefone):
        self.__crm=crm
        super().__init__(nome, idade, cpf, telefone)

        def get_crm(self):
            return self.__crm

        def set_crm(self,oab):
            self.__crm=crm