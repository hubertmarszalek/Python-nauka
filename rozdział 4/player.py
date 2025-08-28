players = ['adam', 'jola', 'marian', 'lena', 'karol']
print(players[1:3])   #wypisuje po indeksach
print(players[2:])  #od 2 pkt (0 , 1, 2)
print(players[-2:])  #2 od tyłu
print(players[:-1])  #odejmuje z końca


print("Oto 3 pierwszych graczow z druzyny")
for player in players[:3]:
    print(player.title())