#Date: 09-09-18
#Author: A.Suraj Kumar
#Roll No: 181046037
'''Suppose you have three nonempty stacks R, S and T.
Describe a sequence of operations that results in S storing all elements originally in T below of S’s original elements,
 with both sets of those elements in their original configuration. For example, if R = [1,2,3], S = [4, 5] and T = [6, 7, 8, 9],
 the final configuration should have R = [1, 2, 3] and S = [6, 7, 8,  9, 4, 5].'''

import LimitedStack
Ls=LimitedStack.LimitedStack()
ls=LimitedStack.LimitedStack()
R = [1,2,3]#(or)[x for x in input("Enter an elements: ").split(',')]
S = [4, 5]#(or)[x for x in input("Enter an elements: ").split(',')]
T = [6, 7, 8, 9]#(or)[x for x in input("Enter an elements: ").split(',')]
for i in range(len(R)):
	Ls.StackPush(R.pop())
R=Ls.Viewstack()
print('Status of Stack in R: ',R)
print("The top of the stack is : ",Ls.StackPeek())
for i in range(len(S)):
	Ls.StackPush(S.pop())
R=Ls.Viewstack()
print('Status of Stack in R: ',R)
print("The top of the stack is : ",Ls.StackPeek())
for i in range(len(T)):
	Ls.StackPush(T.pop())
R=Ls.Viewstack()
print('Status of Stack in R: ',R)
print("The top of the stack is : ",Ls.StackPeek())
for j in range(len(Ls.data)):
	if (j > 2):
		ls.StackPush(Ls.data.pop())
S=ls.Viewstack()
print('The Elements in stack S: ',S)
print('Top of a stack in S: ',ls.StackPeek())
print('Elements in Stack T: ',T)