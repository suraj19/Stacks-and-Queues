#Date: 23-08-18
#Author: A.Suraj Kumar
#Roll No: 181046037
#Modify ArrayStack implementation so that the stack’s capacity is limited to maxlen elements. If push is called when the stack is at full capacity, throw a Full exception.

import sys
import LimitedStack
def maxlen():
	s1=[x for x in input('Enter a List of Elements:').split(',')]
	maxlen=5	
	Ls=LimitedStack.LimitedStack()
	if len(s1)<=maxlen:
		Ls.StackPush(s1)
		print("Elements in Stack",s1)
	else:
		raise Exception('Stack is Out of Capacity')
			 
maxlen()
