class Node(object):
    def __init__(self, max_capacity=8):
        self.capacity = max_capacity
        self.next = None
        self.prev = None
        self.items = [None] * max_capacity
        self.value = None
        self.size = 0

class UnrolledLinkList(object):
    def __init__(self, root=None):
        self.sizeAll = 0
        self.root = root

    def __iter__(self):
        return UnrolledLinkList()

    def __next__(self):
        if self.root is None:
            raise StopIteration
        curNode = self.root
        for i in range(0, curNode.size):
            temp = curNode.elements[i]
            return temp
        self.root = curNode.next

    # return the sizeALl about the UnrolledLinkList
    def size(self):
        return self.sizeAll

    # Insert new element in UnrolledLinkList by index
    def add(self, index, e):

        # When the index is illegal, return directly
        if index < 0 or index > self.sizeAll:
            return
        curNode = self.root
        while index >= curNode.size:
            if index == curNode.size:
                break
            index -= curNode.size
            curNode = curNode.next
        # If the capacity of the node to be inserted is full, to create a new node
        if curNode.size == curNode.capacity:
            node = Node()
            next_node = curNode.next
            curNode.next = node
            node.next = next_node
            move_idx = curNode.size // 2
            for i in range(move_idx, curNode.size):
                node.items[i - move_idx] = curNode.items[i]
                curNode.items[i] = None
                curNode.size -= 1
                node.size += 1

            if index >= move_idx:
                index -= move_idx
                curNode = node

        for i in range(curNode.size - 1, index - 1, -1):
            curNode.items[i + 1] = curNode.items[i]
        curNode.items[index] = e
        # Number of corresponding nodes plus 1
        curNode.size += 1
        self.sizeAll += 1

    # Remove an element in UnrolledLinkList by index
    def remove(self, index):
        if index < 0 or index > self.sizeAll:
            return

        curNode = self.root
        # Determine the specific node location of the element to delete
        while index >= curNode.size - 1:
            if index == curNode.size - 1:
                break
            index -= curNode.size
            curNode = curNode.next
        for i in range(index, curNode - 1, 1):
            curNode.items[i] = curNode.items[i + 1]
        curNode.items[curNode.size - 1] = None
        # Number of corresponding nodes minus 1
        curNode.size -= 1
        if curNode.capacity >= curNode.size + curNode.next.size and curNode.next.capacity != -1:
            nextNode = curNode.next
            for i in range(0, nextNode.size):
                curNode.items[curNode.size + 1] = nextNode.items[i]
            curNode.size += nextNode.size
            curNode.next = nextNode.next
            # Number of corresponding nodes minus 1
        self.sizeAll -= 1

    # make UnrolledLinkList be a list
    def to_list(self):
        res = []
        curNode = self.root
        while curNode is not None:
            for i in range(0, curNode.size):
                res.append(curNode.items[i])
            curNode = curNode.next
        return res

    # Make a list to be  UnrolledLinkList
    def from_list(self, lst):
        if len(lst) == 0:
            self.root = None
            return
        for e in reversed(lst):
            self.add(0, e)

    # Find the specified data in the UnrolledLinkList
    def find(self, data):
        curNode = self.root
        count = 0
        while curNode is not None:
            for i in range(0, curNode.size):
                if data == curNode.items[i]:
                    count += 1
                    index = count - 1
                    return index
            return -1

    # Utilize f to filter the UnrolledLinkList
    def filter(self, f):
        curNode = self.root
        for i in range(0, curNode.size):
            curNode.items[i] = f(curNode.items[i])
        return self.to_list()

    # Utilize the f to map the UnrolledLinkList
    def map(self, f):
        curNode = self.root
        while curNode is not None:
            for i in range(0, curNode.size):
                curNode.items[i] = f(curNode.items[i])
            curNode = curNode.next

    # process structure elements to build a return value by specific functions
    def reduce(self, f, initial_state):
        state = initial_state
        curNode = self.root
        while curNode is not None:
            for i in range(0, curNode.size):
                state = f(state, curNode.items[i])
            curNode = curNode.next
        return state

    # Make it empty and return None
    def empty(self):
        return None

    # Combine two UnrolledLinkList
    def mconcat(self, lst1, lst2):
        temp = self.root
        if lst1 is not None:
            while temp.next is not None:
                temp = temp.next
            temp.next = lst1.root
        if lst2 is not None:
            while temp.next is not None:
                temp = temp.next
            temp.next = lst2.root

