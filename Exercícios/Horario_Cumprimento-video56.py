# 2. Faça um programa que pergunte a hora ao usuário e, baseado no horário descrito, exiba a saudação apropriada
# bom dia: 0 - 11  boa tarde 12 - 17 boa noite 18-23

hora = input('Que horas são? Digite apenas números inteiros...: ')

if hora.isdigit():
    hora = int(hora)
    if 0 <= hora <= 11:
        print('Bom dia!')
    elif 12 <= hora <= 17:
        print('Boa tarde!')
    elif 18 <= hora <= 23:
        print('Boa noite!')
    else:
        print('Hora inválida!')
else:
    print('Digite apenas números!')


'''
entrada = input('Digite a hora em números inteiros: ')

    try:
    hora = int(entrada)

    if hora >= 0 and hora <= 11:
    
    elif hora >= 12 and hora <= 17:
    
    elif hora >= 18 and hora <= 23:

    else:
        print('Não conheço essa hora')
except:
    print ('Por favor, digite apenas números inteiros')

 

'''