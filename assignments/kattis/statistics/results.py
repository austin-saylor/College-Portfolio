from calculator import Calculator


class Results(Calculator):
    def __init__(self, case: list[int], case_num: int):
        """
        Initialize the 'Results' class.
        """
        super().__init__(case[1:])
        self.__case = case
        self.__case_num = case_num

    @property
    def _case(self) -> list[int]:
        """
        Get the case property.
        """
        return self.__case

    @_case.setter
    def _case(self, newCase: list[int]) -> None:
        """
        Set the value of the case.
        """
        self.__case = newCase

    @property
    def _case_num(self) -> int:
        """
        Get the case_num property.
        """
        return self.__case_num

    @_case_num.setter
    def _case_num(self, newCaseNum: int) -> None:
        """
        Set the value of 'case_num'.
        """
        self.__case_num = newCaseNum

    def get(self) -> str:
        """
        Use the calculator to compile the
        results of the case.
        """
        minimum = self.minimum_number()
        maximum = self.maximum_number()
        range_val = self.range_value()

        return f"Case {self._case_num}: {minimum} {maximum} {range_val}"
