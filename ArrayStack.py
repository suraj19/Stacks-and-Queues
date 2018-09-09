class ArrayStack:
	
	def __init__(self):
		self.data=[]#creates a list 
	def __len__(self):
		return len(self.data)#it will returns no. of elements in a stack
	def isempty(self):
		return len(self.data) == 0#it will check weather the stack is empty
	def push(self,e):
		self.data.append(e)#add an element to stack
	def top(self):
		if self.isempty():
			raise("Stack is Empty")#Again they check stack is empty
		return self.data[-1]#print the top element of a stack
	def pop(self):
		if self.isempty():
			raise("Stack is Empty")
		self.data.pop()#pop an element of the stack
	def Viewstack(self):
		if not self.isempty():
			return self.data

'''A=ArrayStack()
list_1=[x for x in input("Enter an element to stack:").split(',')]
for i in list_1:
	A.push(i)
print("Stack:",A.Viewstack())
for k in list_1:
	A.top()
print("The top element in Stack is: ", A.top())
for j in list_1:
	A.pop()
print("Stack:", A.Viewstack())'''
