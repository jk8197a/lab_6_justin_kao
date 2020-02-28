from node import Node

#Problem 2
class LinkedList:

	#initialize linked list with attributes
	def __init__(self, head = None, size = 0, tail = None):
		self.head = head
		self.size = size
		self.tail = tail

	#establish getters and setters for attributes
	def getHead(self):
			return self.head

	def setHead(self, h):
			self.head = h 

	def getSize(self):
			return self.size

	def setSize(self, s):
			self.size = s

	def getTail(self):
			return self.tail

	def setTail(self, t):
			self.tail = t

	#establish method to say when list is empty
	def isEmpty(self):

		if (self.getSize() > 0):
			return(False)
		return(True)

	#establish method for adding node
	def addNode(self, ndata):

		#create instance of new node
		newNode = Node(data = ndata)

		#Simple case
		if(self.isEmpty()):

			#set head to new node
			#head stays with first node
			self.setHead(newNode)

		else:
			self.getTail().setNext(newNode)
			#temp_tail = self.getTail()
			#temp_tail.setNext(newNode)

		#set tail to new node
		self.setTail(newNode)

		#increment size 
		self.setSize(self.size + 1)


def main():

	#create instance of linked list
	ll = LinkedList()
	ll.addNode(ndata = 100)
	ll.addNode(ndata = 200)
	ll.addNode(ndata = "AU")
	print(ll.getTail().getData())

if __name__ == '__main__':
	main()