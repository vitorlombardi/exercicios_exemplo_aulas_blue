from pessoaAdvogado import Pessoa_Advogado
from pessoaMedico import pessoa_medico


lista_m=[]
lista_a=[]

pessoa_m1=pessoa_medico(123456,'jorginho',25,65432112345,16253409)
pessoa_m2=pessoa_medico(654321,'miranha',20,12345678923,98765432)

lista_m.append(pessoa_m1)
lista_m.append(pessoa_m2)

pessoa_a1=Pessoa_Advogado(1234,'paulo',65,50432112345,243409)
pessoa_a2=Pessoa_Advogado(6543,'jurema',58,52345678987,63765432)

lista_a.append(pessoa_a1)
lista_a.append(pessoa_a2)


print('~'*40)
print('adivogados : ')
for ad in lista_a:
    print('OAB: {} | nome: {} | idade: {}'.format(ad.get_oab(),ad.get_nome(),ad.get_idade()))
    print('CPF: {} | tel : {} |'.format(ad.get_cpf(),ad.get_telefone().get_telefone()), end='\n\n')
print('~'*40)
print('medicos : ')
for md in lista_a:
    print('CRM: {} | nome: {} | idade: {}'.format(md.get_crm(),md.get_nome(),md.get_idade()))
    print('CPF: {} | tel : {} |'.format(md.get_cpf(),md.get_telefone().get_telefone()), end='\n\n')
print('~'*40)

