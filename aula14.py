'''
No Python, tudo é objeto!
Objeto - executa ações (métodos) - Fazem ações com os dados que eles armazenam (atributos).

'''


a = 'A'
b = 'B'
c = 1.1

string = 'b = {nome2} a = {nome1} b = {nome2} c = {nome3:.2f}'
formato = string.format(
    nome1=a, nome2=b, nome3=c
    
) 

#string format - parêmetro nomeado


print(formato)