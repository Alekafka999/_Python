for i in range(15):
    if i == 3:
        print('i é 2, pulando...')
        continue

    if i == 25 :
        print('i é 8, seu else não executará')
        break

    for j in range(1,3):
        print(i,j)

else:
    print('For: só sucesso, brou!')