#TDD=Test Driven Development

import unittest
from calculateSalary import *


class SalaryTests(unittest.TestCase):
    def test_when_hoursworked_8_multiplied_with_hourlysalarly_200_equals_Salary(self):

    #arrange
        hoursWorked = 10
        hourlySalary = 100
    #act
        result = calculateSalary(hoursWorked, hourlySalary)
    #assert
        self.assertEqual(1000,result)


    def test_when_age_is_between_25_return_5_percent_bonus(self):

        age = 25

        result = calculateBonus(age,"")

        self.assertEqual("5%", result)

    def test_when_age_is_45_return_5_percent_bonus(self):

        age = 45

        result = calculateBonus(age,"")

        self.assertEqual("6%", result)

    def test_when_age_is_over_45_return_6_percent_bonus(self):

        age = 47
        
        result = calculateBonus(age, "")

        self.assertEqual("6%", result)

    def test_when_name_is_Stefan_return_220kr_bonus(self):

        name = "Stefan"

        result = calculateBonus(30,name)

        self.assertEqual("220kr", result)






unittest.main()