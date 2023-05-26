while True:
    pass
    text = input("Mata in en text: ")
    text = text.upper()
    if text == "Slut":
        break

longestSoFar = ""
while True:
    pass
    text = input("Ange en text: ")
    text = text.upper()
    if text == "Slut":
        break
    if len(text) > len(longestSoFar):           #len = length
        longestSoFar = text

        print(f"Längsta texten du skrev in var: {longestSoFar}")


def calculateBonus(baseSalary: float, age: int, IsBoss):

    bonus = 0
    if  age >= 30: #jag tolkar det som att...
        bonus = bonus + (baseSalary * 0.04)
    if IsBoss == True:
        bonus = bonus + 1000
        return bonus
    
    
