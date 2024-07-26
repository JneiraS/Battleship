#!/usr/bin/env python3
# -*- coding: utf-8 -*-

GRID_SEIZE: int = 10

set_of_possible_coordinates: list[tuple] = [
    (i, j) for i in range(1, GRID_SEIZE + 1) for j in range(1, GRID_SEIZE + 1)
]

POSSIBLE_SHIP_DIRECTIONS: tuple = ("horizontal", "vertical")
NAME_AND_SIZE_OF_SHIPS: dict = {
    "aircraft_carrier": 5,
    "cruiser": 4,
    "destroyer": 3,
    "submarine": 3,
    "torpedo_boat": 2,
}
