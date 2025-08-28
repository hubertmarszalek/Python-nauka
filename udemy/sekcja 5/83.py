def FindLargest(num1, num2):
    if num1 > num2:
        print(f"{num1} jest większe niż: {num2}")
        return
    elif num1 < num2:
        print(f"{num1} jest mniejsza niz: {num2}")
        return
    else:
        print("są rowne")
        return

numbers1 = FindLargest(7,5)

print(numbers1)


def find_largest(num1, num2):
    if num1 > num2:
        return num1
    elif num2 > num1:
        return num2
    else:
        return None  # gdy równe

print(find_largest(7, 5))  # 7
print(find_largest(3, 9))  # 9
print(find_largest(4, 4))  # None




def find_largest(num1, num2):
    if num1 > num2:
        return f"{num1} jest większe niż {num2}"
    elif num1 < num2:
        return f"{num1} jest mniejsze niż {num2}"
    else:
        return "Są równe"

numbers1 = find_largest(7, 5)
print(numbers1)  # 7 jest większe niż 5

