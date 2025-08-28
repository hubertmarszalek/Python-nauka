n = int(input("podaj n: "))

nieparzyste_liczby = []
parzyste_liczby = []
liczby=[]

for i in range(1,n+1):
    if i % 2 == 0:
        parzyste_liczby.append(i)
    if i % 2 != 0:
        nieparzyste_liczby.append(i)

liczby = parzyste_liczby + nieparzyste_liczby
liczby = sorted(liczby)
print(liczby)
print(f'niepartzyste to: {nieparzyste_liczby}')
print(f'partzyste to: {parzyste_liczby}')
