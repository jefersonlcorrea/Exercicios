desafio = 'ex009'
print('{:=^30}'.format(desafio))
#numero = int(input('Digite o número para exibir a tabuáda: '))
for x in range(10):
    print('\nTabuada do {}'.format(x + 1))
    for y in range(10):
        print('{} X {} = {}'.format(x+1,y+1,(x+1)*(y+1)))
print('Finalizado!')
