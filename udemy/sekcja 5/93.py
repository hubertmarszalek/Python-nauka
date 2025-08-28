
def analitics_temp(temperatures):
    print(max(temperatures))
    print(min(temperatures))
    print(sum(temperatures)/len(temperatures))


temperatures = []

while True:
    one_temp = (input("wprowadz temperature lub napisz koniec: "))
    if one_temp == "koniec":
        analitics_temp(temperatures)
        break

    one_temp = float(one_temp)
    temperatures.append(one_temp)

