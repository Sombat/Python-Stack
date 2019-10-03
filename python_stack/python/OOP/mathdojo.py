# Assignment: MathDojo
# Objectives:
# 1. Practice creating a class and creating new instances
# 2. Practice chaining methods
# 3. Practice writing flexible functions that can take a varying number of arguments

class MathDojo:
	def __init__(self):
		self.result = 0
	def add(self, num, *nums):
		self.result = num
		for a in nums:
			self.result += nums
		return self
	# def subtract(self, num, *nums):
	# 	self.result = num
	# 	for b in nums:
	# 		self.result += nums
	# 	return self
# create an instance:
md = MathDojo()
# to test:
x = md.add(2).add(2,5,1).result#.subtract(3,2).result
print(x)	# should print 5
# run each of the methods a few more times and check the result!