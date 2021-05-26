#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    """ Function to make test normal integers """

    def test_max_integer(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([10, 2, 30, 4]), 30)
        self.assertEqual(max_integer([2, 3, 5, 1]), 5)

    """ Function to make test float values """

    def test_float(self):
        self.assertEqual(max_integer([1.0, 2.0, 3.0, 4.0]), 4.0)
        self.assertEqual(max_integer([10.0, 2.0, 60.0, 4.0]), 60.0)
        self.assertEqual(max_integer([2.0, 3.0, 5.0, 1.0]), 5.0)

    """ Function to make test negatives values """

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-10, -2, -30, -4]), -2)
        self.assertEqual(max_integer([-2, -3, -5, -1]), -1)

    """ Function to make test float values """

    def test_mixed(self):
        self.assertEqual(max_integer([-1, 2.0, 40, -69]), 40)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer("Python"), 'y')

    """ Function to get  raise message errors """

    def test_raise_messages(self):
        self.assertRaises(TypeError, max_integer, [98, '98'])
        self.assertRaises(TypeError, max_integer, ['98', 25, -3, 2.6])
        self.assertRaises(TypeError, max_integer, None)
