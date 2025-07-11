"""
Testing module.
"""

import unittest
from unittest.mock import MagicMock, patch
from io import StringIO
from kattis_abc import Kattis
from cups import main
from cup_data import Cup, Cup_List, Sort
from typing import Any
from hypothesis import given, strategies as st


class TestCup(unittest.TestCase):
    """
    Class containing testing for the
    'Cup' object.
    """

    def test_cup_initialization(self) -> None:
        """
        Tests cup initialization.
        :return: None
        """
        cup: Cup = Cup("blue 10")
        self.assertEqual(cup.color, "blue")
        self.assertEqual(cup.diameter, 20)

        cup = Cup("20 red")
        self.assertEqual(cup.color, "red")
        self.assertEqual(cup.diameter, 20)


class TestKattis(unittest.TestCase):
    """
    Class containing the tests for
    Kattis ABC.
    """
    @patch.multiple(Kattis, __abstractmethods__=set())
    def test_initialization(self) -> None:
        """
        Test initialization of the Kattis ABC class.

        :return: None
        """
        self.kattis = Kattis("data source")  # type: ignore

    @patch.multiple(Kattis, __abstractmethods__=set())
    def test_kattis(self) -> None:
        """
        Test the abstract methods in the
        Kattis ABC class.

        :return: None
        """
        self.kattis = Kattis("data source")  # type: ignore
        self.kattis.read_input()
        self.kattis.data
        self.kattis.answer
        self.kattis.solve()
        self.kattis.print_answer()


class TestCupList(unittest.TestCase):
    """
    Class containing the tests for 'Cup_List'.
    """

    def setUp(self) -> None:
        """
        set up an instance of 'Cup_List'.

        :return: None
        """
        self.cups: Cup_List = Cup_List()
        self.cups.append(Cup("blue 10"))
        self.cups.append(Cup("red 20"))

    def test_insert(self) -> None:
        """
        Test insertion into the cup list.

        :return: None
        """
        new_cup: Cup = Cup("yellow 5")
        self.cups.insert(1, new_cup)

        self.assertEqual(self.cups[1].color, "yellow")
        self.assertEqual(self.cups[1].diameter, 10)

        with self.assertRaises(TypeError):
            new_cup = "not_a_cup"  # type: ignore[assignment]
            self.cups.insert(2, new_cup)

    def test_len(self) -> None:
        """
        Test the 'len' function on
        'Cup_List'.

        :return: None
        """
        self.assertEqual(len(self.cups), 2)

    def test_getitem_with_int(self) -> None:
        """
        Test the '__getitem__' method of
        'Cup_List', when 'index' is
        an 'int'.

        :return: None
        """
        cup = self.cups[0]

        self.assertIsInstance(cup, Cup)

        self.assertEqual(cup.color, "blue")
        self.assertEqual(cup.diameter, 20)

    def test_getitem_with_slice(self) -> None:
        """
        Test the '__getitem__' method of
        'Cup_List', when 'index' is
        a 'slice'.

        :return: None
        """
        cup_slice = self.cups[0:2]

        self.assertIsInstance(cup_slice, list)

        self.assertEqual(cup_slice[0].color, "blue")
        self.assertEqual(cup_slice[0].diameter, 20)

        self.assertEqual(cup_slice[1].color, "red")
        self.assertEqual(cup_slice[1].diameter, 40)

    def test_setitem_with_int(self) -> None:
        """
        Test the '__setitem__' method of
        'Cup_List', when 'index' is
        an 'int'.

        :return: None
        """
        cup_list = Cup_List()
        cup = Cup("red 10")
        cup_list.append(cup)
        index_int = 0
        cup_list.__setitem__(index_int, cup)

        with self.assertRaises(TypeError) as type_explanation:
            cup_list[0] = "not_a_cup"  # type: ignore
        self.assertTrue(
            "Expected item of type Cup" in str(type_explanation.exception))

    def test_setitem_with_slice(self) -> None:
        """
        Test the '__setitem__' method of
        'Cup_List', when 'index' is
        a 'slice'.

        :return: None
        """
        new_cups = [Cup("yellow 5"), Cup("purple 8")]
        self.cups[0:2] = new_cups

        self.assertEqual(len(self.cups), 2)
        self.assertEqual(self.cups[0].color, "yellow")
        self.assertEqual(self.cups[1].color, "purple")

        with self.assertRaises(TypeError) as explanation:
            self.cups[0:2] = [Cup("orange 12"), "not_a_cup"]  # type: ignore
        self.assertTrue(
            "Expected Iterable of Cups" in str(explanation.exception))

    def test_delitem_with_int(self) -> None:
        """
        Test the deletion of items from the
        cup list.

        :return: None
        """
        del self.cups[1]

        self.assertEqual(len(self.cups), 1)
        self.assertEqual(self.cups[0].color, "blue")


