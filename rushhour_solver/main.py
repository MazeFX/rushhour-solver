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


class RushHour(object):
    """
    Main Rush Hour object.

    Needs a filename as input along with possible kwargs.


    """

    def __init__(self, filename, **kwargs):
        self.filename = None
        self.set_filename(filename)
        self._start_solving()

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
        return parser.get_board()

    def _start_solving(self):
        start_board = self.get_board()
