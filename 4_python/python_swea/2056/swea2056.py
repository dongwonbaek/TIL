import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    a = input()
    
    if a[4:6] in ['01','03','05','07','08','10','12']:
        if int(a[6:8]) >= 1 and int(a[6:8]) <= 31:
            print(f'#{test_case} {a[0:4]}/{a[4:6]}/{a[6:8]}')
        else:
            print(f'#{test_case} -1')
    elif a[4:6] in ['04','06','09','11']:
        if int(a[6:8]) >= 1 and int(a[6:8]) <= 30:
            print(f'#{test_case} {a[0:4]}/{a[4:6]}/{a[6:8]}')
        else:
            print(f'#{test_case} -1')
    
    elif a[4:6] in ['02']:
        if int(a[6:8]) >= 1 and int(a[6:8]) <= 28:
            print(f'#{test_case} {a[0:4]}/{a[4:6]}/{a[6:8]}')
        else:
            print(f'#{test_case} -1')

    else:
        print(f'#{test_case} -1')