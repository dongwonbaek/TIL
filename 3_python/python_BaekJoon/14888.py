import sys
sys.stdin = open('14888.txt')

from itertools import permutations

N = int(input())
numbers = list(map(int, input().split()))
cal = list(map(int, input().split()))
cals = []

for a in range(4):
    for b in range(cal[a]):
        cals.append(a)

cals_result = list(permutations(cals, sum(cal)))

result = []

for i in cals_result:
    num = numbers[0]
    for j in range(len(cals)):
        if i[j] == 0:
            num += numbers[j + 1]
        elif i[j] == 1:
            num -= numbers[j + 1]
        elif i[j] == 2:
            num *= numbers[j + 1]
        elif i[j] == 3:
            if num < 0:
                num = 0 - (abs(num) // numbers[j + 1])
            else:
                num //= numbers[j + 1]
    result.append(num)

print(max(result))
print(min(result))