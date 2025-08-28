

def sumListElements(listdata):
    if len(listdata) == 0:
        print("pusta lista")
        return None
    result = 0
    for item in listdata:
        result += item
    return result

print(sumListElements([1, 2, 3]))
print(sumListElements([]))




lista = [1, 2, 3, 4, 5]
result = 0
for item in lista:
    result += item
    print("Dodaję:", item, " -> result =", result)

print("Ostateczny wynik:", result)
