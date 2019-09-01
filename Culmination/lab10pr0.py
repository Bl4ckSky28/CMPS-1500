
from BST import *

def printTree(root, indent=0):
    if root != None:
        printTree(root.right, indent+4)
        print(indent*" " + str(root.data))
        printTree(root.left, indent+4)

root1 = TreeNode(4)
root1.left = TreeNode(2)
root1.right = TreeNode(6)
root1.right.right= TreeNode(7)
root1.left.right = TreeNode(3)
root1.right.left = TreeNode(5)
root1.left.left = TreeNode(1)

printTree(root1)

def constructTree1():
    tree = BST()
    tree.insert(1)
    tree.insert(2)
    tree.insert(3)
    tree.insert(4)
    tree.insert(6)
    tree.insert(5)
    tree.insert(7)
    return tree

def constructTree2():
    tree = BST()
    tree.insert(4)
    tree.insert(1)
    tree.insert(7)
    tree.insert(6)
    tree.insert(5)
    tree.insert(2)
    tree.insert(3)
    return tree

print(constructTree2())
