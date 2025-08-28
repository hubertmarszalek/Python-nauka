owoce = ['ananas', 'jablko', 'gruszka']
print(owoce)
mes = f"Moim ulubionym owocem jest {owoce[0]} i {owoce[2]}."
print(mes)

owoce[1] = 'truskawka'
print(owoce)

owoce.append('jabłko') #dodaje pojedynczą
print(owoce)

owoce.extend(['jagoda', 'sliwka'])  #dodaje kilka rzeczy
print(owoce)


owoce.insert(3, 'porzeczka')  #wstawiony na 3 pozycje
print(owoce)


del owoce[2]   #usuwa gruszke
print(owoce)

popped_owoce = owoce.pop()
print(owoce)
print(popped_owoce)
mess = f"Kupiłem ostatnio {popped_owoce}"
print(mess)

owoce.remove('porzeczka')
print(owoce)