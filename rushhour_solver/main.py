# -*- coding: utf-8 -*-

"""
Module: rushhour_solver
File: main.py
Creator: Nick Geense
Date: 23-11-2016

Main controller for rushhour-solver components.

To supply an uniform contruct for interfacing.

"""


class RushHour(object):
    """
    Main Rush Hour object.

    Needs a filename as input along with possible kwargs.


    """

    def __init__(self, filename, **kwargs):
        self.filename = filename
