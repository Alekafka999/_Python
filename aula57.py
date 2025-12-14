'''
Docstring for aula57
Revisão: Lista de listas + índices

    # 0        1
    ['Maria', 'Helena', ],  # 0
    # 0
    ['Elaine', ],  # 1
    # 0       1       2
    ['Luiz', 'João', 'Eduarda', (1,1,2,3,5,8)],  # 2
]

print(salas[2][2])
print(salas[2][3][2])

'''

def fibonacci(n):
    seq = []
    a, b = 1, 1
    for _ in range(n):
        seq.append(a)
        a, b = b, a + b
    return seq

print(fibonacci(20))
