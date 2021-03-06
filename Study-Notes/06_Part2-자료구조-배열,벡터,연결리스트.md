# Part2 - 자료구조 - 배열, 벡터, 연결리스트

## 배열 Array
* 삽입/삭제 : O(N)
* 탐색: O(1)
* C++에서는 size 변경 불가
* Python은 리스트를 사용
<img width="372" alt="스크린샷 2022-02-04 오후 7 37 29" src="https://user-images.githubusercontent.com/61059893/152524823-b70aee9c-0481-4f1b-8666-d774fff36738.png">


![IMG_0251](https://user-images.githubusercontent.com/61059893/152524834-92738efe-61ac-4030-a648-8ab0b8a0b6fd.jpeg)

탐색 : O(1)
-> 메모리상에 연속적으로 공간이 할당되어있고, 이 때문에 임의 접근이 가능하다. = 탐색 속도가 빠르다.

![IMG_0250](https://user-images.githubusercontent.com/61059893/152524867-bb4d2536-0062-46be-ba1f-6095e4cdd547.jpeg)

삽입/삭제 : O(N)
-> 삽입/삭제 시에 빈 공간을 만들거나 채우기 위해서 동작해야하는 횟수가 최악의 경우 N번이다.

> 탐색 유리  
> 삽입/삭제 불리  

- - - -

## 벡터 Vector
벡터는 C++ 에 있는 (STL : Standard Template Library)

* 삽입/삭제 : O(N)
* 탐색: O(1)
* 동적 배열 (size 변경 가능)


- - - -

## 연결 리스트 Linked List
C++에서는 기본 STL로 제공하고 있음.
Python에서는 기본적으로 제공하고 있지 않기 때문에 직접 작성해서 사용해야함.

* 삽입/삭제 : O(1)
* 탐색 : O(N)
* PS에서는 별로 안쓰이지만 다른 자료구조들을 구현할 때 많이 쓰인다. -> 연결 리스트로 풀 수 있는 문제는 다른 것들로 풀이 가능한 경우가 많다. 다만 다른 자료구조들을 구현할 때 연결 리스트가 사용된다.
* 배열과 특성이 상반되는 것을 볼 수 있다. -> 면접 단골 문제임


* 배열은 메모리 상에 연속적인 공간에 할당되어있었지만 연결 리스트는 그렇지 않다.
* 노드가 여러 개 존재하는데, 노드 간에 위치는 가까울 수도 멀 수도 있다.

![IMG_0253](https://user-images.githubusercontent.com/61059893/152524897-62a5014c-6ca4-4b6f-92f3-2750378c9322.jpeg)

탐색 : O(N)
-> 메모리 상에 연속적으로 위치하고 있지 않기 때문에 임의 접근이 불가능하다. 따라서 모든 노드를 선회해야하고 이는 최악의 경우 N회 실행하게 된다.

![IMG_0252](https://user-images.githubusercontent.com/61059893/152524985-d588808e-23cf-4bb7-945e-2aa5a6a5b703.jpeg)

삽입/삭제 : O(1)
-> 노드들이 연속적으로 위치하고 있지 않기 때문에 삽입하려는 위치의 앞 뒤 노드와의 관계만 맺어주면 삽입이 가능하다. 마찬가지로 삭제도 해당 노드를 삭제하고 앞 뒤 노드의 관계를 맺어주면 된다.



