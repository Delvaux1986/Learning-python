toys = {'Laser sword' : 229.0 , 'Mitendo DX' : 127.30, 'Linux cushion' : 74.50, 'Goldorak' : 29.90 , 'Nexxpresso station' : 184.60}

price = sum(toys.values())

print(price)

print('maintenant on va delete un elem du dictionnaire et recalculer')

del toys['Goldorak']

newPrice = sum(toys.values())

print('new Price = ', newPrice)