# -*- coding: utf-8 -*-

"""
Module: tests
File: test_game_components.py
Creator: Nick Geense
Date: 23-11-2016

Unit Tests for Game Components.

"""


import os.path
import unittest
from unittest.mock import patch, MagicMock

from rushhour_solver.game_components import Board, Car, RedCar, Truck


class TestGameComponents(unittest.TestCase):

    # def setUp(self):
    #     root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    #     self.valid_puzzle = os.path.join(root_dir, 'tests', 'puzzle_valid.txt')
    #     self.invalid_puzzle = os.path.join(root_dir, 'tests', 'puzzle_invalid.txt')

    def test_car_init(self):
        id = 'A'
        length = 2
        car = Car(id, 0, 0, 'H')
        self.assertEqual(car.id, id)
        self.assertEqual(car.length, length)

    def test_red_car_init(self):
        id = 'rr'
        length = 2
        car = RedCar(id, 0, 0, 'H')
        self.assertEqual(car.id, id)
        self.assertEqual(car.length, length)

    def test_truck_init(self):
        id = 'A'
        length = 3
        truck = Truck(id, 0, 0, 'H')
        self.assertEqual(truck.id, id)
        self.assertEqual(truck.length, length)
