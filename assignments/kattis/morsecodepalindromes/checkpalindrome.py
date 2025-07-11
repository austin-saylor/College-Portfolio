"""
Palindrome-checking module. This module
takes a given string of morsecode, and
checks if it is a palindrome.
"""


class CheckPalindrome:
    def __init__(self, morse_text: str) -> None:
        """Initialize the morse code text."""
        self._morse_text = morse_text

    @property
    def morse_text(self) -> str:
        """Get the morse_text property."""
        return self._morse_text

    @morse_text.setter
    def morse_text(self, new_morse_text: str) -> None:
        """Set a new morse_text value."""
        self._morse_text = new_morse_text

    def isPalindrome(self) -> int:
        """Check if the morse code is a palindrome."""
        if self.morse_text == "":
            return 0
        return self._morse_text == self._morse_text[::-1]
