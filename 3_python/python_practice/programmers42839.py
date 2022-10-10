# 프로그래머스 코딩테스트연습 고득점 kit의 완전탐색 소수찾기 문제.
from itertools import *
def solution(numbers):
    cnt = 0                                 # 소수를 카운트 하기 위한 변수
    answer = []                             # 중복을 걸러내기 위한 빈 리스트
    for a in range(1, len(numbers) + 1):    # 모든 경우의 수를 추출하기 위해 몇 개를 뽑아낼 지 정하는 for문 작성
        result = permutations(numbers, a)   # permutations 메서드를 활용하여 a에 할당된 숫자만큼 모든 경우의 수를 추출하여 튜플형태로 result 리스트에 할당
        for b in result:                    # result 에서 튜플을 한개씩 뽑아내어 
            sample = ''                     
            for c in b:
                sample += c                 # 튜플 내 요소들을 모두 합쳐
            answer.append(int(sample))      # 중복을 걸러내기 위해 answer 리스트에 추가.
    set_answer = list(set(answer))          # 중복제거 후 리스트화 이 때 리스트는 입력된 문자열로 만들 수 있는 모든 경우가 들어가있다.
    for int_sample in set_answer:           # 중복이 제거된 리스트에서 하나씩 순회
        switch = True                       # 소수임을 판별하는 스위치 생성
        if int_sample > 2:                  # 하나씩 순회하면서 2보다 크면, 
            for d in range(2, int_sample):  # 소수인지 판별하기 위해 2부터 자기 자신 전 숫자까지 순회하면서 나머지를 구한다.
                if int_sample % d == 0:     # 나머지가 0이면 약수가 있다는 뜻이므로 소수가 아니다.
                    switch = False          # 소수가 아니면, 스위치를 거짓으로 바꾸고
                    break                   # 반복문을 강제 종료한다.
            if switch == True:              # 만약 스위치가 참으로 유지된 채 반복문이 종료되었다면, 약수가 없다는 뜻이고, 이는 소수라는 뜻이므로,
                cnt += 1                    # 카운트에 추가한다.
    if '2' in numbers:                      # 2는 소수이지만 제외하고 소수를 찾았기 때문에 입력문자열에 2가 있었다면, 카운트를 하나 추가해준다.
        cnt += 1
    return(cnt)