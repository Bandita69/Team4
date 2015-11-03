__author__ = 'Timko Andras'

import unittest
from alap import i_need_your_kg


class MyTestCase(unittest.TestCase):
    def test_something(self):

        self.assertEqual(40, i_need_your_kg(40), "Nem jo")


if __name__ == '__main__':
    unittest.main()
