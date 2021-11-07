import unittest
from contrived_func import contrived_func

# CS-362- Improving-Coverage

class MyTestCase(unittest.TestCase):
    def test_C1(self):
        self.assertFalse(contrived_func(5))

    def test_C2(self):
        self.assertTrue(contrived_func(6))

    def test_C3(self):
        self.assertFalse(contrived_func(69))

    def test_C4(self):
        self.assertTrue(contrived_func(70))

    def test_C5(self):
        self.assertFalse(contrived_func(85))

    def test_C6(self):
        self.assertTrue(contrived_func(110))

    def test_C7(self):
        self.assertFalse(contrived_func(151))


if __name__ == '__main__':
    unittest.main()
