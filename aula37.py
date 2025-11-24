'''
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
'''

contador = 1

while contador < 23:
    contador += 1
    print(contador)

    if contador == 5:
        print('Chegou no 5')
        continue
    if contador >= 10 and contador < 15:
         print('Não vou mostrar o', contador)
         continue

    else:
        print('Não chegou no 25')    
        continue


print('F-I-M-!')



