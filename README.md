# Data Structure and Algorithm python
Data Structure and Algorithm study to use Python

## Class 1
### 알고리즘이란 (Algorithm) 이란?

사전적 정의 : 어떤 문제를 해결하기 위한 절차, 방법, 명령어들의 집합

프로그래밍에서의 정의 : 주어진 문제의 해결을 위한 자료구조와 연산 방법에 대한 선택

해결하고자 하는 문제에 따라(응용 종류와 범위에 따라) 최적의 해법은 서로 다르다 ⇒ 이 선택을 어덯게 해야 하느냐를 알기 위해 자료구조를 이해해야 함

## Class 2
### 선형 배열 (Linear Array)
배열 : 원소들을 순서대로 늘어놓은 것
리스트 길이과 관계 없이 빠르게 실행 결과를 보게되는 연산들

- 원소 덧붙이기 `.append()`
- 원소 하나를 꺼내기 `.pop()`

리스트의 길이에 비례해서 실행 시간이 걸리는 연산들

- 원소 삽입하기 `.insert()`
- 원소 삭제하기 `.del()`

추가 다른 연산

- 원소 탐색하기: `.index()`

## Class 3
### 배열 더 알아보기 : 정렬과 탐색(Sorting & Searching)
(1) sorted()

- 내장 함수(built-in function)
- 정렬된 새로운 리스트를 얻어냄

(2) sort()

- 리스트의 메서드(method)
- 해당 리스트를 정렬함

정렬의 순서를 반대로

reverse=True

정렬 : 문자열로 이루어진 리스트의 경우

정렬 순서는 사전 순서( 알파벳 순서)를 따름

(문자열 길이가 긴 것이 더 큰 것이 아님)

문자열 길이 순서로 정렬하려면? ⇒ 정렬에 이용하는 키(key)를 지정

탐색 알고리즘(1) — 선형 탐색 (Linear Search)

- 리스트의 길이에 비례하는 시간 소요 ⇒ O(n)
- 최악의 경우 : 모든 원소를 다 비교해야 함

탐색 알고리즘(2) — 이진 탐색(Binary Search)

- 탐색하려는 리스트가 이미 정렬되어 있는 경우에만 적용 가능
- 크기 순으로 정렬되어 있다는 성질 이용!
- 한 번 비교가 일어날 때마다 리스트 반씩 줄임 (divide & conquer) ⇒ O(log n)

## Class 4
### 재귀 알고리즘 (Recursive Algorithms) 기초
재귀함수 (recursive functions) 란?

하나의 함수에서 자신을 다시 호출하여 작업을 수행하는 것

생각보다 많은 종류의 문제가 재귀적으로(recursively) 해결 가능

예 : 이진 트리(binary trees)
왼쪽 서브트리의 원소들은 모두 작거나 같을 것
오른쪽 서브트리의 원소들은 모두 클 것
이 원칙을 모든 노드에 적용 가능

## Class 5
### 재귀 알고리즘 (Recursive Algoriths) 응용
문제 : n개의 서로 다른 원소에서 m개를 택하는 경우의 수

특정한 하나의 원소 입장에서 볼 때, 이 원소를 포함하는 경우와 그렇지 않은 경우를 따로 계산해서 더한다.

재귀 알고리즘의 유용성

문제 : 하노이의 탑

3개의 기둥에서 각자 다른 크기로 이루어진 원반을 옮기는데 최적의 수를 구하기

## Class 6
### 알고리즘의 복잡도 (Complexity of Algorithms)
시간 복잡도 (Time Complexity) : 문제의 크기와 이를 해결하는 데 걸리는 시간 사이의 관계

공간 복잡도 (Space COmplexity) : 문제의 크기와 이를 해결하는 데 필요한 메모리 공간 사이의 관계

평균 시간 복잡도 (Average Time Complexity) : 임의의 입력 패턴을 가정했을 때 소요되는 시간의 평균

최악 시간 복잡도 (Worst-case Time Complexity) : 가 긴 시간을 소요하게 만드는 입력에 따라 소요되는 시간

Big—O Notation

점근 표기법 (asymptotic notation) 의 하나

어떤 함수의 증가 양상을 다른 함수와의 비교로 표현

(알고리즘의 복잡도를 표현할 때 흔히 쓰임)

O(logn), O(n), O(n^2), O(2^n) 등으로 표기

입력의 크기가 n 일 때

O(logn) — 입력의 크기의 로그에 비례하는 시간 소요

O(n) — 입력의 크기에 비례하는 시간 소요

계수는 그다지 중요하지 않음

선형 시간 알고리즘 —O(n)

예 : n개의 무작위로 나열된 수에서 최댓값을 찾기 위해 선형 탐색 알고리즘을 적용

최댓값 — 끝까지 다 살펴보기 전까지는 알 수 없음

Average case : O(n)

Worst case : O(n)

로그 시간 알고리즘 — O(logn)

예 : n 개의 크기 순으로 정렬된 수에서 특정 값을 값을 찾기 위해 이진 탐색 알고리즘을 적용

이차 시간 알고리즘 — O(n^2)

예 : 삽입 정렬(insertion sort)

Best case : O(n)

Worst case : O(n^2)

보다 나은(낮은) 복잡도를 가지는 정렬 알고리즘

예 : 병합 정렬(merge sort) — O(nlogn)

참고 : 입력 패턴에 따라 정렬 속도에 차이가 있지만 정렬 속도에 차이가 있지만 정렬 문제에 대해 O(nlogn) 보다 낮은 복잡도를 갖는 알고리즘은 존재할 수 없음이 증명되어 있음

1. 정렬할 데이터를 반씩 나누어 각각을 정렬시킨다. = O(logn)
2. 정렬된 데이터를 두 묶음씩 한데 합친다. O(n)

꽤나 복잡한 문제

유명한 예 : 배낭문제 (Knapsack Problem)

