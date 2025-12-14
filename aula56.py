'''
Docstring for aula56

split e join com list e str
split - divide uma string
join - une uma string


'''

frase = "Python é lindo demais. Olha só, que coisa interessante!"
palavras_cruas = frase.split(',')

palavras = []
for i, frase in enumerate(palavras_cruas):
    palavras.append(palavras_cruas[i].strip())


#print(palavras_cruas)
#print(palavras)

frases_unidas = ' -- '.join(palavras)
print(frases_unidas)
