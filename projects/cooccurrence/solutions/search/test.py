import sys
import unittest

from cooccurrence import Cooccurrence

class TestCooccurrence(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.co = Cooccurrence(sys.stdin)

    def test_pairs(self):
        test_assertions = [
            (("Leon", "Thomas"), 4),
            (("Dexter", "Stuart"), 0),
            (("David", "Lisa"), 453),
            (("Ann", "Anne"), 10),
            (("Leon", ""), 0),
            (("Leon", "Leon"), 25)
        ]
        for pair, count in test_assertions:
            self.assertEqual(self.co.get(*pair), count)

if __name__ == "__main__":
    unittest.main()
