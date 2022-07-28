"""
Module to perform tests on translation functions
"""
import unittest
from . translator import english_to_french, french_to_english

class TestTranslation(unittest.TestCase):
    """
    Tests to verify translator is working accurately
    """
    def test_english_to_french(self):
        """
        English to French Tests
        """
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        self.assertEqual(english_to_french('yes'), 'Oui')
        self.assertEqual(english_to_french('thanks'), 'Merci')

    def test_french_to_english(self):
        """
        French to English Tests
        """
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        self.assertEqual(french_to_english('oui'), 'Yes')
        self.assertEqual(french_to_english('merci'), 'Thank you')

if __name__=='__main__':
    unittest.main()