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

