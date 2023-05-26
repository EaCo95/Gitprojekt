# Skapa en klass Matratt
# Den ska ha ett namn, pris, typ, antal kalorier
# Typ kan man tänka sig Vegetarisk, Vegansk, Kött ? ÖVERKURS ENUM?
# Skapa upp några objekt och lägg i en lista.
# Skriv ut en dagens lunchmeny!

from dataclasses import dataclass

@dataclass
class Course:

    Name: str
    Price: float
    Type: str
    Calories: int

lunchmenu = []
Course1 = Course("Pannkakor", 100, "vegetarian", 30)
Course2 = Course("Korvstroganoff", 110, "meat", 100)
Course3 = Course("Morotssopoa", 90, "vegan", 50)
lunchmenu.append(Course1)
lunchmenu.append(Course2)
lunchmenu.append(Course3)

print("*** Dagens lunch ***")
for Course in lunchmenu:
    print(f"{Course.Name} {Course.Price} {Course.Type} {Course.Calories}")

