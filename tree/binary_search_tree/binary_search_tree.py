'''
A binary search tree. The structure is the exact same as a regular binary tree, except
it has some unique properties for inserting values and searching for them. Mainly, inserting
new values makes sure the new value gets placed in the tree in such a way that it stays sorted.
searching can therefore be done over only one half of the tree, making for some serious
performance improvement over regular binary trees
'''
class TreeNode:
    def __init__(self, value, left=None,right=None):
        self.left  = left
        self.right = right
        self.value = value
    
    def is_leaf_node(self):
        return not self.right and not self.left

    def insert(self, root, value):
        if value < root.value:
            if root.left:
                insert(root.left, value)
            else:
                root.left = TreeNode(value)
        else:
            if root.right:
                insert(root.right, value)
            else:
                root.right = TreeNode(value)
