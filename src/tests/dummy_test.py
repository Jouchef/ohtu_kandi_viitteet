import unittest
from dummy import dummy

class TestVarasto(unittest.TestCase):
    def setUp(self):
        pass

    def test_dummy(self):
        x = dummy(5)

        self.assertEqual(x, 5)