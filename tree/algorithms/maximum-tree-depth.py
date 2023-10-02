'''
A recursive algorithm to count the maximum depth of a tree
the algorithm goes as follows:
  if the root node is None, the depth is guaranteed to be zero
  if the current element has no children (i.e: no right and left) return it's depth
  otherwise, if it has children at all, return 1 + the bigger of either the depth of the left or right subtree
  
'''
def maxDepth(self, root: Optional[TreeNode]) -> int:
  if not root:
    return 0
  if not root.left and not root.right:
    return 1
  else:
    return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))     
