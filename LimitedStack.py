
class LimitedStack:
	capacity=10
	def __init__(self):
		self.data=[]
		self.count=0
	def isStackEmpty(self):
		return self.count==0
	def isStackFull(self):
		return self.count==LimitedStack.capacity
	def StackLength(self):
		return self.count
	def StackPeek(self):
		if not self.isStackEmpty():
			return self.data[-1]
	def StackPush(self,ele):
		if not self.isStackFull():
			self.data.append(ele)
			self.count+=1
	def StackPop(self):
		if not self.isStackEmpty():
			self.data.pop()
			self.count==1
	def Viewstack(self):
		if not self.isStackEmpty():
			return self.data
	



