class TestSort(unittest.TestCase):
    """
    Class to test the methods that
    the program uses to sort the cups
    and display the answers.
    """
    @patch('sys.stdin', new_callable=StringIO)
    def test_sorting_cups(self, mock_input: Any) -> None:
        """
        Test the sorting functionality.

        :return: None
        """
        mock_input.write("3\nblue 9\n10 red\n15 yellow\n")
        mock_input.seek(0)
        sorter: Sort = Sort(lambda: mock_input.readline().strip())
        sorter.read_input()
        sorter.solve()

        # Checking if sorting by diameter is correct
        self.assertEqual(sorter.answer[0].color, "red")
        self.assertEqual(sorter.answer[1].color, "yellow")
        self.assertEqual(sorter.answer[2].color, "blue")

        # Ensure correct diameters
        self.assertEqual(sorter.answer[0].diameter, 10)
        self.assertEqual(sorter.answer[1].diameter, 15)
        self.assertEqual(sorter.answer[2].diameter, 18)

    def test_answer_setter(self) -> None:
        """
        Test the setter method for
        'answer'.

        :return: None
        """
        sort = Sort("data source")
        ans = [Cup("orange 10"), Cup("20 violet")]
        sort.answer = ans
        self.assertIs(sort.answer, ans)

        with self.assertRaises(ValueError):
            sort.answer = "Non-list"  # type: ignore[assignment]

    def test_print_answer(self) -> None:
        """
        Test the printing functionality.

        :return: None
        """
        cups: list[Cup] = [Cup("blue 9"), Cup("10 red"), Cup("15 yellow")]
        sorter: Sort = Sort(lambda: None)
        sorter.answer = sorted(cups, key=lambda cup: cup.diameter)
        with patch('sys.stdout', new=StringIO()) as mock_output:
            sorter.print_answer()
            self.assertEqual(mock_output.getvalue(), "red\nyellow\nblue\n")


class TestInput(unittest.TestCase):
    """
    Class to test how the program handles
    various inputs.
    """
    @given(
        n=st.integers(max_value=20),
        cup_data=st.lists(
            st.tuples(
                st.text(min_size=1, max_size=20),
                st.integers(max_value=999)
            ),
            min_size=1,
            max_size=20
        )
    )
    def test_readinput_with_colorfirst(
        self,
        n: int,
        cup_data: list[tuple[str, int]]
    ) -> None:
        """
        Test input that is in the format of
        color first, radius second.

        :return: None
        """
        # Create mock input where each tuple is (color, radius)
        data_source = MagicMock()

        # Simulate color-first format:
        inputs = [
            str(n)
        ] + [
            f"{color} {radius}"
            for color, radius in cup_data
        ]
        data_source._input_source.side_effect = iter(inputs)

        # Initialize the Sort class with the mocked data source
        instance = Sort(data_source)
        instance.read_input()

        for i, cup in enumerate(instance.data):
            self.assertIsInstance(cup, Cup)
            expected_color = cup_data[i][0]

            # Diameter is double the radius:
            expected_diameter = 2 * cup_data[i][1]

            self.assertTrue(cup.color, expected_color)
            self.assertTrue(cup.diameter, expected_diameter)

    @given(
        n=st.integers(max_value=20),
        cup_data=st.lists(
            st.tuples(
                st.integers(max_value=999),
                st.text(min_size=1, max_size=20)
            ),
            min_size=1,
            max_size=20
        )
    )
    def test_readinput_with_diameterfirst(
        self,
        n: int,
        cup_data: list[tuple[int, str]]
    ) -> None:
        """
        Test input that is in the format of
        diameter first, color second.

        :return: None
        """
        # Create mock input where each tuple is (diameter, color)
        data_source = MagicMock()

        # Simulate diameter-first format:
        inputs = [
            str(n)
        ] + [
            f"{diameter} {color}"
            for diameter, color in cup_data
        ]
        data_source._input_source.side_effect = iter(inputs)

        # Initialize the Sort class with the mocked data source
        instance = Sort(data_source)
        instance.read_input()

        for i, cup in enumerate(instance.data):
            self.assertIsInstance(cup, Cup)
            expected_diameter = cup_data[i][0]
            expected_color = cup_data[i][1]

            self.assertTrue(cup.diameter, expected_diameter)
            self.assertTrue(cup.color, expected_color)


class TestMain(unittest.TestCase):
    """
    Class containing the tests for
    the main module, 'cups.py'.
    """

    @patch('cup_data.Sort.read_input')
    @patch('cup_data.Sort.solve')
    @patch('cup_data.Sort.print_answer')
    def test_main(self, mock_readinput: Any,
                  mock_solve: Any, mock_printanswer: Any) -> None:
        """
        Tests the 'main' function, where the rest
        of the program is executed.

        :return: None
        """
        main()

        mock_readinput.assert_called_once()
        mock_solve.assert_called_once()
        mock_printanswer.assert_called_once()


if __name__ == '__main__':
    unittest.main()
