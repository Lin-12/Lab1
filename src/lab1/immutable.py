class Node:
    def __init__(self, lst, tail, max_capacity=8):
        self.items = [None] * 8
        self.size = 0
        for i in range(0, len(lst)):
            self.items[i] = lst[i]
            self.size += 1
        self.cap = 8
        self.next = tail
        self.cap = max_capacity

# return the size about UnrolledLinkList
def size(lst):
    if lst is None:
        return 0
    else:
        return lst.size + size(lst.next)


# Add a lst in the head.When the number of elements is more than 8,the part more than 8 will cons in a new node.
def cons(lst, tail=None):
    if len(lst) > 8:
        return cons(lst[8:], cons(lst[:8], tail))
    return Node(lst, tail)


# find the element in the UnrolledLinkList and remove it
def remove(lst, element):
    assert lst is not None, "element should be in list"
    while lst is not None:
        for i in range(0, lst.size):
            if lst.items[i] == element:
                for t in range(i, lst.size):
                    lst.items[t] = lst.items[t + 1]
                lst.size -= 1
        return lst


# return the first element in the first node
def head(lst):
    assert type(lst) is Node
    return lst.items[0]


def tail(lst):
    assert type(lst) is Node
    return lst.next


# make UnrolledLinkList be a list
def to_list(lst):
    if lst is None:
        L = []
        return L
    else:
        a = lst
        cur = lst
        count = 1
        while cur.next is not None:
            count += 1
            cur = cur.next
        L = []
        while cur != a:
            if cur.size == 0:
                cur = a
                for e in range(0, count - 2):
                    cur = cur.next
                count -= 1
            for i in range(0, cur.size, 1):
                L.append(cur.items[i])
                if i == cur.size - 1:
                    cur = a
                    for e in range(0, count - 2):
                        cur = cur.next
                    count -= 1
        if cur == a:
            for i in range(0, cur.size, 1):
                L.append(cur.items[i])
        return L


# Define the empty UnrolledLinkList
def empty():
    return None


# lst1 and lst2 are UnrolledLinkList
def mconcat(lst1, lst2):
    if lst1 is None:
        return lst2
    tmp = lst1
    while tmp.next is not None:
        tmp = tmp.next
    tmp.next = lst2
    return lst1


# Make a list into a UnrolledLinkList
def from_list(lst):
    if len(lst) == 0:
        return cons(lst)
    cur = None
    j = 0
    for i in range(0, len(lst), 8):
        tmp = []
        if len(lst) / 8 >= 1:
            if j < int(len(lst) / 8):
                for t in range(i, i + 8):
                    tmp.append(lst[t])
                cur = cons(tmp, cur)
                j += 1
            else:
                for t in range(i, i + len(lst) % 8):
                    tmp.append(lst[t])
                cur = cons(tmp, cur)
                j += 1
        else:
            for t in range(j, j + len(lst) % 8):
                tmp.append(lst[t])
            cur = cons(tmp, cur)
    return cur


# The function of filter
def filter(lst, f):
    cur = lst
    for i in range(0, cur.size):
        cur.items[i] = f(cur.items[i])
    return cur


# The function of map,
# Utilize the f to map the UnrolledLinkList
def map(lst, f):
    cur = lst
    while cur is not None:
        for i in range(0, cur.size):
            cur.items[i] = f(cur.items[i])
        cur = cur.next
    return lst


# The function of reduce
# process structure elements to build a return value by specific functions
def reduce(lst, fun, initial_state):
    state = initial_state
    cur = lst
    while cur is not None:
        for i in range(0, cur.size):
            state = fun(state, cur.items[i])
        cur = cur.next
    return state


# The function about iterator
def iterator(lst):
    cur = lst
    tmp = []

    def foo():
        nonlocal cur
        if cur is None:
            raise StopIteration
        for i in range(0, cur.size):
            if cur.items[i] is None:
                break
            tmp.append(cur.items[i])
        cur = cur.next
        return tmp

    return foo()


# The function to append elements
def append(l, lst):
    if lst is None:
        return l
    cur = l
    len1 = cur.size
    for i in range(0, len(lst)):
        # When cur node is full,use cons to create a new one
        if cur.size == 8:
            cur = cons([], cur)
            len1 = 0
        cur.items[len1] = lst[i]
        cur.size += 1
        len1 += 1
    return cur
