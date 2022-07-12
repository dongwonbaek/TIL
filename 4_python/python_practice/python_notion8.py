numbers = [0, 20, 100]
a = numbers[0]
for b in numbers:
    if a < b:
        a = b

numberlist = list()
for b in numbers:
    if b < a:
        numberlist.append(b) 

c = numberlist[0]
for d in numberlist:
    if d > c:
        c = d
print(c)