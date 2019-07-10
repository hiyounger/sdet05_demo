import unittest

from Yzx.Person.homework0628.shop.members import Members

class TestAccumulatedShoppingPoints(unittest.TestCase):
    def test_accumulated_shopping_points_case01(self):
        exp_disc=0.9
        act_disc=Members.accumulated_shopping_points(18845871680,10000)
        self.assertEqual(exp_disc, act_disc)
    def test_accumulated_shopping_points_case02(self):
        exp_disc=False
        act_disc=Members.accumulated_shopping_points(1111,10000)
        self.assertEqual(exp_disc, act_disc)


if __name__ == '__main__':
    unittest.main()
