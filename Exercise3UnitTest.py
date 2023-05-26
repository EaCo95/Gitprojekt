from dataclasses import dataclass
from datetime import datetime

@dataclass
class Person:
    Birthdate: datetime
    Name: str = ""
    StreetAddress: str = ""
    PostalCode: int = 0
    PostArea: str = ""

    def NameTo(self, name):
        if len(name) > 1:
            self.Name = name
            return True
        return False
    
    def MoveInWith(self, another):
        self.StreetAddress = another.StreetAddress
        self.PostalCode = another.PostalCode
        self.PostArea = another.PostArea

