import unittest
from main import get_formatted_price


class PriceFormattingTestCase(unittest.TestCase):

    def test_empty_string_or_not_number(self):
        with self.assertRaises(ValueError):
            pretty_price = get_formatted_price("")
        with self.assertRaises(ValueError):
            pretty_price = get_formatted_price("abcde")

    def test_string_with_comma(self):
        pretty_price = get_formatted_price("1,0000000")
        self.assertEqual(pretty_price, "1")

    def test_with_fraction_part(self):
        pretty_price = get_formatted_price("1.34")
        self.assertEqual(pretty_price, "1.34")

    def test_int_part(self):
        prices = ["123", "1234", "12345", "123456"]
        expected_formatting = ["123", "1 234", "12 345", "123 456"]
        for price, pretty_price in zip(prices, expected_formatting):
            with self.subTest():
                self.assertEqual(pretty_price, get_formatted_price(price))

    def test_rounding_correctness(self):
        pretty_price = get_formatted_price("1321.21865601")
        self.assertEqual(pretty_price, "1 321.22")

    def test_negative_number_string(self):
        pretty_price = get_formatted_price("-1234")
        self.assertEqual(pretty_price, "-1 234")

    def test_zero(self):
        pretty_price = get_formatted_price("0")
        self.assertEqual(pretty_price, "0")

if __name__ == '__main__':
    unittest.main()
