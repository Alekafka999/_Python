'''
Operadores Lógicos - OU (disjunção)
Qualquer condição verdadeira torna a expressão verdadeira
Alessandra tem olhos azuis ou pretos
Alessandra tem olhos azuis. Logo, a expressão é verdadeira

Falsy -> 0 0.0 '' False
Truthy -> Qualquer coisa diferente disso
None -> Usado para representar um não valor


entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')

senha_permitida = '123'

if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')
'''
#Avaliação de curto circuito
senha = input('Senha: ') or 'Sem senha'
print(senha)
