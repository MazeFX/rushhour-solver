# -*- coding: utf-8 -*-

"""
Package: rushhour_solver
File: cli.py
Creator: Nick Geense
Date: 23-11-2016

Command Line Interface for the rushhour-solver and board parser.



"""

import subprocess
import os.path
import click
import logging


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

    if log:
        Lumberjack.info('--> Starting application..')
        logging.basicConfig(level=getattr(logging, log.upper()))
    Lumberjack.info('--> Starting application..')

    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    if test:
        print('Starting up tests..')
        testdir = os.path.join(root_dir, 'tests')
        subprocess.run(['python', '-m', 'unittest', 'discover', '-s', testdir])
        return

    print('Here you call the program.')
