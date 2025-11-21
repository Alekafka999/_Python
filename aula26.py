'''
Formatação de strings
 s - string
 d - int
 f - float
 .<número de dpigitos>f
 x ou X - Hexadecimal
 (Caractere)(><^)(quantidade)(tipo - s, d ou f)

 > - Esquerda
 < - Direita
 ^ - Centro
 Sinal - + ou -
 Ex.: 0>-100, .1f
 Conversion flags: - !r !s !a
 = - Força o número a aparecer antes dos zeros
'''

nome = 'Alessandra'
print(f'{nome:/^100}')

variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}')
print(f'{variavel: ^10}')
print(f'{variavel:$^10}.')
print(f'{1000.4873648123746:0>+10,.1f}')
print(f'O hexadecimal de 1500 é {1500:08X}')
print(f'{variavel!r}')

