#Date: 08-08-18
#Author: A.Suraj Kumar
#Roll No: 181046037
#Implement a function that reverses a list of elements by pushing them onto a stack in one order, and write them back to the list in reversed order.


import LimitedStack

def reverses():
	for i in data_list:
		Ls.StackPush(i)
	print('The elements in a Stack:',Ls.Viewstack())
	print("The top of the stack is : ",Ls.StackPeek())
	rev_list=Ls.data
	rev_list.reverse()#reverses list 
	print('The reversed list of elements: ',rev_list)


Ls=LimitedStack.LimitedStack()
ls=LimitedStack.LimitedStack()
data_list=[x for x in input("Enter an elements: ").split(',')]
rev_list=[]
reverses()



















