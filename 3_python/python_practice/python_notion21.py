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
newnumber_list = number_list[::-1]

result = 0
for partnumber in newnumber_list:
    result += int(partnumber) * 10**(n-1)
    n -= 1
    if n-1 < 0:
        break
print(result)