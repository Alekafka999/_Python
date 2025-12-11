'''
Docstring for aula51
Introdução ao desempacotamento

_, _, nome, *resto = ['Maria', 'Helena', 'Luiz']

print(nome)

'''
_, nome, *resto = ['Maria', 'Helena', 'Luiz']
nome1, *_ = ['Maria', 'Helena', 'Luiz']
print(nome1, _)