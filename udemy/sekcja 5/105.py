names = ['ania', 'ola', 'kasia']

join = map(lambda x: x + " kowalska", names)
join = list(join)
print(join)

#zwraca powyzej 12
result = filter(lambda x: len(x) > 12, join)
print(list(result))