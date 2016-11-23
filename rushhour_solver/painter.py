# -*- coding: utf-8 -*-

"""
Module: rushhour_solver
File: painter.py
Creator: Nick Geense
Date: 23-11-2016

Rush Hour solution painter.

Not much time so its gonna be quick and dirty.

"""

import logging

from colorama import Fore, Back, Style


Lumberjack = logging.getLogger(__name__)


class RushHourPainter(object):

    color_mode = False
    color_list = [Back.BLACK, Back.YELLOW, Back.MAGENTA, Back.GREEN,
                  Back.CYAN, Back.WHITE, Back.BLUE, Back.RED]

    def __init__(self, color_mode=False, output='default', *args):
        self.set_color_mode(color_mode)
        self.output_mode = output
        self.start_board = None

    def set_color_mode(self, color_mode):
        self.color_mode = color_mode

    def get_color_mode(self):
        return self.color_mode

    def get_print_color(self, color_index):
        if color_index <= len(self.color_list) - 1:
            return self.color_list[color_index] if self.color_mode else ''
        else:
            Lumberjack.warning('Given color_index is invalid. Not painting color')
            return ''

    def print_solution(self, solution):
        solution_string = self._get_solution(solution)
        for i in range(len(solution_string)):
            print('Step {i}: {step}'.format(i=i, step=solution_string[i]))

    def _get_solution(self, solution):
        """Generate list of steps from a solution path."""
        steps = []
        for i in range(len(solution) - 1):
            r1, r2 = solution[i], solution[i + 1]
            v1 = list(r1.vehicles - r2.vehicles)[0]
            v2 = list(r2.vehicles - r1.vehicles)[0]
            if v1.x < v2.x:
                steps.append('{0} Right'.format(v1.id))
            elif v1.x > v2.x:
                steps.append('{0} Left'.format(v1.id))
            elif v1.y < v2.y:
                steps.append('{0} Down'.format(v1.id))
            elif v1.y > v2.y:
                steps.append('{0} Up'.format(v1.id))
        return steps

    def print_boards(self, boards):
        board_strings = []
        for board in boards:
            for line in board:
                string = ''.join(line)
                boardstrings[board.index(line)] += string


