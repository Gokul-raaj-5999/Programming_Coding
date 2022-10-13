class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class stack():
    def __init__(self):
        self.head = None

    def push(self, data):
        tem = Node(data)

        tem.next = self.head
        self.head = tem
        

    def pop(self):
        if self.head is None:
            print('empty')
            return 
        tem = self.head
        print('poped elemet', tem.data)
        self.head = tem.next
        

    def print(self):
        print('printing...', end=' ')
        if self.head is None:
            print('empty')
            return
        tem = self.head
        while tem.next is not None:
            print(tem.data, end= ' ')
            tem = tem.next
        print(tem.data)
            

s = stack()
s.push(1)
s.push(2)
s.push(3)
s.pop()
s.pop()
s.push(5)
s.push(10)
s.print()

    