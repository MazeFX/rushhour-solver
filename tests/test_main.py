# -*- coding: utf-8 -*-

"""
Module: tests
File: test_main.py
Creator: Nick Geense
Date: 23-11-2016

Unit Tests for Main Rush Hour Program.

"""


import os.path
import unittest

from rushhour_solver.main import RushHour


class TestRushHour(unittest.TestCase):

    def setUp(self):
        root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.valid_puzzle = os.path.join(root_dir, 'tests', 'puzzle_valid.txt')
        self.invalid_puzzle = os.path.join(root_dir, 'tests', 'puzzle_invalid.txt')

    def test_rushhour_init(self):
        rushhour = RushHour(self.valid_puzzle)
        self.assertEqual(rushhour.filename, self.valid_puzzle)


if __name__ == '__main__':
    unittest.main()
