string = "Hello"


def showInfo():
    print(3, string) # Uwaga, odwołanie do zmiennej globalnej!: 3, Hello


def printData():
    string = "Test" # zmienna lokalna przesłania globalną
    print(2, string) # 2, Test
    showInfo() # wywołanie funkcji showInfo()


print(1, string) # Hello
printData()




print(" ")




firstNum = 10

def test():
    firstNum = 2
    print("test() firstNum:", firstNum)
    def bar():
        print("bar() firstNum:", firstNum)
    bar()
    print("end test()")

print("global firstNum:", firstNum)
test()



print(" ")



number = 20

def printNumber():
    # nie modyfikujemy globalnej tylko
    # tworzymy lokalna zmienna
    number = 2  # nie zmienia globalnej
    print("doNumber():", number)

printNumber()
print("global number ", number)






print("\nzmiana globalnej wewnatrz funkcji")
number_a = 20

def printNumber():
    global number_a
    number_a = 15

    print("doNumber():", number_a)

printNumber()
print("global number ", number_a)




print("\ninstrukcja if ")




string = "Hello"

if 1 == 1:
    print(1, string)
    if 2 == 2:
        string = "Hejka"
        print(2, string)
        if 3 == 3:
            print(3, string)

print(4, string)



print("\ninstrukcja if z funkcja")

string = "Hello"


def testFunc():
    string = "LocalHi"
    if 1 == 1:
        print(1, string)
        if 2 == 2:
            string = "Hejka"
            print(2, string)
            if 3 == 3:
                print(3, string)
    print(4, string)

testFunc()
print(5, string)








