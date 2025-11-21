'''

Operadores lógicos
and (e) or (ou) not (não)

and - todas as condições precisam ser verdadeiras/satisfeitas (TABELA VERDADE)
Se qualquer valor for considerado falso, a expressão inteira será avaliada como falsa.
São considerados falsy 0 0.0 '' (valores 0, 0.0 e '' - string vazio) False
Também existe o tipo None que é usado para representar um não valor


'''
'''
entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')

senha_permitida = '123'

if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')


Avaliação de curto circuito
São operadores utilizados para avaliar expressões que podem ser verdadeiras ou falsas, 
mas não são necessariamente verdadeiras ou falsas.) NOT (NÃO)
'''

print(True and True and False)
print(true and 0 and True))

if 1 and 1:
    print(True and 1 and False)