import unittest
from ispalindrom import IsPalindrom

class PalindromTests(unittest.TestCase):
    def test_when_palindrom_then_should_return_true(self):
        #arrange
        texten = "ANNA"
        #act
        result = IsPalindrom(texten)
        #assert
        self.assertTrue(result)
        #self.assertEqual(result, True)

    def test_when_not_palindrom_then_should_return_false(self):
        texten = "ANNE"
        result = IsPalindrom(texten)
        self.assertFalse(result)


    def test_when_palindrom_and_mixed_casing_then_should_return_true(self):
        texten = "ANNa"
        result = IsPalindrom(texten)
        self.assertTrue(result)


    def test_when_palindrom_and_space_then_should_return_true(self):
        texten = "ANN a"
        result = IsPalindrom(texten)
        self.assertTrue(result)




unittest.main()