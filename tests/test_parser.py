# -*- coding: utf-8 -*-

"""
Module: tests
File: test_parser.py
Creator: Nick Geense
Date: 23-11-2016

Unit Tests for Rush Hour file parser.

"""

import os.path
import unittest

from rushhour_solver.parser import RushHourParser
from rushhour_solver.game_components import Car


class TestRushHourParser(unittest.TestCase):

    def setUp(self):
        root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.valid_puzzle = os.path.join(root_dir, 'tests', 'puzzle_valid.txt')
        self.invalid_puzzle = os.path.join(root_dir, 'tests', 'puzzle_invalid.txt')

    def test_rushhour_parser_init(self):
        parser = RushHourParser(self.valid_puzzle)
        self.assertEqual(parser.filename, self.valid_puzzle)

    def test_rushhour_set_valid_filename(self):
        with self.assertRaises(ValueError):
            parser = RushHourParser('not/a/real/path')

    def test_parser_finds_vehicles(self):
        parser = RushHourParser(self.valid_puzzle)
        test_board = [['.', '.', '.', '.', 'A', 'A']]
        vehicles = parser._find_vehicles(test_board)
        self.assertIsInstance(vehicles[0], Car)
        self.assertEqual(vehicles[0].id, 'A')

