raining = True
haveUmbrella =True
temp = 9

if temp >= 40 or temp <= 0:
    print("Zostań w domu")
elif temp > 0 and temp <= 10 and haveUmbrella == True and raining == True:
    print("mozesz wyjsc z parasolka")
elif raining == False and temp >= 10:
    print("mozesz wyjsc bez parasolki")
else:
    print("Zostan w domu")