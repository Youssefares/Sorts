#python stuff
import unittest
import time
import random

#our stuff
from AVL.BST import BST
from Merge.merge_sort import merge_sort
from is_sorted import is_sorted
from min_heap_invariant import is_min_heap
from PriorityQ.min_heap import MinHeap

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

    #testing BST operations
    def test_tree_min_is_correct(self):
        result = self.tree.min()
        self.assertEqual(result, self.min)


    def test_tree_max_is_correct(self):
        result = self.tree.max()
        self.assertEqual(result, self.max)

    def test_tree_find_works(self):
        self.assertTrue(self.tree.find(self.arr[23]) is not None)
        self.assertTrue(self.tree.find(2000) is None)

    # def test_tree_delete_works(self):
    #     doomed = self.arr[13]
    #     self.assertTrue(self.tree.find(doomed) is not None)
    #     self.assertTrue(self.tree.delete(doomed))
    #     self.assertTrue(self.tree.find(doomed) is None)





class isSortedTestCase(unittest.TestCase):
    def setUp(self):
        self.arr = random.sample(range(-523000,14252000),1000000)


    def test_is_sorted_works(self):
        self.assertFalse(is_sorted(self.arr))
        self.assertTrue(is_sorted(sorted(self.arr)))


class MergeSortTestCase(unittest.TestCase):
    def setUp(self):
        self.N = pow(2,20)
        self.arr = random.sample(range(-523000,14252000),self.N)

    def test_merge_sort_works(self):
        start = time.time()
        merge_sort(self.arr)
        end = time.time()
        self.assertTrue(is_sorted(self.arr))
        print("MergeSort Time: {0} for N = {1}".format(end-start, self.N))


class HeapSortTestCase(unittest.TestCase):
    def setUp(self):
        self.N = pow(2,20)
        self.arr = random.sample(range(-523000, 14252000), self.N)

    def test_build_max_heap_works(self):
        h = MinHeap(self.arr)
        self.assertTrue(is_min_heap(h.arr))


unittest.main()
