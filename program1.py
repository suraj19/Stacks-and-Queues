#Date: 08-08-18
#Author: A.Suraj Kumar
#Roll No: 181046037
#Implement a function with signature transfer(S,T) that transfers all elements from Stack S onto Stack T, so that that elements that starts at the top of S is the first to be inserted into T, and element at the bottom of S ends up at the top of T.


import LimitedStack
def Transfer():
	e=[x for x in input('Enter a List of Elements:').split(',')]
	T=LimitedStack.LimitedStack()
	for i in range(len(e)):
		T.StackPush(e.pop())
	print('input: ',e)
	print('My Stack: ',T.Viewstack())
	return T
Transfer()
