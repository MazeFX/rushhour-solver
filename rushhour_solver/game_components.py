# -*- coding: utf-8 -*-

"""
Module: rushhour_solver
File: game_components.py
Creator: Nick Geense
Date: 23-11-2016

Module for game component classes.

**Classes**

* Board
* Vehicles
    Subclasses: Car, Truck, RedCar

"""


class Board(object):

    def __init__(self):
        self.board = None
        self.vehicles = set()

    def set_board(self, board):
        self.board = board

    def get_board(self):
        return self.board

    def set_board_from_vehicles(self, vehicles):
        self.vehicles = set(vehicles)
        board = [['.' for n in range(6)] for n in range(6)]

        for vehicle in self.vehicles:
            x, y = vehicle.x, vehicle.y
            if vehicle.orientation == 'H':
                for i in range(vehicle.length):
                    board[y][x + i] = vehicle.id
            else:
                for i in range(vehicle.length):
                    board[y + i][x] = vehicle.id
        self.board = board

    def set_vehicles(self, vehicles):
        self.vehicles = set(vehicles)

    def get_vehicles(self):
        return self.vehicles

    def get_red_car(self):
        red_car = None
        for vehicle in self.vehicles:
            if vehicle.id == 'r':
                red_car = vehicle
        return red_car

    def __hash__(self):
        return hash(self.__repr__())

    def __eq__(self, other):
        return self.board == other.board

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        s = '-' * 8 + '\n'
        for line in self.get_board():
            s += '|{0}|\n'.format(''.join(line))
        s += '-' * 8 + '\n'
        return s

    def __str__(self):
        s_vehicles = [str(x) for x in self.vehicles]
        s = 'Car list:\n' + ''.join(s_vehicles)
        b_board = [str(x) for x in self.board]
        b = 'Board:\n' + '\n'.join(b_board)
        return s + b


class Vehicle(object):
    """Vehicle base class"""

    def __init__(self, id, x, y, orientation):
        self.id = id
        self.x = x
        self.y = y
        self.orientation = orientation
        self.color = None


class Car(Vehicle):

    def __init__(self, *args):
        super(Car, self).__init__(*args)
        self.length = 2

    def __repr__(self):
        s = '<Car object: id={id}, x={x}, y={y}, orientation={orientation}>\n'.format(
            id=self.id,
            x=self.x,
            y=self.y,
            orientation=self.orientation
        )
        return s


class Truck(Vehicle):

    def __init__(self, *args):
        super(Truck, self).__init__(*args)
        self.length = 3

    def __repr__(self):
        s = '<Truck object: id={id}, x={x}, y={y}, orientation={orientation}>\n'.format(
            id=self.id,
            x=self.x,
            y=self.y,
            orientation=self.orientation
        )
        return s


class RedCar(Vehicle):

    def __init__(self, *args):
        super(RedCar, self).__init__(*args)
        self.length = 2

    def __repr__(self):
        s = '<RedCar object: id={id}, x={x}, y={y}, orientation={orientation}>\n'.format(
            id=self.id,
            x=self.x,
            y=self.y,
            orientation=self.orientation
        )
        return s