## Class 7
### 연결 리스트 (Linked Lists) (1)
추상적 자료구조 (Abstract Data Structure)

Data

- 예 : 정수, 문자열, 레코드, ...

A set of operations

- 삽입, 삭제, 순회...
- 정렬, 탐색...

기본적 연결 리스트

67 ⇒ 34 ⇒ 58

각각의 데이터들이 담겨져 있는 것을 Node라고 부름

Node

- Data
- Link (next)

Node 내의 데이터는 다른 구조로 이루어질 수 있음

예. 문자열, 레코드, 또 다른 연결 리스트 등

리스트의 맨 앞에 원소 : Head 맨 끝의 원소 : Tail

＃of nodes : 3 연결 리스트 안에 노드가 몇 개 있는지 표기

```python
class Node:
	def __init__(self, item):
		self.data = item
		self.next = None

class LinkedList:
	def __init__(self):
		self.nodeCount = 0
		self.head = None
		self.tail = None
```

연산 정의

1. 특정 원소 참조 (k 번째)
2. 리스트 순회
3. 길이 얻어내기
4. 원소 삽입
5. 원소 삭제
6. 두 리스트 합치기

```python
def getAt(self, pos):
	if pos <= 0 or pos > self.nodeCount:
	    return None
		i = 1
		curr = self.head
		while i < pos:
			curr = curr.next
			i += 1
		return curr
```

배열과 비교한 연결 리스트

저장공간

- 배열 : 연속한 위치
- 연결리스트 : 임의의 위치

특정 원소 지칭

- 배열 : 매우 간편 O(1)
- 연결리스트 : 선형탐색과 유사 O(n)

```python
def traverse(self):
	answer = []
	i = 1
	while <= self.nodeCount:
		answer.append(self.getAt(i))
	return answer

  이렇게 하면 안됨.
```

## Class 8
### 연결 리스트(Linked Lists) (2)

연결 리스트 연산 — 원소의 삽입

```python
def insertAt(self, pos, newNode):
	prev = self.getAt(pos - 1)
	newNode.next = prev.next
	prev.next = newNode
	self.nodeCount += 1
    
pos가 가리키는 위치에 (1 <= pos <= nodeCount + 1)
newNode를 삽입하고 성공 / 실패에 따라 True / False 를 리턴

L.inssertAt(pos, newNode)
```

(1) 삽입하려는 위치가 리스트 맨 앞일 때

- prev 없음
- Head 조정 필요

(2) 삽입하려는 위치가 리스트 맨 끝일 때

- Tail 조정 필요

빈 리스트에 삽입할 때? ⇒ 이 두 조건에 의해 처리됨

```python
def insertAt(self, pos, newNode):
    if pos < 1 or pos > self.nodeCount + 1:
	    return False

	if pos == 1:
		newNode.next = self.head
		self.head = newNode
	else:
		prev = self.getAt(pos - 1)
		newNode.next = prev.next
		prev.next = newNode
	if pos == self.nodeCount + 1:
		self.tail = newNode

	self.nodeCount += 1
	return True
```

```python
def insertAt(self, pos, newNode):
	if pos < 1 or pos > self.nodeCount + 1:
		return False

	if pos == 1:
		newNode.next = self.head
		self.head = newNode
	else:
		if pos == self.nodeCount + 1:
			prev = self.tail
		else:
			prev = self.getAt(pos - 1)
		    newNode.next = prev.next
			prev.next = newNode

	if pos == self.nodeCount + 1:
		self.tail = newNode

	self.nodeCount += 1
	return True
```

```python
class LinkedList:
	def __init__(self):
		self.nodeCount = 0
		self.head = None
		self.tail = None

	def  __repr__(self):
		if self.nodeCount == 0:
			return 'LinkedList: empty'

		s = ' '
		curr = self.head
		while curr is not None:
		    s += repr(curr.data)
			if curr.next is not None:
				s += ' -> '
			curr = curr.next
		return s

	def getAt(self, pos):
		if pos <= 0 or pos > self.nodeCount:
			return None

		i = 1
		curr = self.head
		while i < pos:
			curr = curr.next
			i += 1
	    return curr

	def insertAt(self, pos, newNode):
		if pos < 1 or pos > self.nodeCount + 1:
			return False
				
		if pos == 1:
			newNode.next = self.next
			self.next = newNode
		else:
			if pos == self.nodeCount + 1:
			    prev = self.tail
			else:
				prev = self.getAt(pos - 1)
			newNode.next = prev.next
			prev.next = newNode

		if pos == self. nodeCount + 1:
			self.tail = newNode

		self.nodeCount += 1
		return True				
```

연결 리스트 원소 삽입의 복잡도

맨 앞에 삽입하는 경우 : O(1)

중간에 삽입하는 경우 : O(n)

맨 끝에 삽입하는 경우 : O(1)

연결 리스트 연산 — 원소의 삭제

```python
def popAt(self, pos):

pos 가 가리키는 위치의 (1 <= pos <= nodeCount)
node를 삭제하고 그 node의 데이터를 리턴

r = L.popAt(pos)
 코드 구현 주의사항
(1) 삭제하려는 node가 맨 앞의 것일 때
=> prev 없음
=> Head 조정 필요

(2) 리스트 맨 끝의 node를 삭제할 때
=> Tail 조정 필요

* 유일한 노드를 삭제할 때? => 이 두 조건에 의해 처리되는가?
```

삭제하려는 node 가 마지막 node일 때, 즉 pos == nodeCount 인 경우?

하지만 한 번에 처리할 수 없다. (prev를 찾을 방법이 없으므로) ⇒ 앞에서부터 찾아와야 함

연결 리스트 원소 삭제의 복잡도

맨 앞에서 삭제하는 경우 : O(1)

중간에서 삭제하는 경우 : O(n)

