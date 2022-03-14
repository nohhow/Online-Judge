import sys
import heapq

N = int(sys.stdin.readline())

hq = []      
result = []  

for _ in range(1 ,N+1):
    x = int(sys.stdin.readline())
    if x == 0:
        if len(hq)==0:
            result.append(0)
        else:
            result.append(heapq.heappop(hq)[1])
    else:
        heapq.heappush(hq, (abs(x),x))


for i in result:
    print(i)
            
        
        
