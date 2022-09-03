word = input()
모음 = ['a', 'e', 'i', 'o', 'u']
count = 0
for a in word:
    for b in 모음:
        if a == b:
            count += 1
print(count)