맨 끝에서 삭제하는 경우 : O(n)

연결 리스트 연산 — 두 리스트의 연결

```python
def concat(self, L):
    self.tail.next = L.head
	self.tail = L.tail
	self.nodeCount += L.nodeCount

 인자 L 리스트가 빈 것이면 아래대로
def concat(self, L):
	self.tail.next = L.head
	if L.tail:
	    self.tail = L.tail
	self.nodeCount += L.nodeCount
    
 연결 리스트 self의 뒤에 또다른 연결 리스트인 L을 이어붙임
L1.concat(L2)

self.tail.next = L2.head

self.tail = L2.tail

```

## Class 9
### 연결 리스트(Linked Lists) (3)
연결 리스트가 힘을 발휘할 때

순서대로 연결할 때 (스마트폰 팝업화면?) 순서지어 연결 되있는 화면

카카오톡을 위로 밀어 실행 종료할 때

최대 장점 : 삽입과 삭제가 유연하다는 것이 가장 큰 장점

새로운 메서드들을 만들자:

insertAfter(prev, newNode) ⇒ 맨 앞에서 어떻게?

popAfter(prev) ⇒ 맨 앞에서는 어떻게?

조금 변형된 연결 리스트

맨 앞에 dummy node 를 추가한 형태로

```python
class LinkedList:
	def __init__(self):
		self.nodeCount = 0
		self.head = Node(None)
		self.tail = None
		self.head.next = self.tail

	리스트 순회
	def traverse(self):
		result []
		curr = self.head
		while curr.next:
		    curr = curr.next
			result.append(curr.data)
		return result
		
	k번째 원소 얻어내기
	def getAt(self, pos):
		if pos < 1 or pos > self.nodeCount:
			return None
			i = 0
			curr = self.head
			while i < pos:
			    curr = curr.next
				i += 1
			return curr
		
# getAt(0) = Head

def insertAfter(self, prev, newNode):
	newNode.next = prev.next
	if prev.next is None:
		self.tail = newNode
	prev.next = newNode
	self.nodeCount += 1
	return True 

prev가 가리키는 node의 다음에 newNode를 삽입하 성공/ 실패에 따라 True/False 를 추력

L.insertAfter(prev, newNode)

```

메서드 insertAt()의 구현

def insertAt(self, pos, newNode):

이미 구현한 insertAfter() 를 호출하여 이용하는 것으로

1. pos 범위 조건 확인
2. pos == 1 인 경우에는 head 뒤에 새 node 삽입
3. pos == nodeCount + 1 인 경우는 prev ← tail
4. 그렇지 않은 경우에는 prev ← getAt(...)

```python
def insertAt(self, pos, newNode):
	if pos < 1 or pos > self.nodeCount + 1:
		return False

	if pos != 1 and pos == self.nodeCount + 1:
		prev = self.tail
	else:
		prev = self.getAt(pos - 1)
	return self.insertAfter(prev, newNode)

```

연결 리스트 연산 — 원소의 삭제

```python
def popAfter(self, prev):
prev의 다음 node를 삭제하고 그 node의 data를 리턴

r = L.popAfter(prev)

(1) prev가 마지막 node일 때 (prev.next == None)
-> 삭제할 node 없음
-> return Nond

(2) 리스트 맨 끝의 node를 삭제할 때 (curr.next == None)
-> Tail 조정 필요

```

두 리스트의 연결

```python
L1.concat(L2)

self.tail.next = L2.head.next

def concat(self, L):
	self.tail.next = L.head.next
	if L.tail:
		self.tail = L.tail
	self.nodeCount += L.nodeCount

```

## Class 10
### 양방향 연결 리스트 (Doubly Linked Lists)
한 쪽으로만 링크를 연결하지 말고, 양쪽으로! → 앞으로도 (다음 node) 뒤로도 (이전 node) 진행 가능

Node 의 구조 확장

```python
class Node:
    def __init__(self, item):
	    self.data = item
		self.prev = None
		self.next = None
```

리스트 처음과 끝에 dummy node를 두자 ! → 데이터를 담고 있는 node 들은 모두 같은 모양

```python
class DoublyLinkedList:
	def __init__(self, item):
		self.nodeCount = 0
		* self.head = Node(None)
		* self.tail = Node(None)
		self.head.prev = None
		* self.head.next = self.tail
		* self.head.prev = self.head
		self.tail.next = None

* 중요 표시
```

```python
리스트 순회
def traverse(self):
	result = []
	curr = self.head
	while curr.next.next:
		curr = curr.next
		result.append(curr.data)
	return result

리스트 역순회
def reverse(self):
	result = []
	curr = self.tail
	while curr.prev.prev:
		curr = curr.prev
			result.append(curr.data)
	return result

L.insertAfter(prev, newNode)

원소의 삽입
def insertAfter(self, prev, newNode):
	next = prev.next
    newNode.prev = prev
	newNode.next = next
	prev.next = newNode
	next.prev = newNode
	self.nodeCount += 1
	return True
    
특정 원소 얻어내기
def getAt(self, pos):
	if pos < 0 or pos > self.nodeCount:
		return None
	i = 0
	curr = self.head
	while i < pos:
		curr = curr.next
		i += 1
	return curr

원소의 삽입
def insertAt(self, pos, newNode):
	if pos < 1 or pos > self.nodeCount + 1:
		return False
								
	prev = self.getAt(pos - 1)
	return self.insertAfter(prev, newNode)
```

리스트 마지막에 원소 삽입하면? → 마지막에 원소를 넣으면 어떻게 처리할지 기재되어 있지 않음

```python
def getAt(self, pos):
	if pos < 0 or pos > self.nodeCount:
		return None

	if pos > self.nodeCount // 2:
		i = 0
		curr = self.tail
		while i < self.nodeCount - pos + 1:
		    curr = curr.prev
			i += 1
		else:
```

