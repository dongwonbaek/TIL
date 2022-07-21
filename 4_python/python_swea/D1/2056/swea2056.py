import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    a = input()
    year = a[0:4]
    month = a[4:6]
    day = a[6:8]
    date = (f'#{test_case} {year}/{month}/{day}')

    if month in ['01','03','05','07','08','10','12']:
        if int(day) >= 1 and int(day) <= 31:
            print(date)
        else:
            print(f'#{test_case} -1')
    elif month in ['04','06','09','11']:
        if int(day) >= 1 and int(day) <= 30:
            print(date)
        else:
            print(f'#{test_case} -1')
    
    elif month in ['02']:
        if int(day) >= 1 and int(day) <= 28:
            print(date)
        else:
            print(f'#{test_case} -1')

    else:
        print(f'#{test_case} -1')