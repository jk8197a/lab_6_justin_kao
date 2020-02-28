#Problem 1
class Node:

	#initialize node with attributes 
	def __init__(self, data, next_pointer = None):
		self.data = data
		self.next_pointer = next_pointer

	#establish getters and setters for attributes 
	def getData(self):
		return self.data

	def setData(self, d):
		self.data = d

	def getNext(self):
		return self.next_pointer

	def setNext(self, n):
		self.next_pointer = n
