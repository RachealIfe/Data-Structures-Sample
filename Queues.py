class Queue:
    def __init__(self):
        self.items=[]

    def is_empty(self):
        return self.items ==[]

    def enqueue(self, item):

        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def print_queue(self):
        print(self.items)

q=Queue()
'''userin=input("Enter end if you have finished writing the values")
if userin == "end":
    print("End")
else:
    q.enqueue(userin)'''
q.enqueue('a')
q.enqueue('b')
q.enqueue(42)
q.print_queue()

q.dequeue()
q.print_queue()
