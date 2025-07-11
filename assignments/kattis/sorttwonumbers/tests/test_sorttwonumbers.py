import unittest
from sorttwonumbers import answer


class Test(unittest.TestCase):
    def test_1(test) -> None:
        in_1a = -26403
        in_1b = 28754
        test.assertEqual(answer(in_1a, in_1b), "-26403 28754")

        in_2a = 164820
        in_2b = 146060
        test.assertEqual(answer(in_2a, in_2b), "146060 164820")

        in_3a = 1182
        in_3b = 1460
        test.assertEqual(answer(in_3a, in_3b), "1182 1460")

        print("All test cases passed!")


if __name__ == '__main__':
    unittest.main()
