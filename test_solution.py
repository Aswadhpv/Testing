import unittest
from solution import Solution

class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]
        self.assertEqual(len(heights), 9)
        self.assertTrue(all(0 <= h <= 10000 for h in heights))
        self.assertEqual(self.solution.maxArea(heights), 49)

    def test_example_2(self):
        heights = [1, 1]
        self.assertEqual(len(heights), 2)
        self.assertTrue(all(0 <= h <= 10000 for h in heights))
        self.assertEqual(self.solution.maxArea(heights), 1)

    def test_min_constraints(self):
        heights = [0, 0]
        self.assertEqual(len(heights), 2)
        self.assertTrue(all(0 <= h <= 10000 for h in heights))
        self.assertEqual(self.solution.maxArea(heights), 0)

        heights = [1, 2]
        self.assertEqual(len(heights), 2)
        self.assertTrue(all(0 <= h <= 10000 for h in heights))
        self.assertEqual(self.solution.maxArea(heights), 1)

    def test_max_constraints(self):
        heights = [10000] * 100000
        self.assertEqual(len(heights), 100000)
        self.assertTrue(all(0 <= h <= 10000 for h in heights))
        self.assertEqual(self.solution.maxArea(heights), 10000 * (len(heights) - 1))

    def test_varied_heights(self):
        heights = [2, 3, 4, 5, 18, 17, 6]
        self.assertEqual(len(heights), 7)
        self.assertTrue(all(0 <= h <= 10000 for h in heights))
        self.assertEqual(self.solution.maxArea(heights), 17)

        heights = [1, 3, 2, 5, 25, 24, 5]
        self.assertEqual(len(heights), 7)
        self.assertTrue(all(0 <= h <= 10000 for h in heights))
        self.assertEqual(self.solution.maxArea(heights), 24)

    def tearDown(self):
        del self.solution

if __name__ == "__main__":
    unittest.main()
