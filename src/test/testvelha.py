__author__ = 'carlo'

import sys
sys.path.append("/home/carlotolla/dev/velha3d/src/test/")
import unittest
import unittest.mock as mock
import glow


class TestIntegerArithmeticTestCase(unittest.TestCase):
    def tearDown(self):
        self.s.reset_mock()
        self.b.reset_mock()
        self.c.reset_mock()

    @mock.patch('glow.sphere')
    @mock.patch('glow.box')
    @mock.patch('glow.canvas')
    def setUp(self, canvas, box, sphere):
        self.s = sphere
        self.b = box
        self.c = canvas
        from velha import main, Casa
        self.casas = Casa.CASAS

        self.t = main()

    def testClicou(self):
        self.b.reset_mock()
        self.assertIn((0, 0, 0), self.casas, "Not in CASAS:" % self.casas)
        self.t[0].clicou()
        self.t[4].clicou()
        self.t[9].clicou()
        self.t[5].clicou()
        self.t[18].clicou()
        self.assertEqual(len(self.s.mock_calls), 6, "Not 2 spheres: %s" % self.s.mock_calls)
        self.assertEqual(len(self.b.mock_calls), 5, "Not 5 boxes: %s" % self.b.mock_calls)

    def testInit(self):  # test method names begin 'test*'
        #self.assertEqual(len(self.c.mock_calls), 2, "Not 2 canvas: %s" % self.c.mock_calls)
        #self.assertEqual(len(self.b.mock_calls), 27, "Not 27 boxes: %s" % self.b.mock_calls)
        self.assertIn((0, 0, 0), self.casas, "Not in CASAS:" % self.casas)

if __name__ == "__main__":
    unittest.main()
    print('didit', __name__)
