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

![Screenshot_20211020-230913_Chrome.jpg](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/c33c2c40-3dd0-4ac3-a7d1-1896472c1ecf/Screenshot_20211020-230913_Chrome.jpg)

자료를 생성하는 작업이 여러 곳에서 일어나는 경우

Producer 1 ,2  → Consumer

![Screenshot_20211020-230939_Notion.jpg](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/b59a2905-fb9d-4751-9a63-857b3acd6a94/Screenshot_20211020-230939_Notion.jpg)

자료를 이용하는 작업이 여러 곳에서 일어나는 경우

Producer → Consumer 1, 2

![Screenshot_20211020-230955_Chrome.jpg](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/11f23195-6563-4b97-b377-b7489cf83bad/Screenshot_20211020-230955_Chrome.jpg)

자료를 생성하는 작업과 그 자료를 이용하는 작업이 양쪽 다 여러 곳에서 일어나는 경우 ex.운영체제

Producer 1, 2 → Consumer 1, 2

![Screenshot_20211020-230831_Chrome.jpg](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/d4815c2c-608a-43f4-9026-91596838a105/Screenshot_20211020-230831_Chrome.jpg)

자료를 처리하여 새로운 자료를 생성하고, 나중에 그 자료를 또 처리해야 하는 작업의 경우

![Screenshot_20211020-231220_Chrome.jpg](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/01f8318d-32bf-4e4e-b92e-63f7219bda7f/Screenshot_20211020-231220_Chrome.jpg)

환형 큐 (Circular Queue)

정해진 개수의 저장공간을 빙 돌려가며 이용

운영체제 등에서는 리소스가 한정되있기 때문에 큐의 길이를 한정함

큐가 가득 차면 ? → 더이상 원소를 넣을 수 없음 (큐 길이를 기억하고 있어야 함)

![Screenshot_20211020-231307_Notion.jpg](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/1e867393-3076-4196-9a72-b2facdd624c7/Screenshot_20211020-231307_Notion.jpg)

![Screenshot_20211020-232006_Chrome.jpg](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/c143cc83-39a8-4a19-82ef-bdd4df6b0614/Screenshot_20211020-232006_Chrome.jpg)

![Screenshot_20211020-231829_Notion.jpg](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/48877481-70c4-451f-a1fa-ccecb0ecb383/Screenshot_20211020-231829_Notion.jpg)

![Screenshot_20211020-231431_Chrome.jpg](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/9438ca6c-be7b-480e-8ae2-7a48ce2cb12e/Screenshot_20211020-231431_Chrome.jpg)

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
