class Node(object):
    def __init__(self, max_capacity=16):
        self.capacity = max_capacity
        self.next = None
        self.prev = None
        self.items = [None]*max_capacity
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

    def size(self):
        return self.sizeAll

    def add(self, index, e):
        if index < 0 or index > self.sizeAll:
            return
        l1 = UnrolledLinkList()
        l1 = self
        curNode = l1.root
        while index >= curNode.size:
            if index == curNode.size:
                break
            index -= curNode.size
            curNode = curNode.next
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
        curNode.size += 1
        l1.sizeAll += 1

    def remove(self, index):
        if index < 0 or index > self.sizeAll:
            return
        l1 = UnrolledLinkList(Node())
        l1 = self
        curNode = l1.root
        while index >= curNode.size - 1:
            if index == curNode.size - 1:
                break
            index -= curNode.size
            curNode = curNode.next
        for i in range(index, curNode - 1, 1):
            curNode.items[i] = curNode.items[i + 1]
        curNode.items[curNode.size - 1] = None
        curNode.size -= 1

        if curNode.capacity >= curNode.size + curNode.next.size and curNode.next.capacity != -1:
            nextNode = curNode.next
            for i in range(0, nextNode.size):
                curNode.items[curNode.size + 1] = nextNode.items[i]
            curNode.size += nextNode.size
            curNode.next = nextNode.next
        l1.sizeAll -= 1

    def to_list(self):
        res = []
        l1 = UnrolledLinkList(Node())
        l1 = self
        curNode = l1.root
        while curNode is not None:
            for i in range(0, curNode.size):
                res.append(curNode.items[i])
            curNode = curNode.next
        return res

    def from_list(self, lst):
        l1 = UnrolledLinkList(Node())
        l1 = self
        if len(lst) == 0:
            l1.root = None
            return
        for e in reversed(lst):
            l1.add(0, e)

    def find(self, data):
        l1 = UnrolledLinkList(Node())
        l1 = self
        curNode = l1.root
        count = 0
        while curNode is not None:
            for i in range(0, curNode.size):
                if data == curNode.items[i]:
                    count += 1
                    index = count - 1
                    return index
            return -1

    def filter(self, f):
        l1 = UnrolledLinkList(Node())
        l1 = self
        curNode = l1.root
        for i in range(0, curNode.size):
            curNode.items[i] = f(curNode.items[i])
        return l1.to_list()

    def map(self, f):
        curNode = self.root
        while curNode is not None:
            for i in range(0, curNode.size):
                curNode.items[i] = f(curNode.items[i])
            curNode = curNode.next

    def reduce(self, f, initial_state):
        l1 = UnrolledLinkList(Node())
        l1 = self
        state = initial_state
        curNode = l1.root
        while curNode is not None:
            for i in range(0, curNode.size):
                state = f(state, curNode.items[i])
            curNode = curNode.next
        return state

    def empty(self):
        return None

    def mconcat(self, lst1, lst2):
        l1 = UnrolledLinkList(Node())
        l1 = self
        temp = l1.root
        if lst1 is not None:
            while temp.next is not None:
                temp = temp.next
            temp.next = lst1.root
        if lst2 is not None:
            while temp.next is not None:
                temp = temp.next
            temp.next = lst2.root
