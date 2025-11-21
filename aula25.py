'''
Interpolação BÁSICA de strings

s - string
d e i - int
f - float (número de ponto flutuante)
x e X - Hexadecimal (ABCDEF0123456789)
'''

nome = 'Luiz'
preco = 1000.95897643
variavel = '%s, o preço é R$%.2f' % (nome, preco)
print(variavel)
print('O hexadecimal de %d é %04X' % (1500, 1500))

'''
Formatação básica de strings
s - string
d - int
f - float
.<número de dígitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)(tipo - s, d ou f)

> - Esquerda
< - Direita
^ - Centro
= - Força o número a aparecer antes dos zeros
'''