```python
def insertBefore(self, next, newNode):

def popAfter(self, prev):
def popBefore(self, next):
def popAt(self, pos):

def concat(self, L):

```

## Class 11
### 스택 (Stacks)
이전에 배운 것들은 다른 자료구조에 이용될 수 있는 아주 기본적인 것이었다면

이번부터는 특정한 문제를 풀기 위한 알고리즘

스택 (Stack)

- 자료 (data element) 를 보관할 수 있는 (선형) 구조
- 단, 넣을 때에는 한 쪽 끝에서 밀어 넣어야 하고 → push 연산
- 꺼낼 때에는 같은 쪽에서 뽑아 꺼내야 하는 제약이 있음 → pop 연산
- 후입선출 (LIFO - Last-In First-Out) 특징을 가지는 선형 자료구조

스택의 동작

초기상태 : 비어있는 스택(empty stack)

데이터 원소 A를 스택에 추가

데이터 원소 B를 스택에 추가

데이터 원소 꺼내기

비어 있는 스택에서 데이터 원소를 꺼내려 할 때 → 스택 언더플로우(stack underflow)

꽉 찬 스택에 데이터 원소 넣으려 할 때 → 스택 오버플로우(stack overflow)

```python
S = Stack()
s.push(A)
S.push(B)
r1 = S.pop()
r2 = S.pop()
r3 = S.pop()
```

(1) 배열 (array) 을 이용하여 구현

- Python 리스트와 메서드들을 이용

(2) 연결 리스트 (linked list)를 이용하여 구현

- 지난 강의에서 마련한 양방향 연결 리스트 이용

연산의 정의

- size() - 현재 스택에 들어 있는 원소의 수를 구함
- isEmpty() - 현재 스택이 비어 있는지를 판단
- pust(x) - 데이터 원소 x를 스택에 추가
- pop() - 스택의 맨 위에 저장된 데이터 원소를 제거 (또한, 반환)
- peek() - 스택의 맨 위에 저장된 데이터 원소를 반환 (제거하지 않음)

```python
#배열로 구현한 스택
class ArrayStack:

#스택의 크기를 리턴
	def size(self):
		return len(self.data)

#스택이 비어 있는지 판단
	def isEmpty(self):
		return self.size() == 0

#데이터 원소를 추가
	def push(self, item):
		self.data.append(item)

#데이터 원소를 삭제(리턴)
	def pop(self):
		return self.data.pop()

#스택의 꼭대기 원소 반환
	def peek(self):
		return self.data[-1]

```

```python
from doublylinkedlist import Node
from doublylinkedlist import DoublyLinkedList

class LinkedListStack:

	def __init__(self):
		self.data = DoublyLinkedList()

	def size(self):
		return self.data.getLength()

	def isEmpty(self):
		return self.size() == 0

	def push(self, item):
		node = Node(item)
		self.data.insertAt(self.size() + 1, node)

	def pop(self):
		return self.data.popAt(self.size())

	def peek(self):
		return self.data.getAt(self.size()).data
```

```python
from pythonds.basic.stack import Stack
S = Stack()
dir(S)
#파이썬 스택 라이브러리
```

연습문제 — 수식의 괄호 유효성 검사

올바른 수식:

- (A + B)
- {(A + B) * C}
- [(A + B) * (C + D)]

올바르지 않은 수식:

- (A + B
- A + B)
- {A * (B + C })
- [(A + B) * (C + D)}

알고리즘 설계 — 수식을 왼쪽부터 한 글자씩 읽어서:

- 여는 괄호 - ( or { or [ -를 만나면 스택에 푸시
- 닫는 괄호 - ) or } or ] - 를 만나면:
    - 스택이 비어 있으면 올바르지 않은 수식
    - 스택에서 pop, 쌍을 이루는 여는 괄호인지 검사
        - 맞지 않으면 올바르지 않은 수식
        
        
## Class 12
### 스택의 응용 : 수식의 후위 표기법
중위 표기법과 후위 표기법

중위 표기법 (infix notation)

(A + B) * (C + D)

- 연산자가 피연산자들의 사이에 위치

후위 표기법 (postfix notation) 

A B + C D + *

- 연산자가 피연산자들의 뒤에 위치

중위 표현식 → 후위 표현식

[중위] A * B + C → [후위] A B * C +

[중위] A + B * C → [후위] A B C * +

[중위] A + B + C → [후위] A B + C +

괄호의 처리

[중위] (A + B) * C

[후위] A B + C *

- 여는 괄호는 스택에 push
- 닫는 괄호를 만나면 여는 괄호가 나올 때까지 pop

[중위] A * (B + C)

[후위] A B C + *

연산자를 만났을 때, 여는 괄호 너머까지 pop 하지 않도록 여는 괄호의 우선순위는 가장 낮게 설정

예제 1

[중위] (A + B) * (C + D)

[후위] A B + C D + *

에제 2

[중위] (A + (B - C)) * D

[후위] A B C - + D *

[중위] A * (B - (C + D))

[후위] A B C D + - *

알고리즘의 설계

연산자의 우선순위 설정

```python
prec = {
	'*' : 3, '/' : 3,
	'+' : 2, '-' : 2,
	'(' : 1
}

```

중위 표현식을 왼쪽부터 한 글자씩 읽어서

피연산자이면 그냥 출력

'(' 이면 스택에 push

')' 이면 '(' 이 나올 때까지 스택에서 pop, 출력

연산자이면 스택에서 이보다 높(거나 같)은 우선순위 것들을 pop, 출력. 그리고 이 연산자는 스택에 push

스택에 남아 있는 연산자는 모두 pop, 출력

코드의 구현 — 힌트

- 스택의 맨 위에 있는 연산자와의 우선순위 비교
    - 스택의 peek() 연산 이용
- 스택에 남아 있는 연산자를 모두 pop() 하는 순환문
    - while not opStack.isEmpty():

