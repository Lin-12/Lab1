#Laboratory 1
#List of group members:
Name:Huang Yanlin   student number:192050222
Name:Lin ningning   student number:192050192

#Laboratory work number:
variant1

#variant description:
Unrolled linked list is a kind of transformation or improvement of linked list. Each node of it is stored by an array. The capacity of node array is fixed. 1. Insert operation: insert the element after finding the position according to the subscript. If the current inserted node array is full, a new node is created, and half of the elements of the current node are moved to the array of the new node, and the element is inserted finally. 2. Delete: delete the element according to the subscript. A node after deleting an element may need its neighbors to merge. Unrolled linked list has the advantages of random access of array and efficient insertion and deletion of linked list.

#synopsis:
mutable version used used list to create a unrolled linked list

In immutable version,we create a new unrolled linked list before modifying each unrolled linked list, and do not change the original linked list

#contribution summary for each group member:

mutable&mutable_test:Lin ningning

immutable&immutable_test:Huang Yanlin
