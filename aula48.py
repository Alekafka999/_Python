'''
Docstring - Vídeos 81 e 82

Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo de dado
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, +
Creat Read Update Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)



string = 'ABCDE' # 5 caracteres (len)
lista = [123, True, 'Luiz Otávio', 1.2, []] # 5 elementos (len)

print(lista, type(lista))

lista[-3] = 'Maria'
print(lista[2], type(lista[2]))
print(lista)



lista = [10, 20, 30, 40, 50]
lista[2] = 666
numero = lista[2]

print(numero)
print(lista[2])



lista = [10,20,30,40,50]
lista.append(60)
print(lista)

lista.pop()
print(lista)

lista.append(70)
print(lista)

ultimo_valor = lista.pop()
print(lista,"Removido:",ultimo_valor)


Métodos úteis:
appende - Adiciona um item ao final da lista
insert - Adiciona um item no índice escolhido
pop - Remove o último item ou o item do índice escolhido (retorna o item removido)
del - Remove um item pelo índice (não retorna o item removido)
clear - Remove todos os itens da lista
extend - Estende a lista adicionando outros valores (uma lista ou qualquer iterável)
+ - Concatena listas - polimorfismo


lista = [10,20,30,40,50]
lista.insert(2,666)
nome = lista.pop()
lista.append(1233)
del lista[1]
print(lista)

lista_a = [1,2,3]
lista_b = [4,5,6]
lista_c = lista_a + lista_b
print(lista_c)



lista_a = ['Luiz', 'Maria', 1, 2, False]
lista_b = lista_a.copy()

lista_a[0] = 'Qualquer coisa'

print(lista_b)

'''

