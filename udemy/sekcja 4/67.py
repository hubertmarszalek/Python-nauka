numbers = [-4,-3,-2,-1,0,1,2,3,4]

for num in numbers:
    if num == 0:
        print("zero jest parzyste")
    elif num % 2 != 0:
        print(f'{num} jest nie parzyste')
    else:
        print(f'{num} jest parzyste')