# Testing-Part-2
Testing the Task Container with Most water using E2E/UI tests

# Max Area Container Solution with Web UI

This project contains a web-based solution to the "Container with Most Water" problem, using Flask for the web framework and plain HTML for the UI. The project also includes end-to-end tests using Selenium.

## Solution

The solution logic is implemented in `solution.py`.

## Web UI

The web UI is implemented in `app.py` and the HTML template is in `templates/index.html`.

## Running the Web App

1. Install dependencies:
    ```bash
    pip install flask
    ```

2. Run the web app:
    ```bash
    python app.py
    ```

3. Open your browser and navigate to `http://127.0.0.1:5000/`.

## Running the E2E Tests

1. Install dependencies:
    ```bash
    pip install selenium webdriver-manager
    ```

2. Ensure the web app is running.

3. Run the E2E tests:
    ```bash
    python test_e2e.py
    ```

## Testing Techniques

1. **Finding and Reporting Bugs**:
    - E2E tests will fail if the expected output does not match the actual output, indicating a bug.

2. **Use of Test Stubs**:
    - No external dependencies in this context require mocks/stubs. Future enhancements might use `unittest.mock`.

3. **Using Test Parameterization**:
    - Different test cases are manually written for varied input scenarios.

4. **Using Setup/Teardown**:
    - `setUp` and `tearDown` methods are used to initialize and clean up the web driver before and after each test.

5. **Fixing Detected Bugs**:
    - Fixes should be made in `solution.py` or `app.py`, with appropriate commit messages reflecting the changes.

### New Test cases
- test_valid_input: Validates the application's response when valid input heights are provided.
- test_min_constraints: Checks the application's behavior with the minimum required constraints.
- test_large_input: Tests the application's performance with a large input.
- test_invalid_input: Verifies the handling of invalid input scenarios.
- test_empty_input: This test checks if the application correctly handles an empty input by verifying the presence of an appropriate error message.
- test_non_numeric_input: This test verifies that the application can identify and handle non-numeric inputs, ensuring an error message is displayed.
- test_negative_numbers_input: This test ensures that the application correctly handles negative numbers in the input and displays an appropriate error message.
- test_special_characters_and_whitespace: This test verifies how the application handles input containing special characters and whitespace.
- test_responsiveness: This test simulates quick user interactions to check the responsiveness of the application and verifies that the result is displayed within a reasonable time frame.
- test_all_heights_zero: This test case checks the behavior of the application when all heights provided are zero.

## Constraints Verification

All tests verify that:
- The length of the `height` array is within the required range.
- Heights within the array are within the valid range `[0, 10,000]`.

This project ensures that the solution adheres to the constraints and behaves as expected across various test scenarios.

### ©Copyrights owned by Aswadh Puthen Veede(HITS)
