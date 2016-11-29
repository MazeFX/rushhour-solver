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
    fore_color_list = [Fore.YELLOW, Fore.MAGENTA, Fore.GREEN,
                       Fore.CYAN, Fore.WHITE, Fore.BLUE, Fore.RED]
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

    def _print_color_wrapper(self, text, car_color, fore):
        if self.color_mode:
            color_index = self.car_colors[car_color]
            if color_index <= len(self.back_color_list) - 1:
                if fore == 1:
                    s = self.fore_color_list[color_index] + text + Style.RESET_ALL
                    return s
                else:
                    s = self.back_color_list[color_index] + text + Style.RESET_ALL
                    return s
            else:
                Lumberjack.warning('Given color_index is invalid. Not painting color')
                return ''
        else:
            return text

    def print_solution(self, solution):
        output_mode = self.get_output_mode()
        color_mode = self.get_color_mode()

        print('Found solution:')
        if color_mode:
            self.car_colors = self.get_car_colors(solution)

        if output_mode == 'boards':
            Lumberjack.info('--> Visualisation for solution: only boards.')
            board_rows = self._get_board_strings(solution)
            for i in range(len(board_rows)):
                row = board_rows[i]
                for line in row:
                    print('{0}'.format(line))
                print('')
        else:

            if output_mode == 'boards+moves':
                Lumberjack.info('--> Visualisation for solution: Boards with solution moves.')
                board_rows = self._get_board_strings(solution)
                solution_rows = self._get_solution_string(solution, True)
                for i in range(len(board_rows)):
                    row = board_rows[i]
                    for line in row:
                        print('{0}'.format(line))
                    print('')
                    print('{0}'.format(solution_rows[i]))
                    print('')

            elif output_mode != '':
                Lumberjack.info('--> Invalid argument for visualisation, switching to default.')
                output_mode = 'default'

            if output_mode == 'default':
                Lumberjack.info('--> Visualisation for solution: Default, only solution moves.')
                solution_string = self._get_solution_string(solution, False)
                for i in range(len(solution_string)):
                    print('Step {i}: {step}'.format(i=i + 1, step=solution_string[i]))

        print('Board solved in {0} steps.'.format(len(solution)))

    def _get_solution_string(self, solution, horizontal):
        """Generate list of steps from a solution path."""
        steps = []
        for i in range(len(solution) - 1):
            r1, r2 = solution[i], solution[i + 1]
            v1 = list(r1.vehicles - r2.vehicles)[0]
            v2 = list(r2.vehicles - r1.vehicles)[0]
            if v1.x < v2.x:
                steps.append(self._print_color_wrapper('{0}'.format(v1.id), v1.id, 1) + ' Right')
            elif v1.x > v2.x:
                steps.append(self._print_color_wrapper('{0}'.format(v1.id), v1.id, 1) + ' Left')
            elif v1.y < v2.y:
                steps.append(self._print_color_wrapper('{0}'.format(v1.id), v1.id, 1) + ' Down')
            elif v1.y > v2.y:
                steps.append(self._print_color_wrapper('{0}'.format(v1.id), v1.id, 1) + ' Up')

        if horizontal:
            solution_rows = []
            line_string = '  Start  '
            for i in range(len(steps)):
                if self.color_mode:
                    string = '{:^18}'.format(steps[i])
                else:
                    string = '{:^9}'.format(steps[i])
                    print('step = ', len(steps[i]))
                    print('length = ', len(string))
                line_string += string
                if (i + 2) % 8 == 0:
                    solution_rows.append(line_string)
                    line_string = ' '
            solution_rows.append(line_string)
            steps = solution_rows

        return steps

    def _get_board_strings(self, solutions):
        """Build a list of lines for displaying the board in a row"""
        board_strings = []
        board_rows = []
        line_string = ''
        boards = [x.board for x in solutions]
        for i in range(len(boards)):
            board = boards[i]
            line_string += ' +------+'
            for line in board:
                if self.color_mode:
                    cells = []
                    for cell in line:
                        if cell in self.car_colors:
                            cells.append(self._print_color_wrapper(cell, cell, 0))
                        else:
                            cells.append(cell)
                else:
                    cells = line
                string = ' |' + ''.join(cells) + '|'
                if board.index(line) + 1 > len(board_strings):
                    board_strings.append('')
                board_strings[board.index(line)] += string

            if (i + 1) % 8 == 0:
                board_strings = [line_string] + board_strings + [line_string]
                board_rows.append(board_strings)
                line_string = ''
                board_strings = []

        board_strings = [line_string] + board_strings + [line_string]
        board_rows.append(board_strings)
        return board_rows


