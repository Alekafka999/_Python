'''
Docstring for aula41

while/else

'''

string = 'Valor_Qualquer'
i = 0
while i < len(string):
    letra = string[i]

    if letra == ' ':
        break

    print(letra)
    i += 1

else:
        print('Não encontrei um espaço vazio na string')

print('Fora do while')
