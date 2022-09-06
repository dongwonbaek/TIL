import sys
sys.stdin = open('2116.txt')

dice = {
    '0' : '5',
    '1' : '3',
    '2' : '4',
    '3' : '1',
    '4' : '2',
    '5' : '0'
}

# A : BCDE / B : ACEF / 
T = int(input())
result = []
answer = []
for _ in range(T):
    dice_sam = list(map(int, input().split()))
    result.append(dice_sam)
for a in range(6):
    max_ = 0
    for b in range(T):
        biggest = 0
        for c in range(6):
            if c != a and c!= int(dice[str(a)]) and result[b][c] > biggest:
                biggest = result[b][c]
        if b + 1 < T:
            a = result[b + 1].index(result[b][int(dice[str(a)])])
        max_ += biggest
    answer.append(max_)
print(max(answer))