## Class 13
### 스택의 응용 : 후위 표기 수식 계산
중위 표기법 (infix notation) 

- 연산자가 피연산자들의 사이에 위치
- (A + B) * (C + D)

후위 표기법 (postifx notation)

- 연산자가 피연산자들의 뒤에 위치
- A B + C D + *

알고리즘의 설계

후위 표현식을 왼쪽부터 한 글자씩 읽어서

피연산자면 스택에 push

연산자를 만나면 스택에서 pop → (1), 또 pop → (2)

(2) 연산 (1) 을 계산, 이 결과를 스택에 push

수식의 끝에 도달하면 스택에서 pop → 이것이 계산 결과

```python
def splitTokens(exprStr)
	tokens = []
	val = 0
	valProcessing = False
	for c in exprStr:
		if c == ' ':
			continue
		if c in '0123456789':
			val = val * 10 int(c)
			valProcessing = True
		else:
			if valProcessing:
				toekns.append(val)
				val = 0
			valProcessing = False
			tokens.append(c)
	if valProcessing:
		toekns.append(val)

return tokens
```

```python
from stacks import ArrayStack as Stack

def infixToPostfix(tokenList):
	prec = {
		'*' : 3,
		'/' : 3,
		'+' : 2,
		'-' : 2.
		'(' : 1
	}

	opStack = Stack()
	postfixList = []

	for token in tokenList:
		if type(token) is int:
			pass
		elif token == '(':
			pass
		elif token == ')':
			pass
		else:
			pass

	while not opStack.isEmpty():
		pass

	return postfixList

```

```python
from stacks import ArrayStack as Stack

	def postfixEval(tokenList)
		valStack = Stack()

		for token in tokenList:
			if type(token) is int:
				pass
			elif token == '*':
				pass
			elif token == '/':
				pass
			elif token == '+':
				pass
			elif token == '-':
				pass

		return valStack.pop()

def solution(expr):
	tokens = splitTokens(expr)
	postfix = infixToPostfix(tokens)
	val = postfixEval(postfix)
	return val
```

## Class 14
### 큐 (Queue)
자료 (data element) 를 보관할 수 있는 (선형) 구조

단, 넣을 때에는 한 쪽 끝에서 밀어 넣어야 하고

→ 인큐 (enqueue) 연산

꺼낼 때에는 반대 쪽에서 뽑아 꺼내야 하는 제약이 있음

→ 디큐 (dequeue) 연산

선입선출 (FIFO - First-In First-Out) 특징을 가지는 선형 자료구조

대기열 = 큐

```python
#초기 상태 : 비어있는 큐 (empty Queue)
Q = Queue()

#데이터 원소 A를 큐에 추가
Q.enqueue(A)

#데이터 원소 B를 큐에 추가
Q.enqueue(B)

#데이터 원소 꺼내기
r1 = Q.dequeue() # r1 = 'A'
r2 = Q.dequeue() # r2 = 'B'

```

큐의 추상적 자료구조 구현

(1) 배열 (array) 을 이용하여 구현

- Python 리스트와 메서드들을 이용

(2) 연결 리스트 (linked list) 를 이용하여 구현

- 이전 강의에서 마련한 양방향 연결 리스트 이용

연산의 정의

- size() - 현재 큐에 들어 있는 데이터 원소의 수를 구함
- isEmpty() - 현재 큐가 비어 있는지를 판단
- enqueue(x)  - 데이터 원소 x를 큐에 추가
- dequeue() - 큐의 맨 앞에 저장된 데이터 원소를 제거 (또한, 반환)
- peek() - 큐의 맨 앞에 저장된 데이터 원소를 반환 (제거하지 않음)

```python
#배열로 구현
class ArrayQueue:

#빈 큐를 초기화
	def __init__(self):
		self.data = []

#큐의 크기를 리턴
	def size(self):
		return len(self.data)

#큐가 비어 있는지 판단
	def isEmpty(self):
		return self.size() == 0

#데이터 원소를 추가
	def enqueue(self,item):
		self.data.append(item)

#데이터 원소를 삭제(리턴)
	def dequeue(self):
		return self.data.pop(0)

#큐의 맨 앞 원소 반환
	def peek(self):
		return self.data[0]
```

배열로 구현한 큐의 연산 복잡도

size() = O(1)

isEmpty() = O(1)

enqueue() = O(1)

dequeue() = O(n) → 맨 앞 원소를 꺼내면 뒤에 있는 모든 원소를 앞으로 당겨야함

peek() = O(1)

```python
#이중 연결 리스트로 큐를 구현
class linkedList

```

## Class 15
### 환형 큐(Circular Queues)
큐 (Queue) 의 사용

자료를 생성하는 작업과 그 자료를 이용하는 작업이 비동기적으로 (asynchronously) 일어나는 경우

Producer 가 만든 자료를 Consumer 가 차곡차곡 쌓인 데이터를 순서대로 꺼내는 경우


자료를 생성하는 작업이 여러 곳에서 일어나는 경우

Producer 1 ,2  → Consumer


자료를 이용하는 작업이 여러 곳에서 일어나는 경우

Producer → Consumer 1, 2


자료를 생성하는 작업과 그 자료를 이용하는 작업이 양쪽 다 여러 곳에서 일어나는 경우 ex.운영체제

Producer 1, 2 → Consumer 1, 2


자료를 처리하여 새로운 자료를 생성하고, 나중에 그 자료를 또 처리해야 하는 작업의 경우


환형 큐 (Circular Queue)

정해진 개수의 저장공간을 빙 돌려가며 이용

운영체제 등에서는 리소스가 한정되있기 때문에 큐의 길이를 한정함

큐가 가득 차면 ? → 더이상 원소를 넣을 수 없음 (큐 길이를 기억하고 있어야 함)

