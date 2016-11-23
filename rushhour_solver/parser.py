# -*- coding: utf-8 -*-

"""
Module: rushhour_solver
File: parser.py
Creator: Nick Geense
Date: 23-11-2016

Rush Hour file parser for analysing board text representations.

Rush Hour Parser should receive a valid filename
and after all checks have passed return a Board object.

"""


import os.path


class RushHourParser(object):

    def __init__(self, filename):
        self.filename = None
        self.board = None
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
        return self.board




