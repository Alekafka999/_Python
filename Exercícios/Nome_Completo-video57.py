#3. Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 lertas ou menos, escreva: "Seu nome é curto".
 # Se tiver entre 5 e 6 letras, "Seu nome é normal". Se tiver mais que 6 letras, "Seu nome é muito grande!" E se tiver espaço?
'''
nome = input('Digite seu primeiro nome: ')

if nome.isdigit():
    print('Você digitou um número no lugar do nome ou idade.')
else:
    print(f'Seu nome é {nome}')
    print(f'Quantas letras ao todo (sem considerar espaços): {len(nome.replace(" ", ""))}')
    
if len(nome.replace(" ", "")) <= 4:
    print('Seu nome é curto')
elif len(nome.replace(" ", "")) <= 6:
    print('Seu nome é normal')
else:
    print('Seu nome é muito grande! Só pessoas lindas possuem o nome cumprido como o seu :)')
'''


nome = input('Digite seu nome: ')
tamanho_nome = len(nome)

if tamanho_nome > 1:
    if tamanho_nome <= 4:
        print('Seu nome é curto')
    elif tamanho_nome >= 5 and tamanho_nome <= 6:
        print('Seu nome é normal')
    else:
        print('Seu nome é muito grande')
else:
    print('Digite mais de uma letra')


