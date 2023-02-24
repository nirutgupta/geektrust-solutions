from io import StringIO
from unittest import TestCase
from unittest.mock import patch

from src.constants import GMAN_MOVE_POWER_USAGE, GMAN_TURN_POWER_USAGE
from src.enums.direction import Direction
from src.facade import GManFacade
from src.models.gman import GMan
from src.gman.path_finder import PathFinder
from src.models.point import Point


class GManTests(TestCase):
    def test_e2e_gman(self):
        gman_facade = GManFacade()
        gman_facade.source(2, 1, "E")
        gman_facade.destination(4, 3)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            gman_facade.print_power()
            self.assertEqual(fake_out.getvalue(), "POWER 155\n")

    def test_bot_move_power_usage(self):
        gman = GMan(100, Point(1, 2), Direction.W)
        gman.move()
        self.assertEqual(gman.power, 100 - GMAN_MOVE_POWER_USAGE)

    def test_bot_turn_power_usage(self):
        gman = GMan(100, Point(1, 2), Direction.W)
        gman.turn()
        self.assertEqual(gman.power, 100 - GMAN_TURN_POWER_USAGE)

    def test_path_finder_total_moves(self):
        pathfinder = PathFinder()
        moves = pathfinder.get_no_of_moves(Point(0, 0), Point(0, 0))
        self.assertEqual(moves, 0)

    def test_path_finder_total_turns(self):
        pathfinder = PathFinder()
        turns = pathfinder.get_no_of_turns(Point(0, 0), Direction.E, Point(1, 2))
        self.assertEqual(turns, 1)