![Screenshot_20211020-231307_Notion.jpg](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/1e867393-3076-4196-9a72-b2facdd624c7/Screenshot_20211020-231307_Notion.jpg)


환형 큐의 추상적 자료구조 구현

연산의 정의

- size() - 현재 큐에 들어 있는 데이터 원소의 수를 구함
- isEmpty() - 현재 큐가 비어 있는지를 판단
- isFull() - 큐에 데이터 원소가 꽉 차 있는지를 판단
- enqueue(x) - 데이터 원소 x를 큐에 추가
- dequeue() - 큐의 맨 앞에 저장된 데이터 원소를 제거 (또한, 반환)
- peek() - 큐의 맨 앞에 저장된 데이터 원소를 반환 (제거하지 않음)

배열로 구현한 환형 큐

정해진 길이 n (예에서는 6) 의 리스트를 확보해 두고

Q.enqueue(A) → rear = A

Q.enqueue(B....) → rear = B....

front 와 rear 를 적절히 계산하여 배열을 환형으로 재활용


## Class 16
### 우선순위 큐 (Priority Queues)
큐가 FIFO (First-In First-Out) 방식을 따르지 않고 원소들의 우선순위에 따라 큐에서 빠져나오는 방식

작은 수가 우선순위가 높다고 가정

Enqueue : 6 7 3 2

Dequeue : 2 3 6 7

ex. 운영체제의 CPU 스케줄러

서로 다른 두 가지 방식이 가능함:

1. Enqueue 할 때 우선순위 순서를 유지하도록
2. Dequeue 할 때 우선순위 높은 것을 선택

→ 어느 것이 더 유리할까? → 1번이 더 유리함 → Dequeue 할 때 모든 원소를 탐색하지 않아도 되기 때문

서로 다른 두 가지 재료를 이용할 수 있음:

1. 선형 배열 이용
2. 연결 리스트 이용

→ 어느 것이 더 유리할까? 시간적으로 볼 때는 연결 리스트가 유리하다 → 인큐를 할 때 정렬해야하니까 중간에 삽입할 경우가 많아 연결 리스트가 이용함

→ 선형 배열은 공간 활용성이 우수

```python
from doublylinkedlist import Node, DoublyLinkedList

#양방향 연결 리스트를 이용하여 빈 큐를 초기화
class PriorityQueue:

	def __init__(self, x):
		self.queue = DoublyLinkedList

class ProiortyQueue:

#주의: 양방향 연결 리스트의 getAt() 메서드를 이용하지 않음! -> 왜? 
def enqueue(self, x):
newNode = Node(x)
curr = [빈칸]
while [빈칸] and [빈칸]:
curr = curr.next
self.queue.[빈칸](curr.newNode)

```

## Class 17
### 트리 (Trees)
트리는 이차원의 자료구조

정보를 조직화하고 검색하는데 굉장히 용이함

- 정점 (node) 과 간선 (edge) 을 이용하여 데이터의 배치 형태를 추상화한 자료구조

Leaf : 이파리

Root : 뿌리

컴퓨터 자료구조에서는 거꾸로 표현함


제일 위에 있는 노드는 루트노드

제일 아래에 위치한 노드는 리프노드

루트노드와 리프노드 사이에 있는 노드를 내부 (Internal) 노드라고 함


노드 G, H, J는 서로 형제간 (sibling) 이라고 함

부모의 부모의 ... - 조상(ancestor) 노드

자식의 자식... - 후손(descendant) 노드

노드의 수준 (Level)

루트노드는 level 0

바로 아래 노드는 level 1 그 아래 노드는 level 2 ...

트리의 높이 (Height)

트리의 높이 (height) = 최대 수준 (level) + 1

*깊이(depth) 라고도 함

height = depth = level 3일경우 + 1을 해서 4가 된다.


부분 트리 (서브트리 — Subtree)

노드의 차수 (Degree) = 자식 (서브트리)의 수

어느 한 노드의 자식 노드는 여러 개가 될 수 있지만 부모 노드는 한 개 밖에 될 수가 없음.

degree : 0 → leaf nodes

이진 트리 (Binary Tree)

모든 노드의 차수가 2 이하인 트리


재귀적으로 정의할 수 있음:

빈 트리(empty tree) 도 이진트리임

루트 노드 + 왼쪽 서브트리 + 오른쪽 서브트리 (단, 이 때 왼쪽과 오른쪽 서브트리 또한 이진 트리)


포화 이진 트리 (Full Binary Tree)

모든 레벨에서 노드들이 모두 채워져 있는 이진 트리


완전 이진 트리 (Complete Binary Tree)

높이 k 인 완전 이진 트리

레벨 k - 2 까지는 모든 노드가 2개의 자식을 가진 포화 이진 트리

레벨 k - 1 에서는 왼쪽부터 노드가 순차적으로 채워져 있는 이진 트리

## Class 18
### 이진 트리 (Binary Trees)
이진 트리의 추상적 자료구조

연산의 정의

- size() — 현재 트리에 포함되어 있는 노드의 수를 구함
- depth() — 현재 트리의 깊이 (또는 높이: height) 를 구함
- 순회 (traversal)

이진 트리의 구현 — 노드 (Node)

```python
#이진 트리의 구현 -- 노드 (Node)
class Node:
	def __init__(self, item):
		self.data = item
		self.left = None
		self.right = None

	def size(self):
		l = self.left.size() if self.left else 0
		r = self.right.size() if self.right else 0
		return l + r + 1

	def depth(self)

#이진 트리의 구현 -- 트리 (Tree)
class BinaryTree:
	def __init__(self, r):
		self.root = r

#이진 트리의 구현 --size()
#재귀적인 방법으로 쉽게 구할 수 있음!
#전체 이진 트리의 size() = left subtree 의 size() + right subtree 의 size() + 1(자기 자신)

	def size(self):
		if self.root:
			return self.root.size()
		else:
			return 0

#이진 트리의 구현 --depth()
	def depth(self):
		if ...

```

