import unittest
from translator import english_to_french, french_to_english


class Test(unittest.TestCase):
    """doc string here"""

    def test_eng_fr(self):
        """doc string here"""
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        self.assertEqual(english_to_french(), 'Aucune donnée')

    def test_fr_eng(self):
        """doc string here"""
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        self.assertEqual(french_to_english(), 'No data')


if __name__ == '__main__':
    unittest.main()
