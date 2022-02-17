# Part2-자료구조-맵,집합
## 맵 Map (Dictionary)

* Key, Value 
* 삽입 / 삭제
	* C++ : O(logN)
	* Python : O(1)

### C++과 Python의 시간복잡도의 차이가 발생하는 이유

C++은 red-black tree
python 은 hash
  
* 트리 구조의 경우는 O(logN) 인 경우가 많다.
O(1)보다 O(logN)이 느린 것은 맞지만 크게 느린 것은 아니다.

* hash의 경우 해시 함수가 각 키마다 해시 함수를 통해서 해시테이블에 배정되는 형태라고 생각하면 된다.

### Python으로 구현시
```python
m = {}
m["Yoondy"] = 40
m["Sky"] = 100
m["Mos"] = 50
print("size:", len(m))
for k in m:
print(k, m[k])
```
- - - -

## 집합 Set

* 중복 X
* 삽입 / 삭제 
	* C++ : O(logN)
	* Python : O(1)

### Python으로 구현시
```python
s = set()
s.add(10)
s.add(10)
s.add(50)
s.add(10)
s.add(70)
print("size:", len(s))
for i in s :
	print(i)
```

**결과**
size : 3
10
50
70

-> 중복이 허용되지 않은 결과를 확인할 수 있다.
