"""
Module that manages the cup data.
"""

from kattis_abc import Kattis
from collections.abc import MutableSequence
from typing import Any, Iterable, overload
from typing import List as TypedList


class Cup:
    """
    Cup class to store the information for the
    'Cup' objects.
    """

    def __init__(self, line: str) -> None:
        """
        Constructor for 'Cup'. This code defines the
        color and diameter of the given cups.

        :param: 'line' - a string that represents data for a cup.
        :return: None
        """
        parts = line.split()
        if parts[0].isdigit():
            self.__diameter = int(parts[0])
            self.__color = parts[1]
        else:
            self.__color = parts[0]
            self.__diameter = 2 * int(parts[1])

    @property
    def diameter(self) -> int:
        """
        Getter method for the diameter.

        :return: int
        """
        return self.__diameter

    @property
    def color(self) -> str:
        """
        Getter method for the color.

        :return: str
        """
        return self.__color


class Cup_List(MutableSequence[Cup]):
    """
    'List' class. This class is used to make
    a custom list of cups, that behaves similarly
    to Python's built-in lists.
    """

    def __init__(self) -> None:
        """
        Constructor for 'List'. Builds a list
        of cups.

        :return: None
        """
        self.__cups: TypedList[Cup] = []

    @property
    def cups(self) -> TypedList[Cup]:
        """
        Getter method for the 'cups' list. Allows
        external classes and methods to access the
        'cups' list.

        :return: TypedList[Cup]
        """
        return self.__cups

    def __len__(self) -> int:
        """
        Method to allow 'len' to
        be used on instances of 'List'.

        :return: int
        """
        return len(self.cups)

    @overload
    def __getitem__(self, index: int) -> Cup:
        """
        Overload method for '__getitem__'. Specifies
        that if '__getitem__' is called with 'index' as
        an 'int, an item of 'Cup' will be returned.
        :return: Cup
        """
        ...

    @overload
    def __getitem__(self, index: slice) -> MutableSequence[Cup]:
        """
        Overload method for '__getitem__'. Specifies
        that if '__getitem__' is called with 'index'
        as a 'slice', a MutableSequence of 'Cup will
        be returned.
        :return: MutableSequence[Cup]
        """
        ...

    def __getitem__(self, index: int | slice) -> Cup | MutableSequence[Cup]:
        """
        Method to allow indexing on
        instances of 'List'.

        :return: Cup or MutableSequence[Cup]
        """
        return self.cups[index]

    @overload
    def __setitem__(self, index: int, value: Cup) -> None:
        """
        Overload method for '__setitem__'. Specifies
        that if '__setitem__' is called with
        'index' as an 'int' and value as a 'Cup',
        None will be returned.
        :return: None
        """
        ...

    @overload
    def __setitem__(self, index: slice, value: Iterable[Cup]) -> None:
        """
        Overload method for '__setitem__'. Specifies
        that if '__setitem__' is called with 'index'
        as a 'slice' and 'value' as an Iterable[Cup],
        None will be returned.
        :return: None
        """
        ...

    def __setitem__(self, index: int | slice,
                    value: Cup | Iterable[Cup]) -> None:
        """
        Method to allow items within an
        instance of 'List' to be modified.

        :return: None
        """
        if isinstance(index, int):
            if not isinstance(value, Cup):
                raise TypeError("Expected item of type Cup" +
                                "got {}".format(type(value).__name__))
            self.cups[index] = value
        elif isinstance(index, slice):
            # Check that value is iterable and consists only of Cup instances
            if isinstance(value, Iterable) and all(isinstance
                                                   (item, Cup)
                                                   for item in value):
                self.cups[index] = list(value)
            else:
                raise TypeError("Expected Iterable of Cups")

    def __delitem__(self, index: int | slice) -> None:
        """
        Method to allow items within an instance
        of 'List' to be deleted.

        :return: None
        """
        del self.cups[index]

    def insert(self, index: int, value: Cup) -> None:
        """
        Method to allow items to be inserted into
        an instance of 'List'.

        :return: None
        """
        if not isinstance(value, Cup):
            raise TypeError(f"Expected item of type Cup, got {type(value)}")
        self.cups.insert(index, value)


class Sort(Kattis):
    """
    'Sort' class. This class is used to sort the given
    cups into a list based on their diameter.
    """

    def __init__(self, data_source: Any) -> None:
        """
        Constructor for 'Sort'.

        :param: data_source - The data that describes the color
        and size of the cups.
        :return: None
        """
        super().__init__(data_source)  # Initialize an instance of 'Kattis'

        # Initialize an instance of the 'Cup_List':
        self.__data: Cup_List = Cup_List()

        # Initialize an empty list to store the answer:
        self.__answer: list[Any] = []

    @property
    def data(self) -> Cup_List:
        """
        Getter method for 'data', which is the list of the
        given cups.

        :return: List
        """
        return self.__data

    @property
    def answer(self) -> TypedList[Any]:
        """
        Getter method for the answer.

        :return: list
        """
        return self.__answer

    @answer.setter
    def answer(self, value: TypedList[Any]) -> None:
        """
        Setter method for the answer. Allows for the modification
        of the list.

        :return: None
        """
        if isinstance(value, list):  # Validate that the value is a list
            self.__answer = value
        else:
            raise ValueError()

    def read_input(self) -> None:
        """
        Read the input, and add each cup to the 'data'
        list.

        :return: None
        """
        n = int(self._input_source().strip())  # Read the number of cups
        for _ in range(n):
            line = self._input_source().strip()
            self.data.append(Cup(line))  # Add cups to the 'data' list

    def solve(self) -> None:
        """
        Solve the problem by sorting the cups based on their size.

        :return: None
        """
        # Sort cups by size, modifying the '__answer' list in the process:
        self.answer = sorted(self.data, key=lambda cup: cup.diameter)

    def print_answer(self) -> None:
        """
        Print the answer by printing out the color of each cup,
        in ascending order based on size.

        :return: None
        """
        for cup in self.answer:
            print(cup.color)
