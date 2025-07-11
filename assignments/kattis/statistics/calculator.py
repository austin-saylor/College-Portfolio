class Calculator:
    def __init__(self, numbers: list[int]):
        self.__numbers = numbers

    @property
    def _numbers(self) -> list[int]:
        """
        Get the numbers property.
        """
        return self.__numbers

    @_numbers.setter
    def _numbers(self, newNumbers: list[int]) -> None:
        """
        Set the value of 'numbers'.
        """
        self.__numbers = newNumbers

    def minimum_number(self) -> str:
        """
        Calculate the minimum value in the set of numbers.
        """
        minimum = min(self._numbers)
        return str(minimum)

    def maximum_number(self) -> str:
        """
        Calculate the maximum value in the set of numbers.
        """
        maximum = max(self._numbers)
        return str(maximum)

    def range_value(self) -> str:
        """
        Calculate the range of values in the set of numbers.
        """
        maximum = max(self._numbers)
        minimum = min(self._numbers)
        range_val = int(maximum) - int(minimum)
        return str(range_val)
