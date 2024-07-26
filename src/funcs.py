# -*- coding: utf-8 -*-

import random
from string import ascii_uppercase

from src.consts import (set_of_possible_coordinates,
                        GRID_SEIZE)


def coordinate_converter(coordinate_to_convert: str) -> tuple[int, int]:
    """
    Convertit une coordonnée sous forme de lettre majuscule suivi d'un numéro en coordonnées numériques.
    Exemple: A1 → (1, 1)
    """
    coordinate_to_convert = coordinate_to_convert.strip().upper()
    return ascii_uppercase.find(coordinate_to_convert[0]) + 1, int(
        (coordinate_to_convert[1:])
    )


def check_coordinates_validity(coordinate: tuple) -> bool:
    """
        Vérifie si les coordonnées sont valides en se basant sur leur emplacement dans un espace 10x10.
    """
    if coordinate[0] <= 10 and coordinate[1] <= 10:
        return True
    else:
        return False


def collect_valid_coordinates() -> tuple:
    """
    Demande à l'utilisateur d'entrer une coordonnée valide jusqu'à ce qu'elle soit acceptée.
    Convertit l'entrée de l'utilisateur en coordonnées valides et vérifie leur adéquation.
    """
    coordinate_is_valid = False

    while not coordinate_is_valid:
        try:
            user_coordinate: str = input("Entrez une coordonnée (exemple: F4 ou d7): ")
            converted_coordinate = coordinate_converter(user_coordinate)
            coordinate_is_valid = check_coordinates_validity(converted_coordinate)

            return converted_coordinate, user_coordinate

        except ValueError as e:
            print(f"Erreur lors de la conversion: {e}")
            continue


def all_ships_have_been_sunk(fleet: list) -> bool:
    """
        Vérifie si toutes les embarcations ont été coulées en comparant le nombre de cellules marquées (
        '#') dans leur disposition.
    """
    return len([value for sublist in [ship.coordinates.values() for ship in fleet] for value in sublist if
                value == '#']) == 17


def select_random_start_within_limit(limit: int, orientation: str) -> tuple:
    """
    Trouve un point de départ aléatoire dont l'abscisse est inférieure ou égale au limit spécifié.
    Parcourt un ensemble de coordonnées possibles jusqu'à trouver un tel point, qui est ensuite retourné.
    """
    direction = 0 if orientation == "horizontal" else 1
    seuil = 0

    while True:
        start_point: tuple = random.choice(set_of_possible_coordinates)
        if start_point[direction] <= limit:
            break
        if seuil > GRID_SEIZE ** 2:
            break
        seuil += 1
    return start_point


def detect_hit_on_ship(fleet: list, coordinate):
    """
    Vérifie si un tir cible un navire. Utilise `collect_valid_coordinates` pour obtenir une coordonnée
    valide de l'utilisateur. Retourne `True` si un navire est touché, `False` sinon.
    """
    if any(ship.evaluate_shot_effect(coordinate) for ship in fleet):
        return True
