from dataclasses import dataclass
import datetime

@dataclass
class Drinks:

    Name: str
    Price: float

drinksMenu = []
Drink1 = Drinks("Screw driver", 120)
Drink2 = Drinks("Pina colada", 130)
Drink3 = Drinks("White Russian", 110)

drinksMenu.append(Drink1)
drinksMenu.append(Drink2)
drinksMenu.append(Drink3)

print("***** Happy Hour *****")
for Drinks in drinksMenu:
    print(f"{Drinks.Name} {Drinks.Price}")

def calculateDiscountedPrice(price):






















    currentDateandTime = datetime.datetime.now()
    currentHour = currentDateandTime.hour

    if currentHour >= 16 and currentHour < 17:
        return price * 0.8
    
    else:
         return price
    
    
    
    
    
 #   print("Happy Hour 20% discount!")

  #  else:
   #         return price
#print("No Happy Hour price!")


 