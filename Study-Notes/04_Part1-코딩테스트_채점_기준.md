# Part1 - 코딩테스트 채점 기준
* 기업 별로 상세 기준은 다 다름
	* 부분 점수가 있을 수도/ 없을 수도
	* 문제마다 배점을 동일하게/다르게
	* 제출 시도 횟수 제한 있기도/없기도
	* 채점 결과 공개/비공개

* 일반적으로
1. 푼 문제가 많을 수록 순위가 높음
2. 같은 문제 수라면 더 적은 시도 횟수 / 더 빨리 맞췄을수록 순위가 높음
3. 절반 이상 풀었을 때 합격권인 경우가 많았음
	* 삼성은 2문제 중 1문제 이상, 카카오는 7문제 중 4문제 정도 이상
	* 문제 난이도와 응시자들 평균 실력에 따라 달라질 수 있음

* 문제마다 존재하는 제한 조건
	* 시간 제한
	* 메모리 제한

## 시간/공간 복잡도 Complexity

### 문제가 ‘어렵다’
* 문제가 어렵다는 것은 무엇인가? 어떤 문제가 어려운 것일까?
-> 푸는데 아무리 오래 걸리는 문제들도 컴퓨터는 빠른 연산으로 풀 수 있다. 

* 컴퓨터 조차도 너무 오래 걸리는 문제가 ‘어려운’ 문제(전산학에서 말하는 어려운 문제)
-> 얼마나 오래 걸려 ? => 시간 복잡도를 통해서 파악

예시 문제
**N이 주어지면 1~N까지의 합을 출력하세요.**
해법1
-> 반복문 돌려서 1부터 N까지 더한 합계를 출력

해법2
-> N(N+1)/2 : 주어진 N 값이 크던 작던 연산 딱 1번 수행(엄밀히는 3번)

해법 1보다 해법 2가 좋은 해법 (N이 아무리 커도 3번의 연산으로 정답 구할 수 있음)

1. 문제를 푸는 솔루션은 꼭 하나만 있으란 법은 없다.
2. 알고리즘에 따라 답을 구하는데 걸리는 시간이 다르다.

## 시간 복잡도
* 알고리즘의 최악의 경우 실행시간
* 입력량 N에 비례해서 얼마만큼 연산을 많이 하는지를 나타냄(앞에서 말한 문제에서)

* 알고리즘의 효율성 척도
* 빅오 표기법 Big-O notaition으로 표기

* 주먹구구식 계산법
	* C++ 기준 1초에 총 연산 1억 번이 넘어가면 위험. 1초= 1억
	* 보통 k중 for문 = O(N^k)

## 빅오 표기법
* 가장 큰 항을 살리고 그보다 작은 항들을 다 뗀다.
* 계수, 상수도 의미 없음. 다 뗀다.
* 가장 크게 증가하는 항만 중요
* N이 무한히 증가한다고 생각해보자.

<img width="758" alt="스크린샷 2022-01-11 오전 10 14 47" src="https://user-images.githubusercontent.com/61059893/152524664-79413d7b-fd01-4543-9211-c887757d47ad.png">
<img width="796" alt="스크린샷 2022-01-11 오전 10 16 21" src="https://user-images.githubusercontent.com/61059893/152524685-377cbaad-0bec-460d-9a98-aa0074133304.png">

* 삼차 시간 알고리즘까지 괜찮게 봄
* 지수 시간 알고리즘은 별로임
* 지수 시간 알고리즘 보다 나쁜건 팩토리얼 알고리즘



## 공간 복잡도 
* N에 비례해서 메모리를 얼마나 쓰는지를 나타냄
* 일반적으로 성립하는 trade-off 관계 : 메모리(공간) <-> 시간
* 메모리를 많이 쓸 수록 시간이 줄고, 메모리를 적게 쓸수록 시간이 오래 걸리는 경향이 있음. 어떤 것을 희생할지 고려해보아야함


## 시간/공간복잡도를 따져보자.
문제 : 시간 제한 2초, 메모리 제한 64MB
입력 : 0 <= N <= 100,000,000

시간 복잡도
O(N)
O(logN)

: O(N^2)은 안됨


공간복잡도
O(N), int 하나에 4Byte이니까  4byte * 10^8 = 400MB -> 메모리 초과
O(루트N)  = 40KB = 0.04MB -> 충분히 가능

::WolframAlpha 에서 계산해보자::

- - - -
문제 : 시간 제한 1초, 메모리 제한 128MB
입력 : -1,000 <=N<=1,000

시간복잡도
* O(N), 1초면 1억 연산 가능, 범위는 2000이니까 가능
* O(N^2), 2000^2 = 400만, 가능

공간복잡도
O(N^2) 일 때, 4Byte * 2000^2 = 16MB, 가능
O(N^3) 은 안됨
