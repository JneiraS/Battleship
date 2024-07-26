from string import ascii_uppercase


class GridPrinter:

    def print(self, coordinates_shots) -> None:
        """
        Affiche une grille de jeu représentant le champ de bataille naval avec les tirs effectués.
        :param coordinates_shots: Un dictionnaire contenant les coordonnées des tirs comme clés et leur
        résultat comme valeurs.
        """
        letters_line = [i for i in ascii_uppercase[0:10]]
        letters_line.insert(0, "   ")
        self.line_printer(letters_line)
        for line in range(1, 11):
            elements = []
            for col in range(1, 11):
                if (col, line) in coordinates_shots.keys():
                    elements.append(str(coordinates_shots[col, line]))
                else:
                    elements.append(' ')
            elements.insert(0, f"  {line}")
            self.line_printer(elements)

    @staticmethod
    def line_printer(line: list) -> None:
        """
        Imprime une ligne de texte avec des barres horizontales et des intersections autour.
        :param line:(list) La ligne de texte à imprimer.
        """
        print(
            f"{' | '.join([str(i).replace('True', ' ') for i in line])} |\n{GridPrinter.bars(len(line))}"
        )

    @staticmethod
    def bars(cell: int) -> str:
        """
         Génère une séquence de barres horizontales et d'intersections basée sur un nombre donné.
        :param cell:(int) Le nombre de répétitions pour les barres horizontales et les intersections.
        :return: Une chaîne de caractères représentant les barres horizontales et les intersections.
        """
        horrizont_bar = "---"
        intersections = "+"
        return ((intersections + horrizont_bar) * cell) + intersections
