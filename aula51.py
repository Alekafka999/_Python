'''
Docstring for aula51
Introdução ao desempacotamento + tuples (tuplas)

_, _, nome, *resto = ['Maria', 'Helena', 'Luiz']

print(nome)

_, nome, *resto = ['Maria', 'Helena', 'Luiz']
nome1, *_ = ['Maria', 'Helena', 'Luiz']
print(nome1, _)

'''

nomes = ['Maria', 'Helena', 'Luiz']
nome1, nome2, nome3 = nomes