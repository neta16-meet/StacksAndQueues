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
		count = 0
		point = self.items
		while point != None:
			count ++
			point = point.getNext()

		return count

class Queue:
	def __init__(self):
		self.items = None

	def isEmpty(self):
		return self.items == None

	def enqueue(self, node):
		

