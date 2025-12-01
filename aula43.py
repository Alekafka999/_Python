''' texto = 'EU NÃO GOSTO DE PHP'

i = 0
tamanho_string =len(texto)

while i < tamanho_string:
    print(texto[i], i)

    i += 1
    '''
#iterável = entrega um elemento da string por vez

texto = 'Odeio PHP'
novo_texto = ''

for letra in texto:
    novo_texto += f'*{letra}'
    print(letra)