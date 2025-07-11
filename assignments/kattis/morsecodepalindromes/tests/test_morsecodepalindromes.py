import unittest
from translator import Translator
from checkpalindrome import CheckPalindrome


translator = Translator()
morse_text = ""
check = CheckPalindrome(morse_text)


class Test(unittest.TestCase):
    def test_1(test) -> None:
        text = "Borrow or Rob?"

        morse_text = translator.translate(text)
        check = CheckPalindrome(morse_text)
        palindrome = check.isPalindrome()

        test.assertEqual(palindrome, 0)

    def test_2(test) -> None:
        text = "Supercalifragilisticexpialidocious"

        morse_text = translator.translate(text)
        check = CheckPalindrome(morse_text)
        palindrome = check.isPalindrome()

        test.assertEqual(palindrome, 0)

    def test_3(test) -> None:
        text = "Sopranos"

        morse_text = translator.translate(text)
        check = CheckPalindrome(morse_text)
        palindrome = check.isPalindrome()

        test.assertEqual(palindrome, 1)

    def test_4(test) -> None:
        text = ""

        morse_text = translator.translate(text)
        check = CheckPalindrome(morse_text)
        palindrome = check.isPalindrome()

        test.assertEqual(palindrome, 0)

    def test_5(test) -> None:
        text = " "

        morse_text = translator.translate(text)
        check = CheckPalindrome(morse_text)
        palindrome = check.isPalindrome()

        test.assertEqual(palindrome, 0)

    def test_6(test) -> None:
        text = "€ € € € € € € € "

        morse_text = translator.translate(text)
        check = CheckPalindrome(morse_text)
        palindrome = check.isPalindrome()

        test.assertEqual(palindrome, 0)

    def test_7(test) -> None:
        text = "¾ ¾ ¾ ¾ ¾ ¾ ¾ ¾ ¾ ¾ "

        morse_text = translator.translate(text)
        check = CheckPalindrome(morse_text)
        palindrome = check.isPalindrome()

        test.assertEqual(palindrome, 0)


if __name__ == '__main__':
    unittest.main()
