class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None

    def insert(self,data):
        self.root = self.add(self.root,data)
        return self.root 
    
    def add(self,root,data):
        if root is None:
            return Node(data)
        else:
            if data < root.data:
                    root.left = self.add(root.left,data)
            else:
                    root.right = self.add(root.right,data)
        return root
    
    def min(self):
        current_node = self.root
        while current_node.left:
             current_node = current_node.left
        return current_node.data
    
    def max(self):
        current_node = self.root
        while current_node.right:
              current_node = current_node.right
        return current_node.data
    def dfs(node):
        if not node:
            return (0, [])
        
        left_sum, left_path = dfs(node.left)
        right_sum, right_path = dfs(node.right)
        
        max_child_sum = max(left_sum, right_sum)
        
        current_sum = max(node.val, node.val + max_child_sum)
        current_path = [node.val] if current_sum == node.val else [node.val] + (left_path if left_sum > right_sum else right_path)
        
        return (current_sum, current_path)
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)
T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = T.insert(i)

T.printTree(root)
print("--------------------------------------------------")
print("Min :",T.min())
print("Max :",T.max())