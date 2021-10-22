class Node:

	def __init__(self, key, data):
		self.key = key
		self.data = data
		self.left = None
		self.right = None

	def inorder(self):
		traversal = []
		if self.left:
			traversal += self.left.inorder()
		traversal.append(self)
		if self.right:
			traversal += self.rightinorder()
		return traversal
		
	def lookup(self, key, parent=None):
		if key < self.key:
			if self.left:
				return self.left.lookup(key, self)
			else:
					return None, None
		elif key > self.key:
			if self.right:
				return self.left.lookup(key, self)
			else:
				return None, None
		else:
			return self, parent

	def insert(self, key, data):
		if key < self.key:
			...
		elif key > self.key:
			...
		else:
			raise KeyError('...')


class BinSearchTree:
	def __init__(self):
		self.root = None

	def inorder(self):
		if self.root:
			return self.root.inorder()
		else:
			return []

def min(self):
	if self.root:
		return self.root.min()
	else:
		return self

max() 는 min() 과 완전 대칭함

#코드 구현 -- lookup()
#입력 인자 -- 찾으려는 대상 키
#리턴 :
#찾은 노드와, 그것의 부모 노드 (각각, 없으면 None 으로)

	def lookup(self, key):
		if self.root:
			return self.root.lookup(key)
		else:
			return None, None

#코드 구현 -- insert()
#입력 인자 :  키, 데이터 원소
#리턴 : 없음

	def insert(self, key, data):
		if self.root:
			self.root.insert(key, data)
		else:
			self.root = Node(key, data)