이진 트리의 순회 (Traversal)

- 깊이 우선 순회 (depth first traversal)
    - 중위 순회 (in-order traversal)
    - 전위 순회 (pre-order traversal)
    - 후위 순회 (post-order traversal)
        - 어떤 노드를 기준으로 했을 때 왼쪽 서브트리도 순회해야하고 오른쪽 서브트리도 순회해야 하는데 왼쪽 오른쪽 서브트리를 방문하는 사이에 방문하면 중위순회, 먼저 방문하면 전위순회, 모두 순회한 뒤에 방문하면 후위순회임
    
- 넓이 우선 순회 (breadth first traversal)

중위 순회

순회의 순서

1. Left subtree
2. 자기 자신
3. Right subtree


```python
#중위 순회 (In-order Traversal)
class Node:

	def inorder(self):
		tarversal = []
		if self.left:
			traversal += self.left.inorder()
		traversal.append(self.data)
		if self.right:
			traversal += self.right.inorder()
		return traversal

class BinaryTree:

	def inorder(self):
		if self.root:
			return self.root.inorder()
		else:
			return []
```

전위 순회  (Pre-order Traversal)

순회의 순서

1. 자기 자신
2. Left subtree
3. Right subtree


후위 순회 (Post-order Traversal)

순회의 순서

1. Left subtree
2. Right subtree
3. 자기 자신

## Class 19
### 이진 트리 - 넓이 우선 순회 (breadth first traversal)
넓이 우선 순회 (Breadth First Traversal)

- 원칙
    - 수준 (level) 이 낮은 노드를 우선적으로 방문
    - 같은 수준의 노드들 사이에는
        - 부모 노드의 방문 순서에 따라 방문
        - 왼쪽 자식 노드를 오른쪽 자식보다 먼저 방문
    - 재귀적 (recursive) 방법이 적합한가? → 적합하지 않음
    - 한 노드를 방문했을 대, 나중에 방문할 노드들을 순서대로 기록해 두어야 함 → 큐 (Queue)를 이용하면 어떨까?
    - 

루트 노드부터 낮은 레벨 순 (왼쪽 → 오른쪽) 으로 순회함


큐를 이용해서 이후에 방문해야하는 노드들을 순서대로 정렬함

```python
#넓이 우선 순회 알고리즘 구현
class BinaryTree:

def bft(self):

```

1. (초기화) traversal ← 빈 리스트, q ← 빈 큐
2. 빈 트리가 아니면, root node 를 q 에 추가 (enqueue)
3. q 가 비어 있지 않은 동안
    1. node ← q 에서 원소를 추출 (dequeue)
    2. node 를 방문
    3. node 의 왼쪽, 오른쪽 자식 (이 있으면) 들을 q에 추가
4. q 가 빈 큐가 되면 모든 노드 방문 완료

## Class 20
### 이진 탐색 트리 (Binary Search Trees) (1)

모든 노드에 대해서

- 왼쪽 서브트리에 있는 데이터는 모두 현재 노드의 값보다 작고
- 오른쪽 서브트리에 있는 데이터는 모두 현재 노드의 값보다 큰 성질을 만족하는 이진 트리

(중복되는 데이터 원소는 없는 것으로 가정)


이진 탐색 트리를 이용한 데이터 검색


(정렬된) 배열을 이용한 이진 탐색과 비교

장점 : 데이터 원소의 추가, 삭제가 용이

단점 : 공간 소요가 큼 → 항상 O(logn)의 탐색복잡도?

이진 탐색 트리의 추상적 자료구조

데이터 표현 - 각 노드는 (key, value) 의 쌍으로

키를 이용해서 검색 가능

보다 복잡한 데이터 레코드로 확장 가능

연산의 정의

- insert(key, data) — 트리에 주어진 데이터 원소를 추가
- remove(key) — 특정 원소를 트리로부터 삭제 (연산 복잡!)
- lookup(key) — 특정 원소를 검색
- inorder() — 키의 순서대로 데이터 원소를 나열
- min(), max() — 최소 키, 최대 키를 가지는 원소를 각각 탐색

이진 탐색 트리에 원소 삽입

## Class 21
### 이진 탐색 트리 (Binary Search Trees) (2)
이진 탐색 트리에서 원소 삭제

1. 키 (key) 를 이용해서 노드를 찾는다.
    1. 해당 키의 노드가 없으면, 삭제할 것도 없음
    2. 찾은 노드의 부모 노드도 알고 있어야 함 (아래 2번 때문)
2. 찾은 노드를 제거하고도 이진 탐색 트리 성질을 만족하도록 트리의 구조를 정리한다.

인터페이스의 설계

입력 : 키 (key)

출력 : 삭제가 된 경우 True, 해당 키의 노드가 없는 경우 False

```python
class BinSearchTree:
	def remove(self, key):
		node, parent = self.lookup(key)
		if node:
			...
			return True
		else:
			return False
```

이진 탐색 트리 구조의 유지

삭제되는 노드가

1. 말단 (leaf) 노드인 경우
    1. 그냥 그 노드를 없애면 됨 → 부모 노드의 링크를 조정 (좌? 우?)
2. 자식을 하나 가지고 있는 경우
    1. 삭제되는 노드 자리에 그 자식을 대신 배치 → 자식이 왼쪽? 오른쪽? → 부모 노드의 링크를 조정 (좌? 우?)
3. 자식을 둘 가지고 있는 경우
    1. 삭제되는 노드보다 바로 다음 (큰) 키를 가지는 노드를 찾아 그 노드를 삭제되는 노드 자리에 대신 배치하고 이 노드를 대신 삭제

```python
class Node:
	def countChildren(self(:
		count = 0
		if self.left:
			count += 1
		if self.right:
			count += 1
		return count
```

