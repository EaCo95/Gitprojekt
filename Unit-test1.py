import unittest
from ispalindrom import IsPalindrom

class PalindromTests(unittest.TestCase):
    def IsPalindrom(input):
        s = input.replace(" ", "").lower()
        backwards = ""
        for part in s:
            backwards = part + backwards

        return backwards == s

    while True:
        print(IsPalindrom(input("Skriv in: ")))

unittest.main()















import unittest
from ispalindrom import IsPalindrom

class PalindromTests(unittest.TestCase):
    def test_when_palindrom_then_should_return_true(self.unittest):
    
    PalindromTests(unittest.TestCase):
        IsPalindrom(input)
        s = input.replace(" ", "").lower()
        backwards = ""
        for part in s:
            backwards = part + backwards

        return backwards == s


    def test_when_not_palindrom_then_should_return_false(self.unittest):


    def test_when_space_in_palindrom_should_return_true

    while True:
        print(IsPalindrom(input("Skriv in: ")))

unittest.main()








