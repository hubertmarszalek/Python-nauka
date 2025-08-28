# kalkulator sredniej arytmetycznej

from functools import reduce

numbers = [1,3,7,20,42,122,3]


result = map(lambda x: x*2, numbers)
print(list(result))

#suma wszytskich liczb
numbers_sum = reduce(lambda x, y: x + y, numbers)
print(f"suma wszytskich liczb to: {numbers_sum}")

#srednia
avg = numbers_sum/len(numbers)
print(f"srednia to: {avg:.2f}")