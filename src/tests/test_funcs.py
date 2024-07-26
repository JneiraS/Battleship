import unittest

from src.funcs import (coordinate_converter,
                       check_coordinates_validity, collect_valid_coordinates, all_ships_have_been_sunk)


class MyTestCase(unittest.TestCase):
    def test_coordinate_converter(self):
        case_1 = coordinate_converter('A1')
        case_2 = coordinate_converter('h5')
        case_3 = coordinate_converter('E8')

        self.assertEqual(case_1, (1, 1))
        self.assertEqual(case_2, (8, 5))
        self.assertEqual(case_3, (5, 8))

    def test_check_coordinates_validity(self):
        case_1 = check_coordinates_validity((5, 5))
        case_2 = check_coordinates_validity((14, 5))

        self.assertTrue(case_1)
        self.assertFalse(case_2)

    def test_collect_valid_coordinates(self):
        _, user_input = collect_valid_coordinates()

        self.assertEqual(user_input, 'b4')

    def test_all_ships_have_been_sunk(self):
        test_fleet: list = [['#', '#', '#'], ['#', '#', '#']]
        self.assertTrue(all_ships_have_been_sunk(test_fleet))


if __name__ == '__main__':
    unittest.main()


def test_all_ships_have_been_sunk():
    assert False
