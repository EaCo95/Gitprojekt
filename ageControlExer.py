# Skapa ett program där användaren får en fråga om att mata in sin ålder. 
# Skapa en metod som tar emot det inmatade värdet och kontrollerar om användaren är myndig dvs över 18 år.
# Metoden returnerar sant eller falskt. Anropa metoden och skriv ut på skärmen om användaren är myndig eller ej.


def ageControl(age):

  if age < 18:
             return False

           
  if age > 18:
             return True
  

 
while True:

    age = int(input("Ange din ålder: "))

    legal = ageControl(age)

    if legal == True:
          
        print("You're legal")

    else:
        print("You're not legal")


# def controllAge(age):

#   if age < 18:

#     return False

 

#     if age > 18:

#         return True

 

# while True:

#     age= int(input("Ange din ålder: "))

#     ok = controllAge(age)

#     if ok == True:

#       print("Yes, good age")

#     else:

#       print("No, too young")