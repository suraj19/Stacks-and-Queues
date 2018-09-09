class ArrayQueue:
	def __init__(self):
		self.data=[None]*10
		self.size=0
		self.front=0
	def __len__(self):
		return self.size
	def is_empty(self):
		return self.size==0
	def first(self):
		if not self.is_empty():
			return self.data[self.front]	#retuns the 1st element in queue
	
	def enqueue(self,ele):
		if self.size==len(self.data):
			self.resize(2*len(self.data))
		avail=(self.front+self.size)%len(self.data) 
		#print(ele)
		self.data[avail]=ele
		self.size+=1
	def resize(self,cap):
			old=self.data
			walk=self.front
			self.data=[None]*cap
			for k in range(len(old)):
				self.data[k]=old[walk]
				walk=(1+walk)%len(old)
			self.front=0
	def dequeue(self):
		if self.is_empty():
			print("The Queue is Empty")
		Answer=self.data[self.front]
		self.data[self.front]=None
		self.front=(self.front+1)%len(self.data)
		self.size-= 1
		return Answer
		'''if (0<self.size<len(self.data)//4):
			self.resize(len(self.data//2)
		return Answer
		else:
			return None'''
	'''def viewqueue(self):
		if self.is_empty():
			print("The Queue is Empty")
		else:
			return self.data'''
	def viewqueue(self):
		return self.data