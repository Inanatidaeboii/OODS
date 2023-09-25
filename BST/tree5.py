class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def insert(root, val):
    if root is None:
        return TreeNode(val)
    if val < root.val:
        root.left = insert(root.left, val)
    elif val > root.val:
        root.right = insert(root.right, val)
    return root

def preorder_traversal(root):
    if root:
        print(root.val, end=" ")
        preorder_traversal(root.left)
        preorder_traversal(root.right)

def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.val, end=" ")
        inorder_traversal(root.right)

def postorder_traversal(root):
    if root:
        postorder_traversal(root.left)
        postorder_traversal(root.right)
        print(root.val, end=" ")

def breadth_first_search(root):
    if not root:
        return
    
    queue = []
    queue.append(root)
    
    while queue:
        node = queue.pop(0)
        print(node.val, end=" ")
        
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

# รับ input และสร้าง BST
input_values = list(map(int, input("Enter Input : ").split()))
root = None
for val in input_values:
    root = insert(root, val)

# แสดงผลลัพธ์แบบ Preorder, Inorder, Postorder, และ Breadth First Search
print("Preorder :", end=" ")
preorder_traversal(root)
print("\nInorder :", end=" ")
inorder_traversal(root)
print("\nPostorder :", end=" ")
postorder_traversal(root)
print("\nBreadth :", end=" ")
breadth_first_search(root)