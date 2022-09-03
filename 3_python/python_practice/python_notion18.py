word = input()
a = list(set(word))
e = list()
d = 0

while d < len(a):
    count = 0
    c = a[d]
    for b in word:
        if b == c:
            count += 1
    d += 1
    e.append(count)

h = dict()
for g in range(len(a)):
    h[a[int(g)]] = e[int(g)]

for words in h:
    print(words, h[words])