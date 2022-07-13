word = input()
result = 0

for a in word:
    result += 1
    
b = range(result)
e = list()

for d in b:
    b = range(result)
    c = b[0]
    for d in b:
        if c < d:
            c = d
    e.append(d)
    result -= 1

g = ''

for f in e:
    g += word[f]

print(g)