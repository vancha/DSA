'''
Depth first search searches a binary search tree from the top to the bottom, moving through the entire left branch, before it moves on to the next
i.e: over the "depth" of a tree

basically how dfs works, is it creates a visited set and a stack and adds the root of a tree to that stack, then:
while there are elements on the stack:
    - pops an element off the stack
    - mark the element as visited (it does not need to be checked if it is visited or not)
      - add it's children to the stack if any are present
'''
def depth_first_search(root, val):
    visited = {}
    stack = [root]

    while stack:
        element = stack.pop()
        if element.val == val:
            return element
        visited[element] = True
        left = element.left
        right = element.right
        if left:
            stack.append(left)
        if right:
            stack.append(right)
    
    return None
