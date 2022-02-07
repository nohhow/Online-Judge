# Part2-자료구조-우선순위_큐

## 우선순위 큐 Priority Queue (Heap)
* 이진트리 형태의 Heap이라는 자료 구조로 구성됨.
* Root Node에 가장 큰 값이 위치한 경우 : Max Heap
* Root Node에 가장 작은 값이 위치한 경우 : Min Heap
* 삽입 / 삭제 : O(log2N) -> 보통은 2를 생략하고 O(logN)이라고 표기함.

  

![](08_Part2-%E1%84%8C%E1%85%A1%E1%84%85%E1%85%AD%E1%84%80%E1%85%AE%E1%84%8C%E1%85%A9-%E1%84%8B%E1%85%AE%E1%84%89%E1%85%A5%E1%86%AB%E1%84%89%E1%85%AE%E1%86%AB%E1%84%8B%E1%85%B1_%E1%84%8F%E1%85%B2/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202022-02-07%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%2010.01.22.png)


### C++에서의 우선순위 큐

##### C++ 은 max-heap을 지원
Max Heap 은 가장 처음 pop() 했을 때 가장 큰 값이 빠져나오는 것이 보장됨.

### Python에서의 우선순위 큐 

##### Python 은 min-heap 지원
Min Heap 은 가장 처음 pop() 했을 때 가장 작은 값이 빠져나오는 것이 보장됨.

#### PriorityQueue Library를 사용하는 경우
이 경우는 Queue와 마찬가지로 thread-safe를 지원하기 때문에 속도 측면에서 사용하기 어렵다.
(그래서 Queue대신 deque를 사용했었다. 우선순위 큐의 경우는 heapq를 사용한다.)

```python
from  queue import PriorityQueue

pq = PriorityQueue()
pq.put(6)
pq.put(10)
pq.put(-5)
pq.put(0)
pq.put(8)
while not pq.empty():
	print(pq.get()) #pop 
```

**결과**
-5
0
6
8
10

#### heapq를 사용하는 경우 (시간초과 방지)
사용법이 조금 특이하기 때문에 익숙해질 필요가 있다.
* heapq 모듈이 heappush, heappop 메서드를 실행할 때마다 자동적으로 리스트의 Index 0 에 항상 최상단 노드가 위치하도록 정렬해줌.

```python
import heapq

pq = []
heapq.heappush(pq, 6)
heapq.heappush(pq, 12)
heapq.heappush(pq, 0)
heapq.heappush(pq, -5)
heapq.heappush(pq, 8)
print(pq)
while pq:
	print(pq[0])
	heapq.heappop(pq)

```


Notice
> C++의 pop은 단순히 값을 빼내는 기능만하고 값을 반환하지 않는다.  
> Python에서는 반환값이 있기 떄문에 print 해주기만 하면 된다.  
