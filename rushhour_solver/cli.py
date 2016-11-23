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
@click.option('--test', is_flag=True, help='Run tests for Rush Hour Solver.')
@click.argument('filename', type=click.Path(exists=True), required=False)
def main(filename, log, test):
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

    print('Trying to find a solution..')
    if filename is None:
        filename = os.path.join(root_dir, 'puzzles', 'puzzle_default.txt')

    print('filename= ', filename)
    rushhour = RushHour(filename)

    solution = rushhour.get_solution()
    painter = RushHourPainter()

    painter.print_solution(solution)
