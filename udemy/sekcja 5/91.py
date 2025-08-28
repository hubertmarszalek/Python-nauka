def calculateBMI(waga,wzrost):
    bmi = waga / ((wzrost/100)**2)
    return bmi

def classifyBMI(bmi):
    if bmi < 18.5:
        return "niedowaga"
    elif  bmi < 25:
        return "normalny"
    elif bmi < 30:
        return "nadwaga"
    else:
        return "masz sporą nadwage"


waga1 = float(input("waga: "))
wzrost1 = float(input("wzrost: "))
bmi1 = calculateBMI(waga1,wzrost1)
classify = classifyBMI(bmi1)
print(f"{classify}, {bmi1:.2f}")


