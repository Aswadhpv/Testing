import unittest
from solution import Solution

class TestSolution(unittest.TestCase):

    def setUp(self):
        """Set up the test environment before each test."""
        self.solution = Solution()

    def test_example_1(self):
        """Test case based on the example provided."""
        heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]
        self.assertEqual(self.solution.maxArea(heights), 49)

    def test_different_heights(self):
        """Test case with different varied heights."""
        heights = [1, 2, 1]
        self.assertEqual(self.solution.maxArea(heights), 2)

    def test_large_numbers(self):
        """Test case with large height numbers."""
        heights = [10000, 1, 10000]
        self.assertEqual(self.solution.maxArea(heights), 20000)

    def test_increasing_sequence(self):
        """Test case with an increasing sequence."""
        heights = [1, 2, 3, 4, 5]
        self.assertEqual(self.solution.maxArea(heights), 6)

    def test_decreasing_sequence(self):
        """Test case with a decreasing sequence."""
        heights = [5, 4, 3, 2, 1]
        self.assertEqual(self.solution.maxArea(heights), 6)

    def test_random_sequence(self):
        """Test case with a random sequence of heights."""
        heights = [1, 3, 2, 5, 25, 24, 5]
        self.assertEqual(self.solution.maxArea(heights), 24)

    def test_identical_heights(self):
        """Test case with all identical heights."""
        heights = [5, 5, 5, 5, 5]
        self.assertEqual(self.solution.maxArea(heights), 20)

    def test_two_heights(self):
        """Test case with only two heights."""
        heights = [2, 4]
        self.assertEqual(self.solution.maxArea(heights), 2)

    def test_large_input_size(self):
        """Test case with the maximum input size."""
        heights = [10000] * 100000
        self.assertEqual(self.solution.maxArea(heights), 10000 * (len(heights) - 1))

    def test_no_water(self):
        """Test case with heights that can't hold any water."""
        heights = [0, 0, 0, 0, 0]
        self.assertEqual(self.solution.maxArea(heights), 0)

    def test_one_height_zero(self):
        """Test case with one height as zero."""
        heights = [0, 10]
        self.assertEqual(self.solution.maxArea(heights), 0)

    def test_empty_input(self):
        """Test case with empty input."""
        heights = []
        result = self.solution.maxArea(heights)
        self.assertEqual(result, 0)  # Expect 0 for empty input

    def test_invalid_input_non_integer(self):
        """Test case with invalid non-integer input."""
        heights = [1, "a", 2]
        with self.assertRaises(TypeError):
            self.solution.maxArea(heights)

    def test_invalid_input_negative(self):
        """Test case with negative heights."""
        heights = [1, -2, 3]
        result = self.solution.maxArea(heights)
        self.assertIsInstance(result, int)  # Just check it returns an int

    def test_invalid_input_exceeds_max(self):
        """Test case with heights exceeding the maximum allowed value."""
        heights = [1, 10001, 2]
        result = self.solution.maxArea(heights)
        self.assertIsInstance(result, int)  # Just check it returns an int

    def tearDown(self):
        """Clean up after each test."""
        del self.solution

if __name__ == "__main__":
    unittest.main()
