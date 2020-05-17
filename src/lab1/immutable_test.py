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
        self.assertEqual(UnrolledLinkList().to_list(), [])
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

    def test_add_to_head(self):
        lst = UnrolledLinkList()
        self.assertEqual(lst.to_list(), [])
        lst.add(0, 'a')
        self.assertEqual(lst.to_list(), ['a'])
        lst.add(0, 'b')
        self.assertEqual(lst.to_list(), ['b', 'a'])

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

    @given(a=st.lists(st.integers()), b=st.lists(st.integers()), c=st.lists(st.integers()))
    def test_monoid_associativity(self, a, b, c):
        a = []
        b = []
        c = []
        lst1 = UnrolledLinkList()
        lst2 = UnrolledLinkList()
        lst3 = UnrolledLinkList()
        lst1.from_list(a)
        lst2.from_list(b)
        lst3.from_list(c)
        lst_test1 = UnrolledLinkList()
        lst_test2 = UnrolledLinkList()
        lst_test2.mconcat(lst1, lst2)
        lst_test1.mconcat(lst_test2, lst3)
        lst1 = UnrolledLinkList()
        lst2 = UnrolledLinkList()
        lst3 = UnrolledLinkList()
        lst1.from_list(a)
        lst2.from_list(b)
        lst3.from_list(c)
        lst_test3 = UnrolledLinkList()
        lst_test2 = UnrolledLinkList()
        lst_test2.mconcat(lst2, lst3)
        lst_test3.mconcat(lst1, lst_test2)

        lst_1 = lst_test1.to_list()
        lst_2 = lst_test2.to_list()
        self.assertEqual(lst_1, lst_2)

    @given(st.lists(st.integers()))
    def test_monoid_identity(self, a):
        a = []
        lst = UnrolledLinkList()
        lst.from_list(a)
        lst1 = UnrolledLinkList()
        lst_concat = UnrolledLinkList()
        lst_concat.mconcat(lst, lst1.empty())
        b = lst_concat.to_list()
        self.assertEqual(b, a)
        lst_concat = UnrolledLinkList()
        lst_concat.mconcat(lst1.empty(), lst)
        b = lst_concat.to_list()
        self.assertEqual(b, a)

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
