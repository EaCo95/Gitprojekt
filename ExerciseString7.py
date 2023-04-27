# Be användare mata in ett ord eller en mening. Programmet skall kontrollera om det

# ordet är en palindrom dvs om ordet blir likadant om man läser framifrån och bakifrån.

# Exempel på palindrom är namn som ”anna” eller ”otto” eller en mening som ”ni talar

# bra latin”. Meddela användaren om det är en palindrom eller ej.


# text = input("Mata in ett ord eller en mening: ")

# text.palindrome

text=input(("Enter a string:"))

if(text==text[::-1]):

    print("The string is a palindrome")

else:

    print("Not a palindrome")

    #Done