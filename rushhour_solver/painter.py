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
    output_mode = 'Default'
    fore_color_list = [Back.YELLOW, Back.MAGENTA, Back.GREEN,
                       Back.CYAN, Back.WHITE, Back.BLUE, Back.RED]
    back_color_list = [Back.YELLOW, Back.MAGENTA, Back.GREEN,
                       Back.CYAN, Back.WHITE, Back.BLUE, Back.RED]
    car_colors = {}

    def __init__(self, output='default', color_mode=False, *args):
        self.set_color_mode(color_mode)
        self.set_output_mode(output)
        self.start_board = None

    def set_color_mode(self, color_mode):
        self.color_mode = color_mode

    def get_color_mode(self):
        return self.color_mode

    def set_output_mode(self, output_mode):
        self.output_mode = output_mode

    def get_output_mode(self):
        return self.output_mode

    def get_car_colors(self, solution):
        color_dict = {}
        vehicles = solution[0].vehicles

        i = 0
        for vehicle in vehicles:
            if vehicle.id == 'r':
                color_dict['r'] = 6
            else:
                color_dict[vehicle.id] = i % 6
            i += 1
        return color_dict

    def get_print_color(self, car_id):
        if self.color_mode:
            color_index = self.car_colors[car_id]
            if color_index <= len(self.back_color_list) - 1:
                return self.back_color_list[color_index]
            else:
                Lumberjack.warning('Given color_index is invalid. Not painting color')
                return ''
        else:
            return ''

    def print_solution(self, solution):
        output_mode = self.get_output_mode()
        color_mode = self.get_color_mode()
        if color_mode:
            self.car_colors = self.get_car_colors(solution)

        # board_string = self._get_board_strings(solution)
        solution_string = self._get_solution_string(solution)




        print('Found solution:')
        for i in range(len(solution_string)):
            print('Step {i}: {step}'.format(i=i + 1, step=solution_string[i]))

    def _get_solution_string(self, solution):
        """Generate list of steps from a solution path."""
        steps = []
        for i in range(len(solution) - 1):
            r1, r2 = solution[i], solution[i + 1]
            v1 = list(r1.vehicles - r2.vehicles)[0]
            v2 = list(r2.vehicles - r1.vehicles)[0]
            if v1.x < v2.x:
                steps.append(self.get_print_color(v1.id) + '{0} Right'.format(v1.id) + Style.RESET_ALL)
            elif v1.x > v2.x:
                steps.append('{0} Left'.format(v1.id))
            elif v1.y < v2.y:
                steps.append('{0} Down'.format(v1.id))
            elif v1.y > v2.y:
                steps.append('{0} Up'.format(v1.id))
        return steps

    def _get_board_strings(self, boards):
        board_strings = []
        for board in boards:
            for line in board:
                string = ''.join(line)
                board_strings[board.index(line)] += string


