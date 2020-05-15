import unittest
from hypothesis import given
import hypothesis.strategies as st
from immutable import *


class TestMutableList(unittest.TestCase):
    def test_size(self):
        lst = UnrolledLinkList()
        self.assertEqual(lst.size(), 0)
        lst.add(0, 'm')
        self.assertEqual(lst.size(), 1)
        lst.add(1, 'n')
        self.assertEqual(lst.size(), 2)

    def test_to_list(self):
        self.assertEqual(UnrolledLinkList().to_list(), 0)
        lst = UnrolledLinkList()
        lst.add(0, 'm')
        self.assertEqual(lst.to_list(), ['m'])
        lst.add(1, 'n')
        self.assertEqual(lst.to_list(), ['m', 'n'])

    def test_from_list(self):
        test_data = [
            [],
            ['m'],
            ['m', 'n']
        ]
        for e in test_data:
            lst = UnrolledLinkList()
            lst.from_list(e)
            self.assertEqual(lst.to_list(), e)

    def test_map(self):
        lst = UnrolledLinkList()
        lst.map(str)
        self.assertEqual(lst.to_list(), [])
        lst = UnrolledLinkList()
        lst.from_list([1, 2, 3])
        lst.map(str)
        self.assertEqual(lst.to_list(), ["1", "2", "3"])

    def test_reduce(self):
        lst = UnrolledLinkList()
        self.assertEqual(lst.reduce(lambda stb, e1: stb + e1, 0), 0)
        # sum of list
        lst = UnrolledLinkList()
        lst.from_list([1, 2, 3])
        self.assertEqual(lst.reduce(lambda stb, e1: stb + e1, 0), 6)
        # size
        test_data = [
            [],
            ['m'],
            ['m', 'n']
        ]
        for e in test_data:
            lst = UnrolledLinkList()
            lst.from_list(e)
            self.assertEqual(lst.reduce(lambda stb, _: stb + 1, 0), lst.size())

    @given(st.lists(st.integers()))
    def test_from_list_to_list_equality(self, a):
        lst = UnrolledLinkList()
        lst.from_list(a)
        b = lst.to_list()
        self.assertEqual(a, b)

    @given(st.lists(st.integers()))
    def test_python_len_and_list_size_equality(self, a):
        lst = UnrolledLinkList()
        lst.from_list(a)
        self.assertEqual(lst.size(), len(a))

    @given(st.lists(st.integers()))
    def test_monoid_associativity(self, a, b, c):
        lst = UnrolledLinkList()
        lst1 = lst.from_list(a)
        lst2 = lst.from_list(b)
        lst3 = lst.from_list(c)
        test1 = lst.mconcat(lst.mconcat(lst1, lst2), lst3)
        test2 = lst.mconcat(lst1, lst.mconcat(lst2, lst3))
        self.assertEqual(test1, test2)

    @given(st.lists(st.integers()))
    def test_monoid_identity(self, lst):
        lst1 = UnrolledLinkList().from_list(lst)
        lst2 = UnrolledLinkList()
        lst_concat = UnrolledLinkList()
        self.assertEqual(UnrolledLinkList(lst_concat.mconcat((lst1, lst2.empty()))).to_list(), lst)
        self.assertEqual(UnrolledLinkList(lst_concat.mconcat(lst2.empty(), lst1)).to_list(), lst)

    def test_iter(self):
        x = [1, 2, 3]
        lst = UnrolledLinkList()
        lst.from_list(x)
        i = 0
        tmp = []
        for e in lst.root.items:
            i += 1
            if i > len(x):
                break
            tmp.append(e)
        self.assertEqual(x, tmp)
        self.assertEqual(lst.to_list(), tmp)

    def find(self):
        x = ['m', 'n', 'o']
        lst = UnrolledLinkList()
        lst.from_list(x)
        index = lst.find('n')
        self.assertEqual(0, index)

    def filter(self):
        def f(x1):
            res = x1 + 1
            return res

        x = [1, 2, 3]
        lst = UnrolledLinkList()
        lst.from_list(x)
        lst.filter(f)
        self.assertEqual([2, 3, 4], lst.to_list())

    if __name__ == '__main__':
        unittest.main()
