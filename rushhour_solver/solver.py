# -*- coding: utf-8 -*-

"""
Module: rushhour_solver
File: solver.py
Creator: Nick Geense
Date: 23-11-2016

Rush Hour solver which will return a solution based
on a provided start board.

"""


import os.path
import logging
from collections import deque

from rushhour_solver.game_components import Board, RedCar, Car, Truck

Lumberjack = logging.getLogger(__name__)


class RushHourSolver(object):

    def __init__(self, start_board):
        self.start_board = start_board

    def set_start_board(self, start_board):
        self.start_board = start_board

    def get_start_board(self):
        return self.start_board

    def start_solving(self, max_steps=30):
        """
        Finding a solution using the Breadth first method.
        Create a list of all possible moves based on a starting
        board.

        Default will search till 25 steps.

        Will return a solution in the form of a list of steps.
        """
        start_board = self.get_start_board()
        visited = set()

        queue = deque()
        queue.appendleft((start_board, tuple()))
        while len(queue) != 0:
            board, steps = queue.pop()
            new_step = steps + tuple([board])

            if len(new_step) >= max_steps:
                break

            if board in visited:
                continue
            else:
                visited.add(board)

            red_car = board.get_red_car()
            if self._is_solved(red_car):
                solution = new_step
                return solution
            else:
                queue.extendleft((move, new_step) for move in self._get_moves(board))

        return None

    def _is_solved(self, red_car):
        x, y = red_car.x, red_car.y
        return x == 2 and y == 4

    def _get_moves(self, start_board):
        """Find all possible moves from current state and return an
        iterable object.
        """

        board = start_board.board
        for v in start_board.vehicles:
            if v.orientation == 'H':
                if v.x - 1 >= 0 and board[v.y][v.x - 1] == '.':
                    new_vehicle = v.__class__(v.id, v.x - 1, v.y, v.orientation)
                    new_vehicles = start_board.vehicles.copy()
                    new_vehicles.remove(v)
                    new_vehicles.append(new_vehicle)
                    yield Board().set_board_from_vehicles(new_vehicles)
                if v.x + v.length <= 5 and board[v.y][v.x + v.length] == '.':
                    new_v = v.__class__(v.id, v.x + 1, v.y, v.orientation)
                    new_vehicles = start_board.vehicles.copy()
                    new_vehicles.remove(v)
                    new_vehicles.append(new_v)
                    yield Board().set_board_from_vehicles(new_vehicles)
            else:
                if v.y - 1 >= 0 and board[v.y - 1][v.x] == '.':
                    new_v = v.__class__(v.id, v.x, v.y - 1, v.orientation)
                    new_vehicles = start_board.vehicles.copy()
                    new_vehicles.remove(v)
                    new_vehicles.append(new_v)
                    yield Board().set_board_from_vehicles(new_vehicles)
                if v.y + v.length <= 5 and board[v.y + v.length][v.x] == '.':
                    new_v = v.__class__(v.id, v.x, v.y + 1, v.orientation)
                    new_vehicles = start_board.vehicles.copy()
                    new_vehicles.remove(v)
                    new_vehicles.append(new_v)
                    yield Board().set_board_from_vehicles(new_vehicles)
