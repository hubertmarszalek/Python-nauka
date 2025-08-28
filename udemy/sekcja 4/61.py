number = 5

while number > 0:
    print(number)
    number -= 1

number = 1

while number < 6:
    print(number)
    number += 1




num = 0
while True:
    print("wprowadz liczbe lub exit")
    strData = input()
    if strData == "exit":
        break
    num += int(strData)
    print("wart po dodaniu liczby" + str(num))





i = 0
sum = 0

while i <= 100:
    sum += i
    i += 1
    print(i)
else:
    print(sum)


































