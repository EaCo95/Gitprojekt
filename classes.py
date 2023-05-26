from dataclasses import dataclass

@dataclass
class Team:
     Namn: str = ""
     FoundedYear:int=0
     Players = []


class Player:
     Namn: str=""
     Age: int=0









class Person:
      Name: str = ""
      StreetAddress: str = ""
      PostalCode: int = 0
      city: str = ""
      Age: int = 0

def SetAge(self, newAge):
    if newAge >= 0 and newAge <= 140:
        self.Age = newAge

def MoveTo(self, streetAdr, postal, city):
      self.StreetAddress = streetAdr
      self.City = city
      self.Postalcode = postal
      
p = Person("Stefan")
p.MoveTo("Testgatan 12", 11122, "Teststad")
p.SetAge(50)

p = Person()
p.StreetAddress = "Testgatan 27"
p.City = "Teststad"
p.PostalCode = 54932
print(f"{p.Name}")

# p = Person()
# p.Name = "Stefan"









# @dataclass
# class Rectangle:
#     width: int = 0
#     height: int = 0

#     def calculateArea(self): # denna parameter self är alltid osynlig. self används istället för this (finns i cs)
#         return self.width * self.height

# r = Rectangle()
# r.width =  20
# r.height = 10
# x = r.calculateArea()
# print(x)

# r2 = Rectangle()
# r2.width = 10
# r2.height = 30
# x = r2.calculateArea()
# print(x)









# def calculateArea(rect):  # function (denna funktion ska ligga inuti klassen.)
#     area = rect.width * rect.height
#     return area
    
# r = Rectangle()
# r.width =  20
#r.height = 10
#r.calculateArea()

# r2 = Rectangle()
# r2.width = 10
# r2.height = 3
# print(calculateArea(r))


    






# @dataclass
# class Person:
#     Name: str = ""
#     StreetAddress: str = ""
#     PostalCode: int = 0
#     city: str = ""

# p = Person()
# p.Name = "Stefan"











# @dataclass
# class HouseBlueprint:
#     color: str = ""
#     nrOfWindows: int = 0
#     Address: str = ""

# mittHus = HouseBlueprint("Brown", 12, "Testgatan 12")
# mittHus.color = "Brown"
# mittHus.nrOfWindows = 12
# mittHus.Address = "Testgatan 12"

# syrransHus = HouseBlueprint()
# syrransHus.color = "Rött"
# syrransHus.nrOfWindows = 12
# syrransHus.Address = "Testgatan 15"


# print("Hello")
    
