def calculateFinalPrice(price, discount):
    finalPrice = price * ((100-discount)/100)
    return finalPrice


cena = float(input("ile to kosztuje: "))
rabat = float(input("ile % rabatu: "))
finalPrice = calculateFinalPrice(cena, rabat)
print(finalPrice)