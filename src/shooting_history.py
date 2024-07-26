# -*- coding: utf-8 -*-
from dataclasses import dataclass

from src.ship import Ship


@dataclass
class ShootingHistory:
    coordinates: dict

    def add_shot(self, shot: tuple, value: str):
        self.coordinates[shot] = value




def mark_as_sunken_in_grid(fleet: list[Ship], history: ShootingHistory) -> None:
    """
    Marque tous les navires coulés dans la grille de jeu en mettant à jour l'historique des tirs.

    Cette fonction parcourt chaque navire dans la flotte. Si un navire est entièrement coulé (c'est-à-dire,
    toutes ses coordonnées sont marquées comme touchées '#'), alors elle met à jour l'historique des tirs
    pour refléter que ces coordonnées ont été définitivement coulées.
    :param fleet:  La flotte de navires à vérifier et potentiellement marquer comme coulés.
    :param history:  L'historique des tirs qui sera mis à jour avec les coordonnées des navires coulés.
    """
    for boat in fleet:
        if len([False for k, v in boat.coordinates.items() if v == '#']) == len(boat.coordinates):
            for k, v in boat.coordinates.items():
                history.coordinates.update({k: '#'})
