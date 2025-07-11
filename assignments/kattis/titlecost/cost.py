class Cost:
    def __init__(self, s: str, c: float) -> None:
        """
        Initialize the two components of the input string.
        """
        self._s = s
        self._c = c

    @property
    def s(self) -> str:
        """
        Get the string component.
        """
        return self._s

    @property
    def c(self) -> float:
        """
        Get the float component.
        """
        return self._c

    def calculate(self) -> float:
        """
        Calculates cost as the length of the string s,
        then compares this value with the float c. The smallest
        of the two values is determined to be the final cost.
        """
        cost = len(self.s)
        final_cost = min(cost, self.c)

        return final_cost
