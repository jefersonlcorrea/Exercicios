desafio = 'ex015'
print('{:=^30}'.format(desafio))
dias=int(input('Quandos dias decorreram no aluguel: '))
km=int(input('Quantos Km foram rodados: '))
print('Total a pagar pelo aluguel: R$ {:.2f}'.format((dias*60)+(km*0.15)))
