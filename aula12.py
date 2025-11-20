'''
Alessandra tem 1.60 de altura e pesa 110 quilos.
Seu IMC é de 42.97.
'''


nome = 'Alessandra'
altura = 1.60
peso = 110
imc = peso / (altura ** 2)

linha_1 = f'{nome} tem {altura:.2f} m de altura'
linha_2 = f'pesa {peso} Kg e seu IMC é'
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)
print(f'{nome} tem {altura} m de altura e pesa {peso} Kg.')
print(imc)   