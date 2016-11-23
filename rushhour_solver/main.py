# -*- coding: utf-8 -*-

"""
Module: rushhour_solver
File: main.py
Creator: Nick Geense
Date: 23-11-2016

Main controller for rushhour-solver components.

To supply an uniform contruct for interfacing.

"""


import os.path

from rushhour_solver.parser import RushHourParser
from rushhour_solver.solver import RushHourSolver
from rushhour_solver.painter import RushHourPainter


class RushHour(object):
    """
    Main Rush Hour object.

    Needs a filename as input along with possible kwargs.


    """

    def __init__(self, filename, **kwargs):
        self.filename = None
        self.solution = None
        self.set_filename(filename)

    def set_filename(self, filename):
        """Filename should be a path"""

        if os.path.exists(filename):
            self.filename = filename
            # TODO - Restart function call when filename changes
        else:
            raise ValueError('File path does not exist.')

    def get_filename(self):
        return self.filename

    def get_board(self):
        parser = RushHourParser(self.filename)
        parser.set_filename(self.filename)
        parser.start_parser()
        return parser.get_board()

    def get_solution(self):
        self.solution = self._start_solving()
        return self.solution

    def _get_solution(self, start_board):
        solver = RushHourSolver(start_board)
        solution = solver.start_solving()
        return solution

    def _start_solving(self):
        start_board = self.get_board()
        solution = self._get_solution(start_board)
        return solution

if __name__ == '__main__':
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filename = os.path.join(root_dir, 'puzzles', 'puzzle_default.txt')
    rushhour = RushHour(filename)
    start_board = rushhour.get_board()
    print(start_board)
    solution = rushhour._get_solution(start_board)
    print(len(str(solution)))
    painter = RushHourPainter()
    painter.print_solution(solution)
