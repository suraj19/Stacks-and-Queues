#Date: 06-09-18
#Author: A.Suraj Kumar
#Roll No: 181046037
#Implement a transfer function and two temporary stacks, to replace the contents of a given stack S with those same elements, but in reverse order.

import LimitedStack
def transfer():
	for i in data_list:
		Ls.StackPush(i)
	print("Elements in Stack: ",Ls.Viewstack())
	for i in range(len(Ls.data)):
		ls.StackPush(Ls.data.pop())
	print("The reverse of Stack: ",ls.Viewstack())

Ls=LimitedStack.LimitedStack()
ls=LimitedStack.LimitedStack()
data_list=[x for x in input("Enter an elements: ").split(',')]
transfer()
