# -*- coding: utf-8 -*-

"""
Module: rushhour_solver
File: cli.py
Creator: Nick Geense
Date: 23-11-2016

Command Line Interface for the rushhour-solver and board parser.



"""

import subprocess
import os.path
import click
import logging

from rushhour_solver.main import RushHour
from rushhour_solver.painter import RushHourPainter


Lumberjack = logging.getLogger(__name__)


@click.command()
@click.option('--log', '-l', help='Set the logger level.')
@click.option('--output', '-o', default='default', help='Set the output setting for representation.')
@click.option('--color', '-c', is_flag=True, help='Turn on color mode for the boards.')
@click.option('--test', is_flag=True, help='Run tests for Rush Hour Solver.')
@click.argument('filename', type=click.Path(exists=True), required=False)
def main(filename, log, output, color, test):
    """
    Command Line Tool for parsing and solving Rush Hour boards.

    Just give a file path and get a solution.
    When no path is provided the solver falls back on a demo default.
    """
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    if log:
        Lumberjack.info('--> Starting application..')
        logging.basicConfig(level=getattr(logging, log.upper()))
    Lumberjack.info('--> Starting application..')

    if test:
        print('Starting up tests..')
        testdir = os.path.join(root_dir, 'tests')
        subprocess.run(['python', '-m', 'unittest', 'discover', '-s', testdir])
        return

    if output == 'boards':
        Lumberjack.info('--> Visualisation for solution: only boards.')

    elif output == 'boards+moves':
        Lumberjack.info('--> Visualisation for solution: Boards with solution moves.')

    elif output != '':
        Lumberjack.info('--> Invalid argument for visualisation, switching to default.')
        output = 'default'

    elif output == 'default':
        Lumberjack.info('--> Visualisation for solution: Default, only solution moves.')

    if color:
        color_mode = True
        Lumberjack.info('--> Color is selected, printing boards in fancy colors.')
    else:
        color_mode = False

    print('Trying to find a solution..')
    if filename is None:
        filename = os.path.join(root_dir, 'puzzles', 'puzzle_default.txt')

    print('filename= ', filename)
    rushhour = RushHour(filename)

    solution = rushhour.get_solution()
    painter = RushHourPainter(output, color_mode)

    painter.print_solution(solution)
