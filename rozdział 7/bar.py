sandwitch_orders = ['tunczyk', 'pomidor', 'pasztet', 'cebula', 'cebula']

finished_sandwitch = []

while 'cebula' in sandwitch_orders:
    sandwitch_orders.remove('cebula')
    print("Skonczyła sie cebula, przepraszamy")


while sandwitch_orders:
    sandwitch_order = sandwitch_orders.pop()
    print(f"{sandwitch_order} w przygotowaniu")

    finished_sandwitch.append(sandwitch_order)

print("\nZrobiono wszytskie kanapki")
for sandwitch in finished_sandwitch:
    print(f"{sandwitch} gotowa do odbioru")