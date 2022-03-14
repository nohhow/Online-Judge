import sys
import heapq as hq

input = sys.stdin.readline

min_heap = [] #양수
max_heap = [] #음수

for _ in range(int(input())):
  x = int(input())
  if x:
    if x > 0:
      hq.heappush(min_heap, x)
    else:
      hq.heappush(max_heap, -x) # max_heap으로 구현하고자 부호를 반전 시키고 꺼낼때도 부호 반전
  else:
    if min_heap:
      if max_heap:
        if min_heap[0] < abs(-max_heap[0]):
          print(hq.heappop(min_heap))
        else:
          print(-hq.heappop(max_heap))
      else:
        print(hq.heappop(min_heap))
    else:
      if max_heap:
        print(-hq.heappop(max_heap))
      else:
        print(0)
