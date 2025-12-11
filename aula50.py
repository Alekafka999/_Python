'''
Docstring for aula50
Exercício
Exiba os índices da lista

'''

lista = ['Maria', 'Helena', 'Luiz', 'Alessandra', 'Parça']

indices = range(len(lista))

print(indices)

for indice in indices:
    print(indice, lista[indice], type(lista[indice]))
    print(lista.index(lista[indice]), lista[indice])
