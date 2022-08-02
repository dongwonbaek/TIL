# 시간 복잡도 & 빅오 표기법

좋은 알고리즘이란 무엇일까?

== 효율성이 좋은 알고리즘?

== 성능이 좋은 알고리즘?

== Input을 넣은 후 Output이 나오는 시간이 짧은 알고리즘!

객관적인 측정을 위해 알고리즘 내부에서 기본연산이 몇 번 일어나는지 살펴본다.



1 < logN < N < NlogN < N^2 < N^3 < 2^N < N!



시간 복잡도가 O(1)인 함수들(활용하면 좋다!)

len()

pop()

append()

set()



O(N)인 함수들(사용해도 된다)

count()

index()

reverse()s



O(N^2) (조금 부담스럽지만 사용해도 된다.)

sort()



.find() 와 .index() 의 차이점

- index는 위치를 찾지 못하면 에러를 반환하지만 find는 -1를 반환.



# 스택, 큐(Stack, Queue)



**스택**

stack은 쌓는다는 의미로 가장 마지막에 들어온 데이터가 가장 먼저 나가므로 LIFO(후입선출) 방식



push 

스택에 새로운 데이터를 삽입하는 행위. 파이썬에서는 리스트를 append로 간단하게 구현할 수 있다.



pop

스택의 가장 마지막 데이터를 가져오는 행위. 파이썬에서는 리스트에 pop으로 간단하게 구현할 수 있다.

.pop() 메서드는 마지막 데이터를 삭제한다.



왜 스택을 써야할까?

1. 뒤집기, 되돌리기, 되돌아가기 (브라우저, 방문기록, 워드 ctrl + z)
2. 마무리 되지 않은 일을 임시 저장



- 괄호 매칭: vs코드에서 괄호를 스택을 활용하여 자동으로 매칭해주는 방식

- 함수 호출(재귀 호출)

- 백트래킹

- DFS(깊이 우선 탐색)



**큐**

큐는 한쪽 끝에서 데이터를 넣고, 다른 한 쪽에서만 데이터를 뺼수 있는 자료구조

가장 먼저 들어온 데이터가 가장 먼저 나가므로 FIFO(선입선출) 방식



dequeue

큐의 첫번째 데이터를 가져오는 행위. append()를 활용



enqueue

큐에 마지막에 새로운 데이터를 삽입하는 행위. popleft()를 활용한다.



파이썬에서 큐를 사용하려면 덱(Deque)을 사용하는 것이 좋다.

~~~python
from collections import deque
numbers = [1, 2, 3, 4, 5]
queue = deque(numbers)
queue.append(6)
queue.popleft()
print(queue)
# deque([2, 3, 4, 5, 6])
~~~



# 힙(Heap)



우선순위 큐는 우선순위를 기준으로 가장 우선순위가 높은 데이터가 가장 먼저 나가는 방식

우선순위 큐를 구현하는 방법

1. 배열
2. 연결 리스트
3. 힙



**힙의 특징**

- 최대값 또는 최소값을 빠르게 찾아내도록 만들어진 데이터구조

- 완전 이진 트리의 형태로 느슨한 정렬 상태를 지속적으로 유지한다.

- 힙 트리에서는 중복값을 허용한다.



힙은 언제 사용해야할까?

1. 데이터가 지속적으로 정렬되야 하는 경우 (느슨한 정렬)
2. 데이터에 삽입/삭제가 빈번할 때



파이썬의 heapq 모듈

Minheap(최소 힙)으로 구현되어 있음(가장 작은 값이 먼저 옴) Maxheap도 가능(가장 큰 값이 먼저 옴)

삽입, 삭제, 수정, 조회 연산의 속도가 리스트보다 빠르다.

heapq.heappop()

heapq.heappush()



~~~python
import heapq # 힙 구현

numbers = [5, 3, 2, 4, 1]
heapq.heapify(numbers) # numbers 자체가 바뀌어 버린다. 최솟값을 맨 앞으로 느슨한 정렬
print(numbers)
# [1, 3, 2, 4, 5]

heapq.heappop(numbers) # 첫번째 값을 뽑아내고 또 다시 가장 작은 값을 첫번째로 이동
print(numbers)
# [2, 3, 4, 5]

heapq.heappop(numbers)
print(numbers)
# [3, 4, 5]

heapq.heappush(numbers, 10)
print(numbers)
# [3, 5, 6, 10]

heapq.heappush(numbers, 0) # 가장 최솟값을 넣는 순간 정렬하여 맨앞으로 이동한다.
print(numbers)
# [0, 3, 5, 6, 10]
~~~