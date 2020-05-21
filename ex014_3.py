desafio = 'ex014_3'
print('{:=^30}'.format(desafio))
fahrenheit = float(input('Digite a temperatura em Fahrenheit ( F° ): '))
print('A temperatura em Kelvin é:{:.2f}'.format((fahrenheit-32)*5/9+273,15))