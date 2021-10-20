class CircularQueue:

	def __init__(self, n): # 빈 큐를 초기화
		self.maxCount = n #인자로 주어진 최대 큐 길이 설정
		self.data = [None] * n
		self.count = 0
		self.front = -1
		self.rear = -1
	
	def size(self): # 큐가 비어 있는가?
		return self.count == 0
	
	def isFull(self): # 큐가 꽉 차 있는가?
		return self.count == self.maxCount
	
	
	def enqueue(self, x): # 큐에 데이터 원소 추가
		self.isFull():
	# IndexError('Queue full') exception 으로 처리
		self.rear = [빈칸]
		self.data[self.rear] = x
		self.count += 1
	
	def dequeue(self): # 큐에서 데이터 원소 뽑아내기
		if [빈칸]:
			raise IndexError('Queue empty')
		self.front = [빈칸]
		x = [빈칸]
		self.count -= 1
		return x

def peek(self):
	if [빈칸]:
		raise IndexError('Queue empty')
	return [빈칸]