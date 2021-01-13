import unittest
from Unique_Character import unique_character

class Unique_CharacterTestCase(unittest.TestCase):

    def test_is_anagram(self):

        self.assertTrue(unique_character("anagram"))
    
    def test_is_lolololer(self):

        self.assertTrue(unique_character("lolololer"))



if __name__ == "__main__":
    unittest.main()