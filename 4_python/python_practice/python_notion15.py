word = input()
index_a = 0
for a in word:
    if a != 'a':
        index_a += 1
    else: 
        print(index_a)
        break
else:
    print(-1)