import sys
import heapq

N = int(sys.stdin.readline())

hq = []      
result = []  

for _ in range(1 ,N+1):
    x = int(sys.stdin.readline())
    if x :
        heapq.heappush(hq, (abs(x), x))
    else:
        print(heapq.heappop(hq)[1] if hq else 0)
