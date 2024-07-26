#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import random
from dataclasses import dataclass

from src.consts import (POSSIBLE_SHIP_DIRECTIONS, NAME_AND_SIZE_OF_SHIPS,
                        set_of_possible_coordinates)
from src.funcs import select_random_start_within_limit


@dataclass
class Ship:
    def __init__(self):
        self.name = None
        self.coordinates = None

    @staticmethod
    def initialize_ship_layout(seize_boat: int, orientation: str) -> dict:
        """
        Génère un dictionnaire représentant un bateau de taille spécifiée, orienté dans une direction donnée.
        """
        limit = 10 - seize_boat
        start_point = select_random_start_within_limit(limit, orientation)
        extension: int = 0
        temp_list = []

        for _ in range(seize_boat):
            while len(temp_list) < seize_boat:
                new_tuple: tuple = (start_point[0] + extension, start_point[1]) if (orientation ==
                                                                                    'horizontal') else (
                    start_point[0], start_point[1] + extension)

                temp_list.append(new_tuple)
                set_of_possible_coordinates.remove(new_tuple)
                extension += 1
        coordinate_and_status: dict = dict(zip(temp_list, [True] * seize_boat))

        return coordinate_and_status

    def evaluate_shot_effect(self, coordinate: tuple) -> bool:
        """
        Vérifie l'impact d'un tir sur un navire, gère les manqués ou touches multiples. Retourne True si le
        tir touche un navire, False sinon.
        """
        # Liste des conditions et actions correspondantes pour l'impact du tir
        impact_conditions = [
            (lambda: self.coordinates.get(coordinate) is True and len(
                [v for k, v in self.coordinates.items() if v is True]) == 1,
             lambda: (self.sunken(), print(f'{self.name} Touché et coulé'))),
            (lambda: self.coordinates.get(coordinate) is True,
             lambda: (self.coordinates.update({coordinate: False}), print('Touché')))
        ]

        # Liste des conditions et actions correspondantes pour les manqués ou touches multiples
        missing_or_multiple_hits = [
            (lambda: self.coordinates.get(coordinate) is False, lambda: print('Le Bateau a déjà été touché '
                                                                              'ici'))
        ]

        # Vérifie les conditions pour l'impact du tir
        if any(action() for condition, action in impact_conditions if condition()):
            return True

        # Vérifie les conditions pour les tirs manqués
        if any(action() for condition, action in missing_or_multiple_hits if condition()):
            return False

    def sunken(self):
        for k, v in self.coordinates.items():
            self.coordinates.update({k: '#'})


class Shipyard:

    @staticmethod
    def production() -> list:
        """
        Génère une flotte de navires avec des coordonnées aléatoires sur un plateau de jeu.

        La fonction parcourt chaque navire défini dans le dictionnaire NAME_AND_SIZE_OF_SHIPS,
        génère une orientation aléatoire pour chaque navire parmi celles disponibles dans
        POSSIBLE_SHIP_DIRECTIONS,
        et initialise les coordonnées de chaque navire en utilisant la méthode initialize_ship_layout.
        Ce processus se répète jusqu'à ce que toutes les places de la flotte soient remplies.

        :return: list: Une liste contenant tous les objets Ship
        """

        coordinates: list = []
        ship_fleet_size = len(NAME_AND_SIZE_OF_SHIPS)

        while len(coordinates) != ship_fleet_size:
            orientation = random.choice(POSSIBLE_SHIP_DIRECTIONS)

            for name, seize in NAME_AND_SIZE_OF_SHIPS.items():
                ship = Ship()
                ship.name = name
                ship.coordinates = Ship.initialize_ship_layout(seize, orientation)
                coordinates.append(ship)

        return coordinates
