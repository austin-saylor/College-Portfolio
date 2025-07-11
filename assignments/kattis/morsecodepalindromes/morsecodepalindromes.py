from translator import Translator
from checkpalindrome import CheckPalindrome
import sys


class Main:
    def __init__(self, text: str) -> None:
        """Initialize the input text."""
        self._text = text

    @property
    def text(self) -> str:
        """Get the input text property."""
        return self._text

    @text.setter
    def text(self, new_text: str) -> None:
        """Set a new text value."""
        self._text = new_text

    def solution(self) -> int:
        """Take the input text, and get the solution."""
        text = self._text

        palindrome = 0

        if text != "":
            translator = Translator()
            morse_text = translator.translate(text)

            check = CheckPalindrome(morse_text)
            palindrome = check.isPalindrome()

            if palindrome:
                palindrome = 1
            else:
                palindrome = 0

        return palindrome


if __name__ == "__main__":
    text = sys.stdin.readline().strip()

    main = Main(text)  # Create an instance of Main with the input text
    solution = main.solution()  # Call the solution method

    print(solution)
