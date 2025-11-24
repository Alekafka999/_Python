'''
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira

Loop infinito

'''

qtd_linhas = 2
qtd_colunas = 3

linha = 1
while linha <= qtd_linhas:
    coluna = 1
    while coluna <= qtd_colunas:
        print(f'{linha = }, {coluna = }') #letra maiúscula Linha / Coluna não funciona
        coluna += 1
    linha += 1

print('Acabou')