# Be användaren mata in en mailadress. Programmet skall kontrollera att inmatningen är

# rätt dvs att det finns ett @ tecken och att det finns en . med 2 eller 3 tecken efter.

# Meddela användaren om det är rätt eller felaktig adress

# antal = len(result)
# count = 0
# for i in range(0, antal):
#     if result[i] == "*":
#         count = count + 1
#         print(f"Det finns {count} i meningen: ")


# email = input("Please enter your email address")
# while '@' not in email:
#     email = input("invalid email address, please re-enter")

#     lastPoint = input.rfind('.')
#     if lastPoint == -1:
#             return False

# print("Your email address had been registered")

# antal = len(mailadress)
# count = 0

# for i in range(0,antal):
#     if mailadress[i] == ""

def IsValidEmail(input):
    if not  '@' in input:
        return False
    lastPoint = input.rfind('.')
    if lastPoint == -1:
        return False
    antalEfter = len(input) - lastPoint -1
    if antalEfter == 2 or antalEfter == 3:
        return True
    return False

print(IsValidEmail("-123424@gmail.com"))