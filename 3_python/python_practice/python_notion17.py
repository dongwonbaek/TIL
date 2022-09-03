word = input()
b = ''
for a in word:
    if ord(a) >= 97 and ord(a) <= 122:
        b += chr(ord(a)-32)
    else:
        b += a
print(b)