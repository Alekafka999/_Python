'''
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> quando o código não tem fim


condicao = True

while condicao:
    nome = input('Qual o seu nome? ')
    print(f'Seu nome é {nome}')

    if nome == 'sair':
        break

print('Agora acabou!')
'''


contador = 0

while contador <= 15:
    contador = contador + 1
    if contador == 6:
        print('666 The Number of the Beast')
        continue
    if contador == 13:  
        print('13 é o verdadeiro número das bestas')  
        continue
    if contador >= 16:
        break

    print(contador)
print('Cest la vie')
