'''
Operadores in e not in
Strings são iteráveis -> navegar item por item
 0 1 2 3 4 5
 O t á v i o
-6-5-4-3-2-1

nome = 'Otávio'
print(nome[2])
print(nome[-4])
print('á' in nome)
print('z' in nome)
print('vio' in nome)
print('z' not in nome)
print('vio' not in nome)

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')


nome = 'P&dr0 Henriqu3'

if ' ' in nome:
    print(f'{nome} possui espaços')
else:
    print(f'{nome} não possui espaços')

numero =-5

if numero>10:
    if numero>25:
        if numero>50:
            print('Número maior que 3')
        else:
            print('Número menor que 3')
    else:
        print('Número menor que 2')
else:
    print('Número menor que 1')
'''

variavel_a = 1 or 0
variavel_b = 0 or 1
print(variavel_a, variavel_a)