말단 (Leaf) 노드의 삭제


자식이 하나인 노드의 삭제 (X를 삭제하는 경우)


삭제되는 노드 (X) 가 root node 인 경우는 어떻게?

→ 대신 들어오는 자식이 새로 root 가 됨

자식이 둘인 노드의 삭제


이진 탐색 트리가 별로 효율적이지 못한 경우

```python
T = BinSearchTree()
T.insert(1, 'John')
T.insert(2, 'Mary')
T.insert(3, 'Anne')
T.insert(4, 'Peter')

```


위 그림은 선형탐색과 비슷한 복잡도가 나옴

보다 나은 성능을 보이는 이진 탐색 트리들

높이의 균형을 유지함으로써 O(logn) 의 탐색 복잡도 보장

삽입, 삭제 연산이 보다 복잡

## Class 22
### 힙(Heaps)
이진 트리의 한 종류 (이진 힙 - binary heap)

1. 루트 (root) 노드가 언제나 최댓값 또는 최솟값을 가짐
    1. 최대 힙 (max heap), 최소 힙 (min heap)
2. 완전 이진 트리여야 함

최대 힙 (Max Heap) 의 예

![Screenshot_20211022-205828_Notion.jpg](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/f3f78d5b-5f84-447c-aa8b-95278882aae3/Screenshot_20211022-205828_Notion.jpg)

재귀적으로도 정의 됨 (어느 노드를 루트로 하는 서브트리도 모두 최대 힙)

이진 탐색 트리와의 비교

1. 원소들은 완전히 크기 순으로 정렬되어 있는가?
2. 특정 키 값을 가지는 원소를 빠르게 검색할 수 있는가?
3. 부가의 제약 조건은 어떤 것인가? (완전 이진 트리)

최대 힙 (Max Heap) 의 추상적 자료구조

연산의 정의

- **init**() — 빈 최대 힙을 생성
- insert(item) — 새로운 원소를 삽입
- remove() — 최대 원소 (root node) 를 반환 (그리고 동시에 이 노드를 삭제

데이터 표현의 설계

배열을 이용한 이진 트리의 표현

노드 번호 m 을 기준으로

- 왼쪽 자식의 번호 : 2 * m
- 오른쪽 자식의 번호 : 2 * m + 1
- 부모 노드의 번호 : m // 2

완전 이진 트리이므로 노드의 추가 / 삭제는 마지막 노드에서만


코드의 구현 — 빈 힙 생성

```python
class Maxheap:
	def __init__(self):
		self.data = [None]

```

최대 힙에 원소 삽입

1. 트리의 마지막 자리에 새로운 원소를 임시로 저장
2. 부모 노드와 키 값을 비교하여 위로, 위로, 이동



최대 힙에 원소 삽입 — 복잡도

원소의 개수가 n 인 최대 힙에 새로운 원소 삽입

→ 부모 노드와의 대소 비교 최대 횟수 : log2

최악 복잡도 O(logn) 의 삽입 연산

삽입 연산의 구현 — insert(item) 메서드

힌트 : python에서 두 변수의 값 바꾸기

a = 3; b = 5

a, b = b, a

```python
class MaxHeap:
	def insert(self, item):
		...

```

최대 힙에서 원소의 삭제

1. 루트 노드의 제거 — 이것이 원소들 중 최댓값
2. 트리 마지막 자리 노드를 임시로 루트 노드의 자리에 배치
3. 자식 노드들과의 값 비교와 아래로, 아래로 이동
    1. 자식은 둘 있을 수도 있는데, 어느 쪽으로 이동? (더 큰 값 쪽으로 이동)

예

최대 원소를 삭제하라! 

1. 루트 노드의 제거 — 이것이 원소들 중 최댓값
2. 트리 마지막 자리 노드를 임시로 루트 노드의 자리에 배치


최대 힙으로부터 원소 삭제 — 복잡도

원소의 개수가 n 인 최대 힙에서 최대 원소 삭제

→ 자식 노드들과의 대소 비교 최대 회 : 2 * log2n

최악 복잡도 O(logn) 의 삭제 연산

삭제 연산의 구현 — remove() 메서드

```python
class MaxHeap:
	def remove(self):
		if len(self.data) > 1:
			self.data[1], self.data[-1] = self.data[-1], self.data[1]
			data = self.data.pop(-1)
			self.maxHeapify(1)
		else:
			data = None
		return data

def maxHeapify(self, i):
left = ...
right = ...
smallest = i
#자신 (i), 왼쪽 자식(left), 오른쪽 자식(right) 중 최대를 찾음
#-> 이것의 인덱스를 smallest 에 담음
if smallest != i:
#현재 노드 (i) 와 최댓값 노드 (smallest) 의 값 바꾸기
#재귀적으로 maxHeapify 를 호출
```

최대/최소 힙의 응용

1. 우선 순위 큐 (priority queue)
    1. Enqueue 할 때 '느슨한 정렬' 을 이루고 있도록 함 : O(logn)
    2. Dequeue 할 때 최댓값을 순서대로 추출 : O(logn)
    3. 제 16강에서의 양방향 연결 리스트 이용 구현과 효율성 비교
2. 힙 정렬 (heap sort)
    1. 정렬되지 않은 원소들을 아무 순서로나 최대 힙에 삽입 : O(logn)
    2. 삽입이 끝나면, 힙이 비게 될 때까지 하나씩 삭제 : O(logn)
    3. 원소들이 삭제된 순서가 원소들의 정렬 순서
    4. 정렬 알고리즘의 복잡도 : O(nlogn)

힙 정렬 (heap sort)의 코드 구현

```python
def heapsort(unsorted):
	H = MaxHeap()
	for item in unsortedd:
		H.insert(item)
	sorted = []
	d = H.remove()
	while d:
		sorted.append(d)
		d = H.remove()
	return sorted
```
