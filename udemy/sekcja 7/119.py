population = (38, 83, 60, 46, 120)

population += (130,)

print("Ilość elementów:", len(population))
print("Czy jest kraj o populacji 100 mln:", 100 in population)
print("Kraj trzeci w kolejnośći:", population[2])

min = min(population)
max = max(population)
print("Min:", min)
print("Max:", max)

if max > 500:
    print("Jest kraj z 500 mln ludności")
else:
    print("Wszystkie kraje nie mają więcej niż 500 mln")
