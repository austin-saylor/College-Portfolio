"""
Testing module. This module tests
the title cost program.
"""

import math
import unittest
from unittest.mock import patch
from input import Input
from cost import Cost
from titlecost import main
from hypothesis import given, settings, Verbosity
from typing import Any
import hypothesis.strategies as st


class TestInput(unittest.TestCase):
    """
    Test class to test input functionality.
    """

    def setUp(self) -> None:
        """
        Set up an instance of the input class.
        """
        self.input = Input()

    def test_initialization(self) -> None:
        """
        Test the initialization of the input class.
        """
        self.assertEqual(self.input.input_str, [])

    def test_input_getter(self) -> None:
        """
        Test the getter method for the
        input string.
        """
        self.input._input_str = ['example', 'test']
        self.assertEqual(self.input.input_str, ['example', 'test'])

    def test_input_setter_valid(self) -> None:
        """
        Test the setter method for the
        input string, when given a
        valid value.
        """
        self.input.input_str = ['example', 'valid']
        self.assertEqual(self.input._input_str, ['example', 'valid'])

    def test_input_setter_invalid(self) -> None:
        """
        Test the setter method for the
        input string, when given an
        invalid value.
        """

        # Test the input setter when given a non-list item (string)
        with self.assertRaises(ValueError) as context:
            self.input.input_str = 'string'  # type: ignore
        self.assertTrue(
            'input_str must be a list of strings'
            in str(context.exception)
        )

        # Test the input setter when given a list with non-strings (int):
        with self.assertRaises(ValueError) as context:
            self.input.input_str = [1, 'integers', 2]  # type: ignore
        self.assertTrue(
            'All items in input_str must be strings'
            in str(context.exception)
        )

        # Test the input setter when given a list with non-strings (float):
        with self.assertRaises(ValueError) as context:
            self.input.input_str = [3.14159, 'floats', 2.71828]  # type: ignore
        self.assertTrue(
            'All items in input_str must be strings'
            in str(context.exception)
        )

        # Test the input setter when given a list with non-strings (bool):
        with self.assertRaises(ValueError) as context:
            self.input.input_str = [True, False]  # type: ignore
        self.assertTrue(
            'All items in input_str must be strings'
            in str(context.exception)
        )

    @patch('builtins.input', return_value='SuperMan 9000')
    def test_get(self, mocked_input: list[str]) -> None:
        """
        Test the value of the input.
        """
        mocked_input = self.input.get()

        # Test the value of the mocked input:
        self.assertEqual(mocked_input, ['SuperMan', '9000'])

        # Ensure that the actual input matches the mocked input:
        self.assertEqual(self.input.input_str, ['SuperMan', '9000'])


class TestCost(unittest.TestCase):
    """
    Test class to test the
    cost calculation.
    """
    @given(s=st.text(), c=st.floats(allow_infinity=True, allow_nan=True))
    @settings(max_examples=200, verbosity=Verbosity.verbose, derandomize=True)
    def test_cost_calculation(self, s: str, c: float) -> None:
        """
        Test the cost calculation.
        """

        # Initialize an instance of 'Cost':
        cost = Cost(s, c)

        # Calculate the final cost,
        # given the mocked values:
        final_cost = cost.calculate()

        # Determine the title length:
        title_len = float(len(s))

        if math.isnan(c):
            # If 'c' is nan, then the final_cost
            # is equal to the title length.
            self.assertEqual(final_cost, title_len)
        elif c < 0:
            # If 'c' is negative, then the final cost
            # is equal to the 'c'.
            self.assertEqual(final_cost, c)
        else:
            if title_len < c:
                # If the title length is less than 'c',
                # then the final cost is equal to the
                # title length.
                self.assertEqual(final_cost, title_len)
            else:
                # If the title length is greater than
                # 'c', then the final cost is equal
                # to 'c'.
                self.assertEqual(final_cost, c)


class TestMain(unittest.TestCase):
    """
    Test class to test the main
    function of the program.
    """
    @patch('titlecost.Input')
    @patch('builtins.print')
    def test_main_functionality(
            self, mock_print: Any,
            mock_Input: Any) -> None:
        """
        Test the main function of the program.
        """
        # Set up the mock for Input class:
        mock_input_instance = mock_Input.return_value
        mock_input_instance.get.return_value = ['SpiderMan', '256']

        # Execute the main function:
        main()

        # Check that get was called:
        mock_input_instance.get.assert_called_once()

        # Verify that print was called with the calculated cost:
        mock_print.assert_called_once_with(9)


if __name__ == '__main__':
    unittest.main()
