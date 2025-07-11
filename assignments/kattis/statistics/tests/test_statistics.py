import io
import unittest
from unittest.mock import patch
from results import Results
from calculator import Calculator
from program import Program
from hypothesis import given, strategies as st, settings, Verbosity


class Test(unittest.TestCase):
    @given(numbers=st.lists(st.integers(), min_size=1))
    def test_numbers_getter(self, numbers: list[int]) -> None:
        """
        Test the getter method
        for 'numbers'.
        """
        calculator = Calculator(numbers)

        self.assertEqual(calculator._numbers, numbers)

    @given(numbers=st.lists(st.integers(), min_size=1))
    def test_numbers_setter(self, numbers: list[int]) -> None:
        """
        Test the setter method
        for 'numbers'.
        """
        calculator = Calculator(numbers)

        # Set a new case
        newNumbers = numbers + [1]
        calculator._numbers = newNumbers

        self.assertEqual(calculator._numbers, newNumbers)

    @given(case=st.lists(st.integers(), min_size=1), case_num=st.integers())
    def test_case_getter(self, case: list[int], case_num: int) -> None:
        """
        Test the getter method
        for 'case'.
        """
        object = Results(case, case_num)

        self.assertEqual(object._case, case)

    @given(case=st.lists(st.integers(), min_size=1), case_num=st.integers())
    def test_case_setter(self, case: list[int], case_num: int) -> None:
        """
        Test the setter method
        for 'case'.
        """
        object = Results(case, case_num)

        # Set a new case
        newCase = case + [1]
        object._case = newCase

        self.assertEqual(object._case, newCase)

    @given(case=st.lists(st.integers(), min_size=1), case_num=st.integers())
    def test_casenum_getter(self, case: list[int], case_num: int) -> None:
        """
        Test the getter method
        for 'case_num'.
        """
        object = Results(case, case_num)

        self.assertEqual(object._case_num, case_num)

    @given(case=st.lists(st.integers(), min_size=1), case_num=st.integers())
    def test_casenum_setter(self, case: list[int], case_num: int) -> None:
        """
        Test the setter method
        for 'case_num'.
        """
        object = Results(case, case_num)

        # Set a new case number
        newCaseNum = case_num + 1
        object._case_num = newCaseNum

        self.assertEqual(object._case_num, newCaseNum)

    @settings(max_examples=100, verbosity=Verbosity.verbose, derandomize=False)
    @given(numbers=st.lists
           (st.integers(min_value=int(-1e12), max_value=int(1e12)),
            min_size=0, max_size=int(1e12)))
    def test_min(self, numbers: list[int]) -> None:
        """
        Test the calculation
        of the minimum value.
        """
        if numbers == []:
            self.assertRaises(ValueError)
        else:
            calculate = Calculator(numbers)
            expected = str(min(numbers))

            result = calculate.minimum_number()
            self.assertEqual(result, expected)

    @settings(max_examples=100, verbosity=Verbosity.verbose, derandomize=False)
    @given(numbers=st.lists
           (st.integers(min_value=int(-1e12), max_value=int(1e12)),
            min_size=0, max_size=int(1e12)))
    def test_max(self, numbers: list[int]) -> None:
        """
        Test the calculation
        of the maximum value.
        """
        if numbers == []:
            self.assertRaises(ValueError)
        else:
            calculate = Calculator(numbers)
            expected = str(max(numbers))

            result = calculate.maximum_number()
            self.assertEqual(result, expected)

    @settings(max_examples=100, verbosity=Verbosity.verbose, derandomize=False)
    @given(numbers=st.lists
           (st.integers(min_value=int(-1e12), max_value=int(1e12)),
            min_size=0, max_size=int(1e12)))
    def test_range(self, numbers: list[int]) -> None:
        """
        Test the calculation
        of the range value.
        """
        if numbers == []:
            self.assertRaises(ValueError)
        else:
            calculate = Calculator(numbers)
            expected = str(max(numbers) - min(numbers))

            result = calculate.range_value()
            self.assertEqual(result, expected)

    @given(case=st.lists
           (st.integers(min_value=-1000000, max_value=1000000), min_size=2),
           case_num=st.integers())
    def test_results(self, case: list[int], case_num: int) -> None:
        """
        Test the compilation of the results
        through the 'Results' class.
        """
        results = Results(case, case_num)
        result = results.get()

        expected_format = f"Case {case_num}:"

        self.assertIn(expected_format, result)

    def test_program(self) -> None:
        """
        Test the main flow of the program through
        the 'Program' class. This test case was
        sourced from ChatGPT.
        """
        inputs = iter(['1 2 3', '', '4 5 6', ''])

        def mock_input() -> str:
            try:
                return next(inputs)
            except StopIteration:
                raise EOFError

        program = Program()
        with patch('builtins.input', new=mock_input):
            with patch('sys.stdout', new_callable=io.StringIO) \
                    as fake_out:
                program.run()
                fake_output = fake_out.getvalue()
                self.assertIn('Case 1: 2 3 1\nCase 2: 5 6 1\n', fake_output)

    @given(string=st.text())
    def test_str_input(self, string: str) -> None:
        """
        Test the behavior of the program
        when given non-numeric strings as input.
        """
        inputs = iter(string)

        def mock_input() -> str:
            try:
                return next(inputs)
            except StopIteration:
                raise EOFError

        program = Program()
        with patch('builtins.input', new=mock_input):
            with patch('sys.stdout', new_callable=io.StringIO):
                program.run()
                self.assertRaises(ValueError)


if __name__ == '__main__':
    unittest.main()
