class Node:
	def __init__(self, value):
		self.value = value
		self.next = None

	def getNext(self):
		return self.next

	def setNext(self, node):
		self.next = node

	def getValue(self):
		return self.value

#Implementing the Stack class through Node
class Stack:
	def __init__(self):
		self.items = None

	def isEmpty(self):
		return self.items == None

	def push(self, value):
		node = Node(value)
		node.setNext(self.items)
		self.items = node

	def pop(self):
		node = self.items
		self.items = self.items.getNext()
		return node

	def top(self):
		return self.items.getValue()

	def size(self):
		if self.isEmpty():
			return 0
		count = 0
		point = self.items
		while point != None:
			count += 1
			point = point.getNext()

		return count

#Implementing the Queue class through Node
class Queue:
	def __init__(self):
		self.items = None

	def isEmpty(self):
		return self.items == None

	def enqueue(self, value):
		node = Node(value)
		if self.isEmpty():
			self.items = node
		else:
			point = self.items
			while point.getNext() != None:
				point = point.getNext()
			point.setNext(node)

	def dequeue(self):
		node = self.items
		self.items = self.items.getNext()
		return node

	def size(self):
		if self.isEmpty():
			return 0
		count = 0
		point = self.items
		while point != None:
			count += 1
			point = point.getNext()
		return count

