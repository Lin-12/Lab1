import unittest
from hypothesis import given, settings
import hypothesis.strategies as st
from immutable import *


class TestImmutableList(unittest.TestCase):
    # test function of size
    def test_size(self):
        self.assertEqual(size(cons('m', None)), 1)
        self.assertEqual(size(cons('m', cons('n', None))), 2)
        lst = [1, 2]
        self.assertEqual(size(cons(lst, None)), 2)

    # test function of head
    def test_head(self):
        self.assertEqual(head(cons('m', cons('n', None))), 'm')
        self.assertEqual(head(cons('m', None)), 'm')

    # test function of tail
    def test_tail(self):
        self.assertEqual(to_list(tail(cons('m', cons('n', None)))), ['n'])

    # test function of to_list
    def test_to_list(self):
        self.assertEqual(to_list(None), [])
        self.assertEqual(to_list(cons('m', None)), ['m'])
        self.assertEqual(to_list(cons('n', cons('m', None))), ['m', 'n'])

    # test function of from_list
    def test_from_list(self):
        test_data = [
            [],
            ['m'],
            ['m', 'n']
        ]
        for e in test_data:
            b = from_list(e)
            a = to_list(b)
            self.assertEqual(a, e)

    # test function of map
    def test_map(self):
        lst = from_list([])
        lst = map(lst, str)
        lst = to_list(lst)
        self.assertEqual(lst, [])
        lst1 = from_list([1, 2, 3])
        lst1 = map(lst1, str)
        lst1 = to_list(lst1)
        self.assertEqual(lst1, ["1", "2", "3"])

    # test function of reduce
    def test_reduce(self):
        # sum of empty list
        lst = Node([], None)
        lst = reduce(lst, lambda st, e: st + e, 0)
        self.assertEqual(lst, 0)
        lst = from_list([1, 2, 3])
        lst = reduce(lst, lambda st, e: st + e, 0)
        self.assertEqual(lst, 6)
        test_data = [
            [],
            ['m'],
            ['m', 'n']
        ]
        for e in test_data:
            lst1 = from_list(e)
            lst = reduce(lst1, lambda st, _: st + 1, 0)
            self.assertEqual(lst, lst1.size)

    # test function of cons
    def test_cons(self):
        self.assertEqual(to_list(cons(['m', 'n', 'o', 'p'], None)), to_list(Node(['m', 'n', 'o', 'p'], None)))
        self.assertEqual(cons('m', cons('n', None)).items, Node('m', Node('n', None)).items)

    # test function of remove
    def test_remove(self):
        lst = ['m', 'n']
        self.assertEqual(to_list(remove(cons(lst, None), 'n')), to_list(cons('m', None)))
        lst = ['m', 'n', 'p']
        self.assertEqual(to_list(remove(cons(lst, None), 'n')), to_list(cons(['m', 'p'], None)))

    @given(st.lists(st.integers()))
    def test_from_list_to_list_equality(self, a):
        l1 = from_list(a)
        l2 = to_list(l1)
        self.assertEqual(l2, a)

    @given(st.lists(st.integers()))
    def test_monoid_identity(self, lst):
        l1 = from_list(lst)
        self.assertEqual(mconcat(empty(), l1), l1)
        self.assertEqual(mconcat(l1, empty()), l1)

    @given(st.lists(st.integers()), st.lists(st.integers()), st.lists(st.integers()))
    def test_monoid_associativity(self, lst1, lst2, lst3):

        l1 = from_list(lst1)
        l2 = from_list(lst2)
        l3 = from_list(lst3)
        m = mconcat(mconcat(l1, l2), l3)

        l1 = from_list(lst1)
        l2 = from_list(lst2)
        l3 = from_list(lst3)
        n = mconcat(l1, mconcat(l2, l3))
        self.assertEqual(to_list(m), to_list(n))

    # test function of filter
    def test_filter(self):
        def fun(_ze):
            res = _ze + 1
            return res
        _ze = [1, 2, 3]
        lst = from_list(_ze)
        lst = filter(lst, fun)
        self.assertEqual([2, 3, 4], to_list(lst))

    def test_iter(self):
        x = [1, 2, 3]
        lst = from_list(x)
        tmp = iterator(lst)
        self.assertEqual(x, tmp)

    # test function of append
    def test_append(self):
        L = cons([], None)
        lst = ['a', 'b']
        l1 = to_list(append(L, lst))
        self.assertEqual(l1, lst)
        lst2 = ['m', 'n']
        l2 = to_list(append(L, lst2))
        lst = ['a', 'b', 'm', 'n']
        self.assertEqual(l2, lst)


if __name__ == '__main__':
    unittest.main()