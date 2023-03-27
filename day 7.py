'''class stack:
    def __init__(self,max_size):
        self.__max_size=max_size
        self.__elements=[None]*self.__max_size
        self.__top=-1
    def is_full(self):
        if(self.__top==self.__max_size-1):
            return True
        return False
    def is_empty(self):
        if(self.__top==-1):
            return True
        return False
    def push(self,data):
        if(self.is_full()):
            print("The stack is full")
        else:
            self.__top+=1
            self.__elements[self.__top]=data
    def pop(self):
        if(self.is_empty()):
            print("The stack is empty")
        else:
            data=self.__elements[self.__top]
            self.__top-=1
            return data
    def display(self):
        if(self.is_empty()):
            print("The stack is empty")
        else:
            index=self.__top
            while(index>=0):
                print(self.__elements[index])
                index-=1
    def get_max_size(self):
        return self.__max_size
ball_stack=stack(4)
print("Is it empty",ball_stack.is_empty())
ball_stack=stack(5)
print("Is it empty",ball_stack.is_empty())
ball_stack.push(6)
ball_stack.push(7)
ball_stack.push(8)
ball_stack.display()
print("Size of the stack",ball_stack.get_max_size())
print("The element deleted",ball_stack.pop())
print("After deleting the element")
ball_stack.display()
print("The size of stack",ball_stack.get_max_size())'''


'''class Queue:
    def __init__(self,max_size):
        self.__max_size=max_size
        self.__elements=[None]*self.__max_size
        self.__rear=-1
        self.__front=0
    def is_full(self):
        if(self.__rear==self.__max_size-1):
            return True
        return False
    def is_empty(self):
        if(self.__front>self.__rear):
            return True
        return False
    def enqueue(self,data):
        if(self.is_full()):
            print("The queue is full")
        else:
            self.__rear+=1
            self.__elements[self.__rear]=data
    def dequeue(self):
        if(self.is_empty()):
            print("The queue is empty")
        else:
            data=self.__elements[self.__front]
            self.__front-=1
            return data
    def display(self):
        for index in range(self.__front,self.__rear+1):
            print(self.__elements[index])
    def get_max_size(self):
        return self.__max_size
queue1=Queue(10)
print("It is full",queue1.is_full())
print("It is empty",queue1.is_empty())
queue1.enqueue(100)
queue1.display()
queue1.enqueue(200)
queue1.enqueue(300)
queue1.enqueue(400)
queue1.display()
queue1.enqueue(500)
queue1.display()
print("The element deleted",queue1.dequeue())
queue1.display()'''


'''def get_evenly_divisible_numbers(queue):
    new_queue=[]
    for num in queue:
        if all(num%i==0 for i in range(1,11)):
            new_queue.append(num)
    return new_queue
queue=[13983,10080,7113,2520,2500]
new_queue=get_evenly_divisible_numbers(queue)
print(new_queue)'''


'''queue1=[3,6,8]
queue2=['b','y','u','t','r','o']
merge_queue=[]
for i in range(max(len(queue1),len(queue2))):
    if i<len(queue1):
        merge_queue.append(queue1[i])
    if i<len(queue2):
        merge_queue.append(queue2[i])
print(merge_queue)'''


'''def merge_list(list1,list2):
    merged_data=""
    list2.reverse()
    for i in range(len(list1)):
        if(list1[i]is None):
            list[i]=" "
        if(list2[i]is None):
            list[i]=" "
        merged_data+=str(list[i])+str(list2[i])+" "
    return merged_data[:-1]
list1=['T','sK','None','b1']
list2=['ue','is','y','he']
merged_data=merge_list(list1,list2)
print(merged_data)'''


'''def check_numbers(number_queue):
    solution_queue1=Queue(5)
    while(not number_queue.is_empty()):
        status=0
        element=number_queue.dequeue()
        for i in range(1,11):
            if element%i!=0:
                status=1
                break
        if status==0:
            solution_queue1.enqueue(element)
    return solution_queue1'''


class Node:
    def __init__(self,dataval=None):
        self.dataval=dataval
        self.nextval=None
class SLinkedList:
    def __init__(self):
        self.headval=None
    def listprint(self):
        printval=self.headval
        while printval is not None:
            print(printval.dataval)
            printval=printval.nextval
list=SLinkedList()
list.headval=Node("Mon")
e2=Node("Tue")
e3=Node("Wed")
list.headval.nextval=e2
e2.nextval=e3
list.listprint()
