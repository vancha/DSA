'''
A binary search tree. The structure is the exact same as a regular binary tree, except
it has some unique properties for inserting values and searching for them. Mainly, inserting
new values makes sure the new value gets placed in the tree in such a way that it stays sorted.
searching can therefore be done over only one half of the tree, making for some serious
performance improvement over regular binary trees
'''
class TreeNode:
    def __init__(self, value, left=None,right=None):
        self.left_child  = left
        self.right_child = right
        self.value = value
        
    #if this node has no left and right children, it's a leaf node
    def is_leaf_node(self):
        return not self.right_child and not self.left_child
        
    #insert takes the root of a truee, and a value to insert
    def insert(self, root, value):
        #inside this function, root is known as "current_node", cause it's the node we are currently looking at
        current_node = root

        #if the value to insert is smaller than the current node's value
        if value < current_node.value:
            #and the current node has a left child
            if current_node.left_child:
                #then the new current node is set to be that left child, and we start from the top again
                insert(current_node.left_child, value)
            else:
                #if not, the left child becomes a new node with the value to insert
                current_node.left_child = TreeNode(value)
        else:
            #we do the same for the right node as we've done for the left node above
            if current_node.right_child:
                insert(current_node.right_child, value)
            else:
                current_node.right_child = TreeNode(value)
