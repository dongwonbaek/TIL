a = int(input())
n = 0

while True:
    if a // (10**n) != 0:
        n += 1
    else:
        break

number_list = []
for b in range(n-1,-1,-1):
    number_list.append(a // 10**(b))
    a -= (a//10**(b)) * 10**(b)
    if b == 0:
        break
print(sum(number_list))