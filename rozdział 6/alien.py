alien_0 = {'color':'green','points':5}

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

alien_1 ={}
alien_1['color'] = 'yellow'
alien_1['points'] = 25
print(alien_1)


alien_2 = {'color':'green','points':5, 'speed':'srednio', 'x_position':25, 'y_position':0}
print(alien_2)
print(f"Poczatkowa wartosc x-position to {alien_2['x_position']}")
if alien_2['speed'] == 'wolno':
    x_increment = 1
elif alien_2['speed'] == 'srednio':
    x_increment = 2
else:
    x_increment = 3

alien_2['x_position'] = alien_2['x_position'] + x_increment
print(f"Nowa pozycja obcefo to: {alien_2['x_position']}")

del alien_2['color']
print(alien_2)