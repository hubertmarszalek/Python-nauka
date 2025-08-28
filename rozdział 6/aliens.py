aliens = []
for alien_number in range(30):
    new_alien = {'color':'green','points':5, 'speed':'slow'}
    aliens.append(new_alien)

for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['points'] = 10
        alien['speed'] = 'slow'
        alien['color'] = 'yellow'

for alien in aliens[6:9]:
    if alien['color'] == 'green':
        alien['points'] = 20
        alien['speed'] = 'fast'
        alien['color'] = 'red'

for alien in aliens[:10]:
    print(alien)
print("...")
print(f"calkowita liczba obcych {len(aliens)}")