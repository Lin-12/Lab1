1.Title:
  Computational Process Organization Lab1,variant 1

2.List of group members:
  Name:Huang Yanlin student number:192050222 
  Name:Lin ningning student number:192050192

3.Laboratory work number:
  Lab1 variant 1

4.Description:
  variant 1: Unrolled linked list (you can use built-in list inside node).

5.Synopsis:
    ¢ñ)add a new element (lst.add(3), cons(lst, 3), extend(lst, 3)); 
    ¢ò)remove an element (lst.remove(3), remove(lst, 3));
    ¢ó)size (lst.size(), size(lst));
    ¢ô)conversion from and to python lists (lst.to_list(), lst.from_list([12, 99, 37]), from_list([12, 99, 37]));
    ¢õ)?nd element by speci?c predicate (lst.find(is_even_), );
    ¢ö)?lter data structure by speci?c predicate (lst.filter(is_even));
    ¢÷)map structure by speci?c function (lst.map(increment));
    ¢ø)reduce ¨C process structure elements to build a return value by speci?c functions (lst.reduce(sum));
    ¢ù)data structure should be a monoid and implement mempty and mconcat functions or methods;
    ¢ú)iterator: 
        for the mutable version in Python style [12, Chapter 7. Classes & Iterators]; 
        for the immutable version by closure [14], see example ahead.

6.Contribution summary for each group member (should be checkable by git log and git blame);:
    mutable&test_mutable:Lin ningning
    immutable&immutable_test:Huang Yanlin

7.Explanation of taken design decisions and analysis:
    Unrolled linked list is a kind of transformation or improvement of linked list. Each node of it is stored by an array. The capacity of node array is fixed. 1. Insert operation: insert the element after finding the position according to the subscript. If the current inserted node array is full, a new node is created, and half of the elements of the current node are moved to the array of the new node, and the element is inserted finally. 2. Delete: delete the element according to the subscript. A node after deleting an element may need its neighbors to merge. Unrolled linked list has the advantages of random access of array and efficient insertion and deletion of linked list.

8.Work demonstration (how to use developed software, how to test it), should be repeatable by an instructor by given command-line examples;
    ¢ñ)We write unrolled linked list file and test file on Pycharm.
    ¢ò)Use terminal to test the code. like 'python Immutable_test.py -v'and 'python test_mutable.py -v'

9.Conclusion:
  Mutable version used used list to create a unrolled linked list.In immutable version,we create a new unrolled linked list before modifying each unrolled linked list, and do not change the original linked list.This Lab makes us to realize unrolled linked list and  mutable/immutable version 