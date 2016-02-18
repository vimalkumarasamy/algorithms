import sys
import os.path
import unittest


sys.path.append(os.path.join(os.path.abspath(os.pardir), "trees"))
from trees.binary_tree import BinaryTree


class TestBinaryTree(unittest.TestCase):
    def setUp(self):
        self.root = BinaryTree(0)

    def tearDown(self):
        self.root = None

    def test_init_root(self):
        self.assertEqual(None, self.root.parent)

    def test_add_right(self):
        self.root.value = 5
        self.root.add(10)
        self.assertEqual(10, self.root.right.value)

    def test_add_left(self):
        self.root.value = 5
        self.root.add(1)
        self.assertEqual(1, self.root.left.value)

    def test_add_right_parent(self):
        self.root.value = 5
        self.root.add(10)
        self.assertEqual(self.root, self.root.right.parent)

    def test_add_left_parent(self):
        self.root.value = 5
        self.root.add(1)
        self.assertEqual(self.root, self.root.left.parent)

    def test_add_two_right(self):
        self.root.value = 5
        self.root.add(10)
        self.root.add(15)
        self.assertEqual(10, self.root.right.value)
        self.assertEqual(15, self.root.right.right.value)

    def test_add_two_left(self):
        self.root.value = 5
        self.root.add(3)
        self.root.add(1)
        self.assertEqual(3, self.root.left.value)
        self.assertEqual(1, self.root.left.left.value)

    def test_add_two_right_one_nested_left(self):
        self.root.value = 5
        self.root.add(10)
        self.root.add(15)
        self.root.add(13)
        self.assertEqual(13, self.root.right.right.left.value)

    def test_add_two_left_one_nested_right(self):
        self.root.value = 15
        self.root.add(10)
        self.root.add(3)
        self.root.add(7)
        self.assertEqual(7, self.root.left.left.right.value)

    def test_search_for_simple_right(self):
        self.root.value = 10
        self.root.add(15)
        self.assertEqual(15, self.root.search_for_value(15).value)

    def test_search_for_simple_left(self):
            self.root.value = 10
            self.root.add(5)
            self.assertEqual(5, self.root.search_for_value(5).value)

    def test_search_two_left_one_nested_right(self):
        self.root.value = 15
        self.root.add(10)
        self.root.add(3)
        self.root.add(7)
        self.assertEqual(3, self.root.search_for_value(3).value)

    def test_delete_left_leaf(self):
        self.root.value = 10
        self.root.add(5)
        self.root.delete(5)
        self.assertRaises(ValueError, self.root.search_for_value, 5)

    def test_delete_right_leaf(self):
        self.root.value = 10
        self.root.add(15)
        self.root.delete(15)
        self.assertRaises(ValueError, self.root.search_for_value, 15)