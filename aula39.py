'''
iterando strings com while

EXERCÍCIO: adiciona um * antes de cada letra de um nome
Exemplo - nome: Luiz
Fazer com loop e concatenação
Resultado *L*U*I*Z*

'''

contador = 1 

while contador <= 6:
    print(*'contador')     

    if contador == 6:
        print('Chegou no 6')
        continue

print('F-I-M-!')


