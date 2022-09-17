import sys
sys.stdin = open('2605.txt')

N = int(input())
student = list(map(int, input().split()))
result = [1]
for a in range(1, N):
   result.insert(len(result) - student[a], a + 1)
print(*result)