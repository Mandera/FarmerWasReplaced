

from unittest import TestCase

from helpers import move_instructions_with_wrap


class Test(TestCase):
    def test_move_instructions(self):
        self.assertEqual((0, 1), move_instructions_with_wrap(3, 4))
        self.assertEqual((1, 3), move_instructions_with_wrap(5, 2))
        self.assertEqual((0, 4), move_instructions_with_wrap(8, 2))

