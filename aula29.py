'''

Introdução ao TRY/EXCEPT
try -> tentar executar o código
    # Execução problematica
except -> ocorreu algum erro ao tentar executar
    # Ocorreu algum erro

    if -> Checa uma condição. Se acontecer um erro/exceção, o programa para
    
'''

numero_str = input('Vou dobrar o número que você digitar: ')

try:
    numero_float = float(numero_str)
    print('FLOAT:', numero_float)
    print(f'O dobro de {numero_str} é {numero_float * 2:.9f}')
except:
    print('Isso não é um número')

'''
OBS: Se o usuário digitar uma letra, o programa irá dar erro, pois não é possível converter uma letra para float.
Para evitar isso, podemos usar o try/except para tratar esse erro.

'''