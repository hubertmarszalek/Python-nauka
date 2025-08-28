from string import digits

#for numbers in range (1,1000000):
#    print(numbers)
#
#
#print(max(range(1,1000000)))



#for numbers in range(1,20,2):
 #   print(numbers)

squares = []
for value in range(3,30):
    square = value ** 3
    squares.append(square)

print(squares)


squares2 = [value ** 3 for value in range(3,30)]
print(squares2)