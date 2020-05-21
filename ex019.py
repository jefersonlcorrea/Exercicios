desafio = 'ex018'
print('{:=^30}'.format(desafio))
import random
nomes = []
for x in range(4):
    entrada = str(input('Digite quatro nomes: {} nome ->'.format(x+1)))
    nomes.append(entrada)
print('O Nome Sorteado foi {}!'.format(nomes[random.randint(0,3)]))