#zamiana C na F
def cToF(celsius):
    fahrenheit = celsius * 9 / 5 + 32
    return fahrenheit

#zamiana F na C
def fToC(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius

ex1 = cToF(20)
print(f"20\xB0 celsius to fahrenheit is: {ex1}\xB0F")

ex2 = fToC(86)
print(f"86\xB0 fahrenheit to celsius is: {ex2}\xB0C")





def convert(value, mode):
    if mode == "f":           # jeśli użytkownik poda "f"
        return fToC(value)    # wywoła funkcję fToC (Fahrenheit → Celsius)
    elif mode == "c":         # jeśli użytkownik poda "c"
        return cToF(value)    # wywoła funkcję cToF (Celsius → Fahrenheit)
    else:                     # jak poda coś innego
        return value          # zwraca bez zmian

ex3 = convert(86, "f")
print(ex3)   # 30.0
