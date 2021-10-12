def sum(n):
	if n <= 1:
		return n
	else:
		return n + sum(n-1)

# Recursive version
# O(n)

def sum(n):
	s = 0
	while n >= 0:
		s += n
		n -= 1
	return s

# Iterative version 
# O(n)

def what(n):
    if n <= 1:
        return 1
    else:
        return n * what(n - 1)

# n! 팩토리얼 구하기

# 피보나치 구하기

def solution(x):
    if x==0 : return 0
    elif x==1 or x==2 : return 1
    else:
        return solution(x-1)+solution(x-2)
    
from math import factorial as f

def combi(n, m):
	return f(n) / (f(m) * f(n-m))


def combi(n, m):
	return combi(n - 1, m) + combi(n - 1, m - 1)
# Trivial case를 고려하지 않은 케이스

def combi(n, m):
	if n == m:
		return 1
	elif m == 0:
		return 1
	else:
		return combi(n - 1, m) + combi(n - 1, m - 1)
 # 효율성 측면에서 좋은가를 고려하기

def fibo(n):
		if n <= 1:
			return n
		return fibo(n - 1) + fibo(n - 2)

 # 피보나치 수열 함수 호출

# 재귀적 알고리즘와 반복적 알고리즘의 효율성 테스트
def rec(n):
	if n <= 1:
		return n
	else:
		return rec(n - 1) + rec(n - 2)


def iter(n):
	if n <= 1:
		return n
	else:
		i = 2
		t0 = 0
		t1 = 1
		while i <= n:
			t0, t1 = t1, t0 + t1
			i += 1
		return t1

while True:
	nbr = int(input("Enter a number: "))
	if nbr == -1
		break

	ts = time.time()
	fibo = iter(nbr)
	us = time.time() - ts
	print("Iterative version: %d (%,3f)" % (fibo, ts))
	ts = time.time()
	fibo = rec(nbr)
	ts = time.time() - ts
	print("Recursive version: %d (%.3f)" % (fibo, s)
          
