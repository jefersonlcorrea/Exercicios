desafio = 'ex008'
print('{:=^30}'.format(desafio))
metros = float(input('Digite um valor em metros: '))
print('Corresponte a: \n-->Metros: {:.2f}\n-->Centímetros: {:.0f}\n-->Milímetros: {:.0f}\n-->Kilometros: {:.3f}'
      .format(metros, metros*100, metros*1000, metros/1000))
