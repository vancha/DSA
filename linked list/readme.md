# Linked List

## Implementation
The linked list as a data structure exists in a variety of types. What all variations of this linked list have in common, is that they are a linear data structure, where the elements are not stored in congiguous memory locations. Elements in the linked lists  use pointers to "link" themselves to other elements.Here I'll list the different types of linked lists and what their properties are. To learn how these data structures can be implemented and used, read the linkedlists.py file.

### singly linked list
A singly linked list consists of nodes where each node has a data field and a single reference (pointer) to the next node in the list.
### doubly linked list
A doubly linked list consists of nodes where each node has a data field and two references (pointers),one to the next node and one to the previous node in the list.
### circular linked list
A circular linked list consists of nodes where each node has a data field and a single reference (pointer) to the next node in the list, the difference between a circular linked list and a regular linked list, is that the last element points back to the first element.
### circular singly linked list
A circular singly linked list is a the same as a singly linked list but the last elements pointer to the next value points back to it's first element
### circular doubly linked list
A circular doubly linked list is a the same as a doubly linked list but the last elements pointer to the next value points back to the first element in the list, and the first element in the lists has it's previous node set to be the last element in the list
