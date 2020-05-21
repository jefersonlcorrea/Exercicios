desafio = 'ex017'
print('{:=^30}'.format(desafio))
from math import hypot
catetoadj = float(input('Cateto Adjacente: '))
catetoop = float(input('Cateto Oposto: '))
print('Hipotenusa: {:.2f}'.format(hypot(catetoadj,catetoop)))
