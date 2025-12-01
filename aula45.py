'''

iterável -> (___ITER___) str, list, tuple, set, dict, range etc
Iterador -> um objeto que pode ser iterado (um objeto que retorna um elemento por vez quando a função next() é chamada)
next -> função built-in que chama o próximo elemento do iterador (ENTREGA O PRÓXIMO VALOR DO ITERADOR)
iter -> me entregue o seu iterador

'''

texto = 'Python'
numeros = range (0, 100, 12)

for numero in numeros:
    print(numero)