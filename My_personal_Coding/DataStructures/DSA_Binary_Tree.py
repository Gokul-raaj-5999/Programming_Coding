"""
notes:
breath first traversal/ BFS = level order 
depth first traversal/ DFS = preorder, inorder, postoredr.
"""
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

spacecount = [2] #space count 3 will be okay for print bTree in 2d space.
# print binary tree have 3 methods inorder, preorder, postorder traversal.

def symentric(root): #to check weather BT is symentric or not True/False
    if not root:
        return True
    def dfs(l, r):
        if not l and not r:
            return True
        if not l or not r:
            return False
        if l.val == r.val:
            return dfs(l.left, r.right) and dfs(l.right, r.left)
        return False     
        
    return dfs(root.left, root.right)   

def dfs(root, depth): # max depth of BT for both left and right.
    if not root:
        return depth
    return max( dfs(root.left, depth+1), dfs(root.right, depth+1))

def levelordercall(root):
    def levelorder(root):
        h = treehight(root)
        for i in range(0, h+1):
            currentlevel(root, i)

    def currentlevel(root, level):
        if not root:
            return
        if level == 1:
            print(root.val, end= ' ')
        elif level > 1:
            currentlevel(root.left, level-1)
            currentlevel(root.right, level-1)

    def treehight(node):
        if not node:
            return 0
        else:
            lhight = treehight(node.left)
            rhight = treehight(node.right)
            if lhight > rhight:
                return lhight +1
            else:
                return rhight +1
    return levelorder(root)

def inorder(root): #left -> node -> right.
    if root:
        inorder(root.left)
        print(root.val, end= ' ')
        inorder(root.right)

def preorder(root): #node -> left -> right.
    if root:
        print(root.val, end = ' ')
        preorder(root.left)
        preorder(root.right)    

def postorder(root): #left -> rigth -> node.
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.val, end= ' ') 

def print2Dshape(root, space):
    if  not root:
        return None

    space += spacecount[0]
    print2Dshape(root.right, space)
    print()
    for i in range(spacecount[0], space):
        print(end = ' ')

    print(root.val)
    print2Dshape(root.left, space)

def rootinsert(temp, key):
    if not temp: #if temp is not in tree then we have to make this key as a new root.
        root = Node(key)
        return None
    q = []
    q.append(temp)
    while len(q):   #when this q is empty which means its starting from root.. and we are searching till 
        temp = q[0]  #all left and right so where we have space we will add this key there.. first preference is left and then right.
        q.pop(0)       # or else it will add that element in that q list.. 
        if not temp.left:
            temp.left = Node(key)
            break
        else:
            q.append(temp.left)
        if not temp.right:
            temp.right = Node(key)
            break
        else:
            q.append(temp.right)
    
def getLeafCount(node):
    if node is None:
        return 0 
    if(node.left is None and node.right is None):
        return 1 
    else:
        return getLeafCount(node.left) + getLeafCount(node.right)

        

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)


    print('printing inorder traversal')
    inorder(root)
    print()

    print('printing preorder traversal')
    preorder(root)
    print()

    print('printing postorder traversal')
    postorder(root)
    print()

    rootinsert(root, 10)
    rootinsert(root, 11)
    rootinsert(root, 12)

    levelordercall(root)

    print( dfs(root, 0)) 

    print( symentric(root))

    print()
    print2Dshape(root, 0)

    print(getLeafCount(root))

    