class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
class single_linked_list:
    def __init__(self):
        self.head = None

    def append(self, new_data):
        new_node = Node(new_data)

        if self.head is None: #
            self.head = new_node #as head is none soo moving the pointer self.head to new_node
            return

        temp = self.head
        while temp.next is not None:
            temp = temp.next

        temp.next = new_node
        new_node.next = None
        print("appended value: ", new_node.value)
        return

    def push(self, new_data): #push in front 
        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        self.head = new_node
        new_node.next = temp     
        return

    def insert(self, loc, new_data):
        new_node = Node(new_data)
        loc = int(loc)
        count = 1
        prev = self.head
        while count < loc:
            prev = prev.next
            count+=1
        
        new_node.next = prev.next
        prev.next = new_node
        return

    def pop(self):
        if self.head is None: #if empty
            print('empty')

        temp = self.head #if has one node it will del that too
        if temp.next is None:
            self.head = None
            return

        temp = self.head  #has more that one value
        while temp.next :
            now = temp
            temp = temp.next
            if temp.next is None:
                now.next = None           
                return
                
        return

    def print(self):
        if self.head is None:
            print("empty")
            return

        print('elements: ', end= " ")
        temp = self.head #here we have subpointer to move along..
        while temp.next is not None :
            print(temp.value , end = ' ')
            temp = temp.next
        print(temp.value)    #printing the last value which has null   
        return           

    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
        return self.print()


sl = single_linked_list() #main code
sl.append(1)
sl.append(2)
while(1):
    ip = list(map(str, input().split()))

    if ip[0] == 'app':
        data = ip[1]
        sl.append(data)
    elif ip[0] == 'print':
        sl.print()
    elif ip[0] == 'pop':
        sl.pop()
    elif ip[0] == 'push':
        data = ip[1]
        sl.push(data)
    elif ip[0] == 'ins':
        loc, data = ip[1], ip[2]
        sl.insert(loc, data)
    elif ip[0] == 'break':
        break
    elif ip[0] == 'rev':
        sl.reverse()