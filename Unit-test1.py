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

class Palin:
    def test_when_palindrom_then_should_return_true(self):
    
    PalindromTests(unittest.TestCase):
        IsPalindrom(input)
        s = input.replace(" ", "").lower()
        backwards = ""
        for part in s:
            backwards = part + backwards

        return backwards == s

    while True:
        print(IsPalindrom(input("Skriv in: ")))

unittest.main()








