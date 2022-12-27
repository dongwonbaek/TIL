import sys
sys.stdin = open('1032.txt')

N = int(input())
words = []
result = ''
for _ in range(N):
    words.append(input())

for a in range(len(words[0])):
    switch = True
    sample = words[0][a]
    for word in words:
        if sample != word[a]:
            switch = False
            result += '?'
            break        
    if switch == True:
        result += sample
print(result)