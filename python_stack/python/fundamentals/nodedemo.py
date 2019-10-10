# SLL are specifically for OOP, where data is stored as object, look into memory management and how to write to specific spots in memory.

class Node:
	def __init(self, value):
		self.value = value
		self.next = None

class SLL:
	def __init(self):
		self.head = None

	def addToFront(self, value):
		newnode = Node(value)
		newnode.next = self.head
		self.head = newnode
		return self

	def prependval(self, val, valuetofind):
		newnode = Node(val)
		runner = self.head # runner is a value to keep where self.head is
		valueFound = False

		if self.head.value == valuetofind:
			valuefound = True
			newnode.next = self.head # .next is pointer or arrow
			self.head = newnode
			return self
		while runner.next: # this loop is there to get us to the right spot to do the arrow switches
			if runner.next.value != valuetofind:
				runner = runner.next
		newnode.next = runner.next
		runner.next = newnode
		return self

	def addToBack(self, value):
		newnode = node(value)
		if self.head == None:
			self.addToFront(value)
			return self
		runner = self.head

	def displaySLL():

	sll1 = SLL() # create new SLL
	sll1.addToBack(12).addToBack(5).addToBack(7).addToBack(9).displaySLL() #add values to sll1 and then display it on terminal
	sll1