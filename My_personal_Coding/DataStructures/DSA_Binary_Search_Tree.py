class Node():
    def __init__(self, data):
        self.val = data
        self.right = None
        self.left = None

def insert(root, key):
    if root is None:
        print('insert->done')
        return Node(key)
    
    print(root.val, end = ' ')
    if root.val == key:
        return root
    elif root.val > key:
        root.left = insert(root.left, key)
    elif root.val < key:
        root.right = insert(root.right, key)
    return root

def inorder(root):
    if root:
        print(root.val, end = ' ')
        inorder(root.left)
        inorder(root.right)

def preorder(root):
    if root:
        preorder(root.left)
        print(root.val, end= ' ')
        preorder(root.right)

        

root = Node(1)
insert(root, 2)
insert(root, 3)
insert(root, 4)
insert(root, 5)

inorder(root)
print()

preorder(root)
print()


        