#Date: 09-09-18
#Author: A.Suraj Kumar
#Roll No: 181046037
#Design a queue using two stacks as instance variables, such that all queue operations execute in amortized O(1) time.
#AMORTIZED COST: Avarage cost per operation small even if one of the operation is expensive
#here we are transfering elemts to Stack1 and againg transfering it to Stack2 and the top of the element is dequeued from stack
#here the 1st dequeued operation is costly but other operations are low time cost
#amortized cost= (Total no costs)/(total no of operations)i.e., here we have 'n' number of operations.
import LimitedStack
Ls=LimitedStack.LimitedStack()
ls=LimitedStack.LimitedStack()
def enqueue(i):
		return Ls.StackPush(i)
def dequeue():
	if not ls.isStackEmpty():
		return ls.StackPop()

data_list=[x for x in input("Enter an elements: ").split(',')]
for i in data_list:
	enqueue(i)
print('The elements in a Stack1:',Ls.Viewstack())
print("The top of the stack1 is : ",Ls.StackPeek())
#print('The Queue with Stacks: ',Ls.Viewstack())
for i in range(len(Ls.data)):
	ls.StackPush(Ls.data.pop())
print("The elements in Stack2: ",ls.Viewstack())
print('Top of a stack: ',ls.StackPeek())
print('Element in queue before dequeue: ',ls.Viewstack())
for i in range(len(ls.data)):
	dequeue()
	print('the status of queue after dequeue: ',ls.Viewstack())
