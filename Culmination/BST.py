from TreeNode import *

######################################################
# BST functions (need root node as argument)

def toString(root, indent=0): # O(n) runtime
    if root == None:
        return ""
    return toString(root.right, indent+4)\
           + indent*" " + str(root.data)+"\n"\
           + toString(root.left, indent+4)

def inorderTrav(root):
    if root!=None:
        inorderTrav(root.left)
        print(root.data, end=" ")
        inorderTrav(root.right)

def preorderTrav(root):
    if root!=None:
        print(root.data, end=" ")
        preorderTrav(root.left)
        preorderTrav(root.right)

def postorderTrav(root):
    if root!=None:
        postorderTrav(root.left)
        postorderTrav(root.right)
        print(root.data, end=" ")


def tree_max(root):
    # Special case for empty tree
    if root == None:
        return None

    # Base case
    if root.right == None:
        return root.data

    # Recursive case
    return tree_max(root.right)

def tree_find(root, x):
    # Recursive binary search, in a BST.
    # Return True if found, False if not found
    if root == None:
        return False
    
    if root.data == x:
        return True
    
    if x<root.data:
        return tree_find(root.left,x)
    else: # x>root.data
        return tree_find(root.right,x)


def tree_insert(root, x):
    # Insert a new item into a binary search tree
    # Return new root

    # Special case for empty tree
    if root == None:
        return TreeNode(x) # new root        
    
    if root.data <= x:
        if root.right == None:
            root.right = TreeNode(x)
        else:
            tree_insert(root.right, x)
    elif root.data > x:
        if root.left == None:
            root.left = TreeNode(x)
        else:
            tree_insert(root.left, x)
            
    return root # Need to return current root    


########################################################
# BST class with methods (use self.root to access root)

class BST:
    def __init__(self, root=None): # O(1) runtime
        self.root = root       

    def __repr__(self): # O(n) runtime
        return toString(self.root)

    def inorder(self):
        inorderTrav(self.root)
        print()

    def preorder(self):
        preorderTrav(self.root)
        print()

    def postorder(self):
        inorderTrav(self.root)
        print()

    def max_rec(self):
        return tree_max(self.root)

    def max(self):
        current = self.root
        
        # Tree is empty
        if current == None:
            return None

        # Tree is non-empty
        while current.right != None:
            current = current.right

        return current.data    

    def min(self):
        # Special case for empty tree   
        if self.root == None:
            return None
        # Tree is non-empty
        current = self.root
        if current == None:
            return None
        
        while (current.left != None):
            current = current.left
            
        return current.data   

    def find(self, x):
        return tree_find(self.root, x)

    def insert(self, x):
        self.root = tree_insert(self.root,x)
 
