desafio = 'ex004'
print('{:=^30}'.format(desafio))
algo = input('digite algo: ')
if algo.isnumeric():
    print('é numérico')
else:
    print('não é numérico')
