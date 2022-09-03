import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    number_list = []
    a = int(input())
    n = 1             # 입력 값에 곱해지는 값
    sheep = a * n      

    while number_list != list(range(10)):       # 넘버리스트와 [0,1,2,3,4,5,6,7,8,9]가 같지 않으면 무한 반복
        
        for b in range(len(str(sheep))):        # sheep을 문자열로 바꾼 값의 길이, 즉 자릿수만큼만 반복하도록 요청
            if sheep % 10 not in number_list:   # 만약 sheep을 10으로 나눈 나머지가 넘버리스트에 포함되어 있지 않다면,
                number_list.append(sheep % 10)  # 그 나머지 값을 넘버리스트에 추가하고,
                sheep //= 10                    # sheep변수에 기존 sheep을 10으로 나눈 몫을 대입한다.
            else:                               # 하지만, 넘버리스트와 [0,1,2,3,4,5,6,7,8,9]이 같다면  
                sheep //= 10                    # sheep변수에 기존 sheep을 10으로 나누 몫을 대입하기만 한다.

        number_list.sort()                      # 그 후 정렬메소드를 통해 range(10)와 순서까지 비교할 수 있도록 조정한다.

        if number_list != list(range(10)):      # 만약 넘버리스트와 [0,1,2,3,4,5,6,7,8,9]가 같다면,
            n += 1                              # 곱해지는 값에 1을 추가하고,
            sheep = a * n                       # sheep을 재할당함으로써 위for문에서 변형된 sheep을 다시 시작값으로 맞춰준다. 
        else:                                   # 하지만, 넘버리스트와 [0,1,2,3,4,5,6,7,8,9]이 같다면 
            print(f'#{test_case} {a * n}')      # 완성된 것이므로 결과값을 출력하고
            break                               # 반복문을 종료시킨다.