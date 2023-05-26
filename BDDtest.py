import unittest
from amount import BankAccount


class BankAccount:
  def __init__(self, id):
    self.id = id
    self.balance = 0

  def withdraw(self, amount):
    
        #Given
    if self.balance >= amount:
      #When
      self.balance -= amount
      return True
    return False

  def deposit(self, amount):
    #Then
    self.balance += amount
    return True
  




#   def test_when_dividable_by_3_should_return_fizz(self):
#         # arrange
#         tal = 15
#         # act
#         result = GetFizzBuzz(tal)
#         #assert
#         self.assertEqual("Fizz",result)