#singly linked list
#this singly linked list is implemented like it is for a lot of the problems on leetcode. it consists of elements that have only one value and one pointer to the next element
class ListNode:
  def __init__(self, val=0, next=None):
    #the elements value
    self.val = val
    #the pointer to the next element
    self.next = next
    
#doubly linked list
#this doubly linked list is implemented like it is for a lot of the problems on leetcode. it consists of elements that have only one value and two pointers: one to the next element in the list, and one to the previous element in the list
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
#circular linked list
#circular singly linked list
#circular doubly linked list
