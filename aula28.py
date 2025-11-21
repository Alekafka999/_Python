'''
Exercício - Vídeo 47
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Nome invertido
        Nome com todas as letras maiúsculas
        Nome com todas as letras minúsculas
        Quantas letras ao todo (sem considerar espaços)
        Quantas letras tem o primeiro nome
        Se o nome contém (ou não) espaços
        Se o nome contém (ou não) números
        Quantas vezes o caractere aparece no nome
        Primeira e última letra do nome
        "As letras do seu nome são: ", {letras do nome separadas por vírgula}
Obs.: Se o usuário digitar um número no lugar do nome, o programa irá mostrar uma mensagem de erro.
'''
nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

if nome.isdigit() or idade.isdigit():
    print('Você digitou um número no lugar do nome ou idade.')
else:
    print(f'Nome invertido: {nome[::-1]}')
    print(f'Nome com todas as letras maiúsculas: {nome.upper()}')
    print(f'Nome com todas as letras minúsculas: {nome.lower()}')
    print(f'Quantas letras ao todo (sem considerar espaços): {len(nome.replace(" ", ""))}')
    print(f'Quantas letras tem o primeiro nome: {len(nome.split()[0])}')
    print(f'Seu nome contém espaços? {"Sim" if " " in nome else "Não"}')
    print(f'Seu nome contém números? {"Sim" if nome.isnumeric() else "Não"}')
    print(f'Quantas vezes o caractere "a" aparece no nome? {nome.lower().count("a")}')
    print(f'Primeira letra do nome: {nome[0]}')
    print(f'Última letra do nome: {nome[-1]}')
    print(f'As letras do seu nome são: {", ".join(nome.split())}')

