# Testing-Part-1
# Max Area Container Solution Testing

This repository contains the solution to the "Container with Most Water" problem and unit tests to validate the solution.

## Solution

The solution is implemented in `solution.py` using a two-pointer technique.

## Unit Tests

Unit tests are written in `test_solution.py` using the `unittest` framework.

### Requirements

- Python 3.7+
- `unittest` (comes with Python's standard library)

### Running the Tests

To run the tests, simply execute:

```bash
python -m unittest discover
```
### Testing Techniques
1. Finding and Reporting Bugs:
Any test case failure is considered a bug. The failed assertion will report the bug and its cause.

2. Use of Test Stubs:
Currently, the tests are direct unit tests and do not use external dependencies requiring mocks/stubs.

4. Using Test Parameterization:
Parameterization is manually done by writing different test cases in the test_solution.py file.

6. Using Setup/Teardown:
- The setUp method is used to create an instance of Solution before each test.
- The tearDown method is used to clean up after each test.
  
7. Fixing Detected Bugs:
If a test fails, the corresponding bug should be fixed in the solution.py file, and a commit message should reflect the fix, e.g., (fix) No upper limit check of the input array length.

### Example Commit for Fixing a Bug(sql)
commit abc1234
Author: Your Name <youremail@example.com>
Date:   2024-06-13

    (fix) No upper limit check of the input array length

### Constraints Verification
All tests verify that:

- The length of the height array is within the required range.
- Heights within the array are within the valid range [0, 10,000].
  
This repository ensures that the solution to the problem adheres to the constraints and behaves as expected across various test scenarios.

###Test Cases
The test_solution.py file contains a series of test cases to verify the correctness of the maxArea function. The tests include:

- test_example_1: Tests the function with an example case.
- test_different_heights: Tests the function with different varied heights.
- test_large_numbers: Tests the function with large height numbers.
- test_increasing_sequence: Tests the function with an increasing sequence of heights.
- test_decreasing_sequence: Tests the function with a decreasing sequence of heights.
- test_random_sequence: Tests the function with a random sequence of heights.
- test_identical_heights: Tests the function with all identical heights.
- test_two_heights: Tests the function with only two heights.
- test_large_input_size: Tests the function with the maximum input size.
- test_no_water: Tests the function with heights that can't hold any water.
- test_one_height_zero: Tests the function with one height as zero.
- test_empty_input: Tests the function with an empty input.
- test_invalid_input_non_integer: Tests the function with invalid non-integer input.
- test_invalid_input_negative: Tests the function with negative heights.
- test_invalid_input_exceeds_max: Tests the function with heights exceeding the maximum allowed value.


### ©Copyrights belongs to Aswadh Puthen Veede (HITS)
