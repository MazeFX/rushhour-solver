# -*- coding: utf-8 -*-

"""
Module: tests
File: test_solver.py
Creator: Nick Geense
Date: 23-11-2016

Unit Tests for Rush Hour Solver.

"""

import os.path
import unittest

from rushhour_solver.solver import RushHourSolver
from rushhour_solver.game_components import Board, Car, RedCar, Truck


class TestRushHourSolver(unittest.TestCase):

    def setUp(self):
        board = [['.', '.', '.', '.', 'A', 'A'],
                 ['.', '.', 'B', 'B', 'C', 'C'],
                 ['r', 'r', '.', '.', 'E', 'F'],
                 ['G', 'G', 'H', 'H', 'E', 'F'],
                 ['.', '.', '.', 'I', 'E', 'F'],
                 ['.', '.', '.', 'I', 'J', 'J']]

        vehicles = [Car('A', 4, 0, 'H'),
                    Car('B', 2, 1, 'H'),
                    Car('C', 4, 1, 'H'),
                    RedCar('r', 0, 2, 'H'),
                    Truck('E', 4, 2, 'V'),
                    Truck('F', 5, 2, 'V'),
                    Car('G', 0, 3, 'H'),
                    Car('H', 2, 3, 'H'),
                    Car('I', 3, 4, 'V'),
                    Car('J', 4, 5, 'H')]

        self.test_board = Board()
        self.test_board.set_board(board)
        self.test_board.set_vehicles(vehicles)

    def test_rushhour_solver_init(self):
        solver = RushHourSolver(self.test_board)
        self.assertEqual(solver.start_board, self.test_board)
