class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue():
    def __init__(self):
        self.head = None

    def pushbach(self,data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            return
        tem = self.head
        while tem.next:
            tem = tem.next
        tem.next = newNode
        return

    def popfrient(self):
        if self.head is None:
            print('empty')
            return
        tem = self.head
        self.head = tem.next
        return

    def printing(self):
        if self.head is None:
            print('empty')
            return
        tem = self.head
        print('printing-> ', end= ' ')
        while tem.next:
            print(tem.data , end= ' ')
            tem = tem.next
        print(tem.data)



q = Queue()
q.pushbach(1)
q.pushbach(2)
q.pushbach(3)
q.printing()
q.popfrient()
q.printing()
q.pushbach(10)
q.printing()