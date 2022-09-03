number = int(input())
n = 0
while 1 == 1:
    if number >= 10**n and number < 10**(n+1):
        print(n+1)
        break
    else:
        n += 1
