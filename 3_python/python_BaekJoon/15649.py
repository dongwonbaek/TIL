import sys
sys.stdin = open('15649.txt')

N, M = map(int, input().split())
answer = []
def back():                     # 재귀함수 활용(백트래킹)
    if len(answer) == M:        # answer 리스트가 최대 길이가 되면 
        print(*answer)          # 리스트의 인스턴스들을 한 칸 간격으로 출력하고
        return                  # 함수 종료
    for a in range(1, N + 1):   # 최대 길이가 아니라면 1부터 N까지의 수들을 순회하면서
        if a not in answer:     # answer 리스트 내에 중복되지 않았다면
            answer.append(a)    # 리스트에 추가하고
            back()              # 함수 재실행
            answer.pop()        # 함수가 종료되면 제일 뒤 인스턴스를 제거하고 중복되지 않은 다른 수를 찾아 순회
                                # 함수 종료 시 상위 함수에서 이어서 순회를 진행하여 중복되지 않는 다른 리스트를 생성함

back()