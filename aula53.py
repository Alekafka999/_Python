'''
Docstring for aula53
enumareta - enumera iteráveis (índices)
'''

lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')


for tupla_enumerada in enumerate(lista):
    print('FOR da tupla:')
    for valor in tupla_enumerada:
        print(f'{valor}')  




'''
for indice, nome in enumerate(lista):
    print(indice, nome)



lista_enumerada = enumerate(lista)
print(next(lista_enumerada))

for item in lista_enumerada:
    print(item)

'''

