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
import logging

from rushhour_solver.game_components import Board, RedCar, Car, Truck

Lumberjack = logging.getLogger(__name__)


class RushHourParser(object):

    def __init__(self, filename):
        self.filename = None
        self.board = None
        self.set_filename(filename)
        self.start_parser()

    def start_parser(self):
        file_content = self._read_file(self.filename)
        content_dimensions_valid = self._check_dimensions(file_content)

        if content_dimensions_valid:
            board = self._rasterize_file_content(file_content)
        else:
            raise ValueError('File Content not valid: Dimensions do not match 6x6 tiles.')

        vehicles = self._find_vehicles(board)
        print(vehicles)

    def set_filename(self, filename):
        """Filename should be a path"""

        if os.path.exists(filename):
            self.filename = filename
            # TODO - Restart function call when filename changes
        else:
            raise ValueError('File path does not exist.')

    def get_filename(self):
        return self.filename

    def _read_file(self, filename):
        with open(filename, 'r') as f:
            file_content = [line.rstrip('\n') for line in f]
            return file_content

    def _check_dimensions(self, file_content):
        if len(file_content) > 6:
            return False

        for line in file_content:
            if len(line) > 6:
                return False

        return True

    def _rasterize_file_content(self, file_content):
        board = []
        for line in file_content:
            board.append([char for char in line])
        return board

    def _find_vehicles(self, board):
        vehicle_names = []
        vehicles = []
        for row in board:
            for cell in row:
                if cell not in vehicle_names and cell != '.':
                    id = cell
                    vehicle_names.append(id)
                    print('found car with id: ', id)
                    x = board.index(row)
                    y = row.index(cell)
                    print('coordinates are: ', x, ', ', y)
                    length = 0

                    if x + 1 < len(board) and board[x + 1][y] == cell:
                        orientation = 'V'
                        print('found orientation V')
                        if x + 2 < len(board) and board[x + 2][y] == cell:
                            length = 3
                        else:
                            length = 2

                    elif y + 1 < len(row) and row[y + 1] == cell:
                        orientation = 'H'
                        print('found orientation H')
                        if y + 2 < len(row) and row[y + 2] == cell:
                            length = 3
                        else:
                            length = 2

                    if length == 2:
                        if id == 'r':
                            vehicles.append(RedCar(id, x, y, orientation))
                        else:
                            vehicles.append(Car(id, x, y, orientation))
                    elif length == 3:
                        if id != 'r':
                            vehicles.append(Truck(id, x, y, orientation))
                    elif length == 0:
                        Lumberjack.warning('Found a piece of information that does not behave like a vehicle!')
        return vehicles

    def get_board(self):
        return self.board
