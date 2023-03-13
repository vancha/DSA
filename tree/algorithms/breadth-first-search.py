'''
Breadth first search

to keep this explanation as simple as possible, breadth first search, moves through a tree from left to right, before it moves from top to bottom. Hence, it moves over the "breadth" of the tree.
To do this, it makes use of a data structure called a queue. As a mnemenic, you can try to remember that "breadth" first search, uses a queue (which i personally always view as a wide data structure, acceptinging input from the left, and giving output from the right), where *depth* first search, uses a stack (where stack is a vertical data structure, accepting input from the top, and also giving output from there). so wide == queue and deep == stack.

basically how bfs works, is it creates a visited set and a queue and adds the root of a tree to that queue, then:
while there are elements in the queue:
    - pops the last element off the queue
    - checks if that popped value had been visited or not
      - if not, marks it visited and adds it's children to the queue
      - if it is, does nothing
'''

#the bfs function takes the root of a tree as an input
def BFS(root):
    #we create a queue and add the root of the tree to it.
    queue = deque()
    queue.appendleft(root)
    visited = {}
    #as long as there are elements in the queue
    while queue:
        #remove them
        u = queue.pop()
        #if it hadn't already been marked as visited
        if u not in visited:
            #mark it as visited now (and print it if you want)
            visited[u] = True
            #get it's left and right children
            left = u.left
            right = u.right
            #check if they've been visited, if not, add them to the queue
            if left and left not in visited:
                queue.appendleft(left)
            if right and right not in visited:
                queue.appendleft(right)
