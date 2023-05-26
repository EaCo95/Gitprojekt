# for tal in range (10, 20 + 1):
#     tal1 = int(input("Ange start"))
#     tal2 = int(input("Ange slut"))
#     print(tal)

# exercise  loop4


# menu = {}

# print("Gör ditt val")

# val1 = GetFizzBuzz:
# val2 = int(input("Välj en siffra:"))
# print(GetFizzBuzz)


# def GetFizzBuzz(num):

#     if (num % 3 == 0):
#         return "Fizz"

#     if num % 5 == 0:
#         return "Buzz"

#     if num % 3 == 0 and num % 5 == 0:
#             return "FizzBuzz"

#     else:
#         return str(num)

import unittest
from fizzbuzz import GetFizzBuzz

class FizzbuzzTest(unittest.TestCase):
    def test_when_dividable_by_3_should_return_fizz(self):
        # arrange
        tal = 15
        # act
        result = GetFizzBuzz(tal)
        #assert
        self.assertEqual("Fizz",result)

    def test_when_dividable_by_5_should_return_buzz(self):
        #arrange
        tal = 20
        #act
        result = GetFizzBuzz(tal)
        #assert
        self.assertEqual("Buzz", result)

    def test_when_dividable_by_3_and_5_should_return_fizzbuzz(self):
        #arrange
        tal = 15
        # act
        result = GetFizzBuzz(tal)
        #assert
        self.assertEqual("FizzBuzz", result)

    def test_when_not_dividable_by_3_or_5_should_return_number_as_string(self):
        tal = 33
        result =GetFizzBuzz(tal)
        self.assertEqual("33", result)

unittest.main()



