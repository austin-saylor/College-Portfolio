"""
Translator module. This module defines an
alphabet-to-morsecode dictionary, and uses
it to translate a given alphabetic string into
morsecode.
"""


class Translator:
    def __init__(self) -> None:
        """Initialize a dictionary to use for translating to morse-code."""
        self._morse_code = {
            'A': ".-", 'B': "-...", 'C': "-.-.", 'D': "-..",
            'E': ".", 'F': "..-.", 'G': "--.", 'H': "....",
            'I': "..", 'J': ".---", 'K': "-.-", 'L': ".-..",
            'M': "--", 'N': "-.", 'O': "---", 'P': ".--.",
            'Q': "--.-", 'R': ".-.", 'S': "...", 'T': "-",
            'U': "..-", 'V': "...-", 'W': ".--", 'X': "-..-",
            'Y': "-.--", 'Z': "--..", '0': "-----", '1': ".----",
            '2': "..---", '3': "...--", '4': "....-", '5': ".....",
            '6': "-....", '7': "--...", '8': "---..", '9': "----."
        }

    @property
    def morse_code(self) -> dict[str, str]:
        """Get the Morse code dictionary."""
        return self._morse_code

    @morse_code.setter
    def morse_code(self, new_morse_code: dict[str, str]) -> None:
        """Set a new Morse code dictionary."""
        self._morse_code = new_morse_code

    def translate(self, text: str) -> str:
        """Translate the given string into morse code."""
        self.morse_text = ""
        for letter in text.upper():
            if letter == " ":
                continue
            else:
                self.morse_text += self._morse_code.get(letter, '')
        return self.morse_text
