data = [0,1,2,3,4,5,6]

for v in data:
    if v  == 4:
        break
    print(v*2)


for v in data:
    if v == 2 or v == 4:
        continue
    print(v)

