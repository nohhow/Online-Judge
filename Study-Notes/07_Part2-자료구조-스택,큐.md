# Part2 - 자료구조 - 스택, 큐

## 스택 Stack
<img width="213" alt="스크린샷 2022-02-06 오후 8 49 56" src="https://user-images.githubusercontent.com/61059893/152680647-40c164f3-fce6-4e7e-9044-e53007ed48bd.png">


* 선입 후출 (FILO : First-In Last-Out)
* 후입 선출 (LIFO : Last-In First-Out)

* 삽입/삭제 : O(1) -> N 개의 데이터 각각에 접근할 수 없음, 삽입과 삭제 모두 Head(Top)에 대해서만 가능하다.
<img width="612" alt="스크린샷 2022-02-06 오후 8 52 58" src="https://user-images.githubusercontent.com/61059893/152680650-f2a2175c-200c-4d9f-be13-2280cb46a8ef.png">


* C++ 에서는 Stack Library 호출 후 사용가능
> push() 삽입  
> top() 최상단 데이터  
> pop() 삭제  

* Python 에서는 배열로 구현 가능
> 음수 Index 룰 호출하면  역순으로 값을 불러온다.  

```python
s= []
s.append(123)
s.append(456)
s.append(789)
while len(s) > 0:
	print(s[-1])
	s.pop(-1)
```

여기서 -1 인덱스는 배열의 항상 마지막 항을 가리키게 된다.


### 스택 실생활 예시
* 웹 서핑과정에서 페이지 뒤로가기를 하는 경우
-> 웹 방문기록을 Stack으로 만들고 뒤로가기를 누르면 마지막으로 들어온 값을 제거하면서 이전 페이지를 알 수 있다.

- - - -

## 큐 Queue
<img width="239" alt="스크린샷 2022-02-06 오후 9 08 33" src="https://user-images.githubusercontent.com/61059893/152680654-7a3dd728-7a01-4bf4-bfb6-d83df8d074a0.png">


* 선입 선출 (FIFO : First-In First-Out)
* 후입 후출 (LILO : Last-In Last-Out)
* 삽입/삭제 : O(1)

큐를 구현할 때 배열을 가지고 구성하려고 한다면 삽입/삭제는 O(1)가 아닌 O(N)이 된다. 
왜냐하면 배열에서 맨 앞에 값을 없앤다면 다른 항들의 값을 모두 앞으로 한 칸씩 옮겨야한다. 그렇기 때문에 O(N)이 된다.
-> O(1)이 되는 Queue를 구성하기 위해서는 **연결리스트를 이용**하거나 **배열을 사용하고 front와 rear를 가리키는 포인터를 사용**하는 방법이 있다.

<img width="662" alt="스크린샷 2022-02-06 오후 9 13 41" src="https://user-images.githubusercontent.com/61059893/152680662-3a7d7c02-efd3-4348-bc20-653864c3edbf.png">

### python으로 구현시
`from queue import Queue`
이처럼 import하여 사용할 수 있지만 이는 멀티쓰레드 구현 시에 안정성을 확보할 수 있는 thread-safe가 포함되어있기 때문에 실행속도가 느리다. PS에서는 멀티쓰레드와 관련이 없기에 이를 사용하지 않고
`from collections import deque` 이를 사용한다.
  
deque는 queue의 상위호환이라고 생각하면 좋다.
* 기존의 queue는 맨 뒤에만 넣을 수 있지만 deque는 앞 뒤로 넣을 수 있다.
```python
from collections import deque

dq = deque()
dq.append(123)
dq.appendleft(456)
dq.appendleft(789)

print(dq.pop())
print(dq.popleft())

```

* deque = Double-Ended QUEue
* Thread-safe 기능 외에 Queue의 기능을 모두 포함하고 있기 때문에 PS에서 이를 사용하지 않을 이유가 없다.

### 큐 실생활 예시
* 줄서기
-> 마지막에 줄 선 사람이 마지막에 입장
