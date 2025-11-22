'''
Flag (Bandeira) - Marcar um local
None = Não valor
is e is not = é ou não é (tipo, valor, identidade)
id = Identidade

v1 = 'a'
v2 = 'a'
print(id(v1))
print(id(v2))
print(v1 is v2)

'''

condicao = False
outra_condicao = False
passou_no_if = None

if condicao:
    passou_no_if = True
    print('Faça algo')

elif outra_condicao:
    print('Faça outra coisa')

else:
    print('Não faça nada')

if passou_no_if is None:
    print('Não passou no if')
else:
    print('Passou no if')
