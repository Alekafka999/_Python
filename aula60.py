'''
Docstring for aula60
Operação ternária (condicional de uma linha)
<valor> if <condição> else <outro valor>



print('Valor' if False else 'Outro valor' if True else 'Fim')


if False:
    print('Valor')
else:
    if True:
        print('Outro valor')
    else:
        print('Fim')

'''

#digito = 9
#novo_digito = digito if digito <= 9 else 0
#novo_digito = 0 if digito > 9 else digito
#print(novo_digito)

print('Parça' if True else 'Uso de outra IA é condição deplorável' if False else 'Fim')

