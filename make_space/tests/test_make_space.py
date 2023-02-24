from io import StringIO
from unittest import TestCase
from unittest.mock import patch

from src.facade import MakeSpaceFacade
from src.models.event import Event


class MakeSpaceTest(TestCase):
    def test_time_range_overlap(self):
        t1 = Event("13:00", "15:00")
        t2 = Event("15:00", "17:00")
        self.assertEqual(t1.overlap(t2), False)

    def test_rooms_available(self):
        test_facade = MakeSpaceFacade()
        with patch('sys.stdout', new=StringIO()) as fake_out:
            test_facade.vacancy("13:00", "15:00")

        self.assertEqual(fake_out.getvalue(), "NO_VACANT_ROOM\n")
