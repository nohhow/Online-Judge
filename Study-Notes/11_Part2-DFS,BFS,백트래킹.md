# Part2-DFS,BFS,백트래킹
## DFS Depth First Search : 깊이 우선 탐색
* 스택이나 재귀를 사용해서 구현
* 완전탐색 알고리즘으로, 모든 노드를 순회함, 단 순서가 중요함.
 
그래프나 트리가 주어졌을 때, DFS를 사용한다고 하면, ROOT에서부터 출발함


adjacent : 인접한
인접 행렬 만들 때 주로 adj = []  사용

이중 배열 만들기
`adj = [[0]*13 for _ in range(13)]`

### Python 으로 DFS 구현
```python
adj = [[0]*13 for _ in range(13)]
adj[0][1] = adj[0][2] = 1
#...
#간선에 대해서 값 1로 변경하는 부분 일부 생략

def dfs(now): #현재 방문하는 노드를 인자로 받음
	for nxt in range(13): #nxt 다음 방문하려는 노드 번호
		if adj[now][nxt]:
			dfs(nxt)

dfs(0)
```


## BFS Breadth First Search : 너비 우선 탐색

* 큐를 사용해서 구현
* 완전탐색 알고리즘으로, 모든 노드를 순회한다. DFS와 탐색 순서가 다름

### Python으로 BFS 구현

```python
from collections import deque

adj = [[0]*13 for _ in range(13)]
adj[0][1] = adj[0][2] = 1
#...
#간선에 대해서 값 1로 변경하는 부분 일부 생략

def bfs():
	dq = deque()
	dq.append(0)
	while dq:
		now = dq.popleft()
		for nxt in range(13):
			if adj[now][nxt]:
				dq.append(nxt)

bfs()

```



## DFS & BFS

### 공통점
* 둘 다 그래프 탐색 알고리즘이다.
* 완전 탐색 알고리즘이다.
	* 모든 경우의 수를 살피기에 반드시 답을 찾을 수 있다.
	* 느리다

### 차이점
* BFS(너비우선) 은 최단 거리 보장이 가능 : **최단 거리 탐색에 사용**
	* 거리 1로 갈 수 있는 곳 다 가보고, 거리 2로 갈 수 있는 곳 다 가보고 이런식이라 가능
* DFS(깊이우선) 은 최단 거리 보장 불가능

### 인접행렬 vs 인접리스트
* 인접행렬 : O(V^2)
* 인접리스트 : O(V + E) = O(max(V, E)) 
	* 간선 개수가 적으면 O(V)가 되기 때문에 인접행렬보다 빠름
	* 간선이 최대로 크면 O(V + V^2) -> O(V^2)으로 인접행렬과 같다고 볼 수 있음

- - - -

## 예제 - 길찾기 문제
* 보통 : 위, 아래, 왼쪽, 오른쪽으로 이동가능  4방향
* **방향값을 미리 코드에 짜두고 for문으로 순회하는 기법을 반드시 익혀야함**

* 방문체크 필요
* 각 칸이 노드
* 상하좌우 4방향의 간선

```python
dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)
chk = [[False] * 100 for _ in range(100)]
N = int(input())

def is_valid_coord(y,x):
	return 0 <= y < N and 0 <= x < N

def bfs(start_y, start_x):
	q = deque()
	q.append((start_y, start_x))
	while len(q) > 0:
		y, x = q.popleft()
		chk[y][x] = True
		for k in range(4):
			ny = y + dy[k]
			nx = x + dx[k]
			if is_valid_coord(ny, nx) and not chk[ny][nx]:
				q.append((ny, nx))

```

- - - -

## 백트래킹 Backtracking 퇴각검색
* 기본적으로 **모든 경우를 탐색**하며 DFS/BFS와 방식은 유사하다.
* 백트래킹은 **가지치기**를 통해 탐색 경우의 수를 줄인다는 차이가 있다.
	* 최악의 경우, 모든 경우를 다 살펴보게 될 수도 있지만 가능한 덜 보겠다는 전략
	* 가망이 없으면 가지 않는다.
