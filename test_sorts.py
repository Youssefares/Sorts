import unittest
import random
from AVL.BST import BST
from is_sorted import is_sorted

class BSTTestCase(unittest.TestCase):

    #get random numbers, their min & max, and insert them in the BST.
    def setUp(self):
        self.tree = BST()
        self.arr = random.sample(range(-1000,1000),30)
        self.min = self.max = self.arr[0]
        for a in self.arr:
            self.tree.insert(a)
            if a < self.min:
                self.min = a
            elif a > self.max:
                self.max = a

    def test_tree_min_is_correct(self):
        result = self.tree.min()
        self.assertEqual(result, self.min)


    def test_tree_max_is_correct(self):
        result = self.tree.max()
        self.assertEqual(result, self.max)


class isSortedTestCase(unittest.TestCase):
    def setUp(self):
        self.arr = random.sample(range(-1000,1000),100)


    def test_is_sorted_works(self):
        self.assertFalse(is_sorted(self.arr))
        self.assertTrue(sorted(self.arr))





unittest.main()
