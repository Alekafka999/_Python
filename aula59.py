'''
Docstring for aula59


Desempacotamento em chamadas
de métodos e funções

'''

string = 'ABCD'
lista = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']
tupla = 'Python', 'é', 'legal'

#a, b, c, d, e, f = lista
#print(a, b, c, d, e, f)

print(*lista, sep=' - ')
print(*string, sep=' - ')
print(*tupla, sep=' - ')