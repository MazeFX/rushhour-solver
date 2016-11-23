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
from unittest.mock import patch, MagicMock

from rushhour_solver.main import RushHour
from rushhour_solver.game_components import Board
from rushhour_solver.parser import RushHourParser


class TestRushHour(unittest.TestCase):

    def setUp(self):
        root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.valid_puzzle = os.path.join(root_dir, 'tests', 'puzzle_valid.txt')
        self.invalid_puzzle = os.path.join(root_dir, 'tests', 'puzzle_invalid.txt')

    def test_rushhour_init(self):
        rushhour = RushHour(self.valid_puzzle)
        self.assertEqual(rushhour.filename, self.valid_puzzle)

    def test_rushhour_set_valid_filename(self):
        with self.assertRaises(ValueError):
            rushhour = RushHour('not/a/real/path')

    def test_rushhour_get_board_returns_board(self):
        with patch.object(RushHourParser, 'get_board', return_value=Board()) as mock_method:
            rushhour = RushHour(self.valid_puzzle)
            board = rushhour.get_board()
            self.assertIsInstance(board, Board)


if __name__ == '__main__':
    unittest.main()
