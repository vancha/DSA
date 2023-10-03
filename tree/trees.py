'''
A simple binary tree data structure. All it exists of is a value, a possible left child, and a possible right child.
since trees are recursive datastructures, those left and right children can in turn be binary trees themselves.
'''
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left_child = left
         self.right_child = right
