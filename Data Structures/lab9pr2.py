

from TreeNode import *

def getheight(root):
    #base case if tree is empty
    if root is None:
        return 0
    #recursive case
    else:
        #checks if left and right subtree are empty
        if root.left == None and root.right == None:
            #recursive definition
            return max(getheight(root.left), getheight(root.right)) + 0
        #if left and right subtree are not empty
        else:
            #recursive definition
            return max(getheight(root.left), getheight(root.right)) + 1
        
