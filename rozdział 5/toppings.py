requested_topping = 'pieczarki'
if requested_topping != 'anchois':
    print('Prosze o anchois')




number = 21
if number > 10:
    print('mozesz wejsc')


requested_topping = ['ser', 'szynka', 'pomidory']
if 'ser' in requested_topping:
    print('DODAJE SER')
    if 'pomidory' in requested_topping:
        print('DODAJE POMIDORY')
        if 'olej' in requested_topping:
            print('DODAJE OLEJ')




requested_topping = ['pieczarki', 'anchois', 'ser']

for topping in requested_topping:
    print(f"dodaje {topping}")

print("pizza gotowa")