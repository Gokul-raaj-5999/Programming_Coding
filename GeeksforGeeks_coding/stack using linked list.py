class StackNode:

    # Constructor to initialize a node
    def __init__(self, data):
        self.data = data
        self.next = None
        
class MyStack:

    def __init__(self):
        self.head = None
        
    #Function to push an integer into the stack.
    def push(self, data):
        tem = StackNode(data)
        tem.next = self.head
        self.head = tem
        
        
        # Add code here


    #Function to remove an item from top of the stack.
    def pop(self):
        if self.head is None:
            return -1
        tem = self.head
        self.head = tem.next
        return tem.data
        # Add code here



#{ 
 # Driver Code Starts
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = MyStack()
        q = int(input())
        q1 = list(map(int, input().split()))
        i = 0
        while(i < len(q1)):
            if(q1[i] == 1):
                s.push(q1[i + 1])
                i = i + 2
            elif(q1[i] == 2):
                print(s.pop(), end=" ")
                i = i + 1
            elif(s.isEmpty()):
                print(-1)
        print()

# } Driver Code Ends
