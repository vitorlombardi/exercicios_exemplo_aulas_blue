class funciorario:
    def __init__(self,nome,cargo,valor_h_t):
        self.nome=nome
        self.cargo=cargo
        self.__valor_h_t=valor_h_t
        self.__horas_t=0
        self.__salario=0

    @property
    def salario(self):
        return self.__salario


    @salario.setter
    def salario(self,novo_salario):
        raise ValueError ('impossivel alterar salario diretamente, utilize a função calcula_salario')

    def registra_h_T(self,horas_tra):
        self.__horas_t=horas_tra

    def calcula_salario(self):
        self.__salario=self.__horas_t*self.__valor_h_t

jorginho=funciorario('jorginho','dev junior',500)
jorginho.registra_h_T(10)
jorginho.calcula_salario()
jorginho.__salario=500
print(jorginho.salario)
print(jorginho.__salario)

