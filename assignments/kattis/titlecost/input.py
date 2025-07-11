class Input:
    def __init__(self) -> None:
        """
        Initialize the input string.
        """
        self._input_str: list[str] = []

    @property
    def input_str(self) -> list[str]:
        return self._input_str

    @input_str.setter
    def input_str(self, value: list[str]) -> None:
        if not isinstance(value, list):
            raise ValueError("input_str must be a list of strings")
        if not all(isinstance(item, str) for item in value):
            raise ValueError("All items in input_str must be strings")
        self._input_str = value

    def get(self) -> list[str]:
        """
        Split the input into two components:
        the move name, and the cap on the cost.
        """
        self.input_str = input().split()
        return self.input_str
