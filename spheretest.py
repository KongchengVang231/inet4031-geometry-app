import unittest
import sphere

class sphereTest(unittest.TestCase):

    #these need to be updated for a sphere
    def test_volume1(self):
        assert(sphere.volume(1) == (4/3) * 3.14159 * 1**3)

    def test_volume2(self):
        assert(sphere.volume(2) == (4/3) * 3.14159 * 2**3)

    def test_volume3(self):
        assert(sphere.volume(3) == (4/3) * 3.14159 * 3**3)

    #failing test
    #def test_volume3(self):
        #assert(sphere.volume(10,1000) == ??)


if __name__ == '__main__':
    unittest.main()
