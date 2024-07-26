#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from src.funcs import collect_valid_coordinates, all_ships_have_been_sunk, detect_hit_on_ship
from src.grid_printer import GridPrinter
from src.ship import Shipyard
from src.shooting_history import ShootingHistory, mark_as_sunken_in_grid


def main():
    """
    Fonction principale du jeu de bataille navale textuel.
    """

    history = ShootingHistory({})
    graphic_grid = GridPrinter()

    try:
        fleet: list = Shipyard().production()

        while True:
            coordinate, original_coordinate = collect_valid_coordinates()
            if detect_hit_on_ship(fleet, coordinate):

                history.add_shot(coordinate, 'x')
                mark_as_sunken_in_grid(fleet, history)

            else:
                if history.coordinates.get(coordinate) is not None:
                    print(f'Vous avez déjà tiré en {original_coordinate.upper()}')
                else:
                    history.add_shot(coordinate, '-')
                    print('Manqué')

            if all_ships_have_been_sunk(fleet):
                print(f"Vous avez gagné! en {len(history.coordinates)} tirs")
                break

            graphic_grid.print(history.coordinates)
    except ValueError:
        print('Erreur! Redémarrez le programme pour une nouvelle tentative de génération aléatoire.')


if __name__ == '__main__':
    main()



