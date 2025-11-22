'''
EXERCÍCIO

1. Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.




#exercício 1

numero = input('Digite um número inteiro: ')

if numero.isdigit():
    numero = int(numero)
    if numero % 2 == 0:
        print(f'{numero} é par')
    else:
        print(f'{numero} é ímpar')
else:
    print('Não é um número inteiro')


Solução do professor

if numero_inteiro % 2 == 0:
    print(f'{numero_inteiro} é par')
else:
    print(f'{numero_inteiro} é ímpar')

'''

# 2. Faça um programa que pergunte a hora ao usuário e, baseado no horário descrito, exiba a saudação apropriada
# bom dia: 0 - 11  boa tarde 12 - 17 boa noite 18-23

horario = input('Digite a hora: ')

if horario >= 0 and horario <= 11:
    print('Bom dia!')
    print('Tenha um bom dia!')



#3. Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 lertas ou menos, escreva: "Seu nome é curto".
 # Se tiver entre 5 e 6 letras, "Seu nome é normal". Se tiver mais que 6 letras, "Seu nome é muito grande!" E se tiver espaço?

 