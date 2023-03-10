import sys
sys.stdin = open('15654.txt')

N, M = map(int, input().split())
list_ = list(map(int, input().split())) 
list_.sort()        # 정해진 수를 활용하여 오름차순으로 정렬해야 한다면, 위에서 수를 입력받아 정렬된 리스트로 구성한다.
answer = [] 

def back():
    if len(answer) == M:
        print(*answer)
        return
    for a in list_: # 기존의 range로 순회하던 것을 정렬된 리스트로 대체하여 똑같이 활용할 수 있다.
        if a not in answer:
            answer.append(a)
            back()
            answer.pop()

back()