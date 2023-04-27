# Skapa ett program där användaren får upp fyra frågor om att mata in ett tal. Spara

# alla talen i en lista. Loopa igenom lista och ta fram det tal som är störst. Skriv

# tillbaka resultatet på skärmen för användaren

# tal1 = int(input("Mata in ett tal: "))


# if number1 >= number2:
#     if number1 >= number3:

#         largest = number1



# elif number2 >= number3:

#     largest = number2

# else:

#     largest = number3

# print(f"Det största talet är: {largest}")




tal1 = int(input("Mata in ett tal?"))


tal2 = int(input("Mata in ett tal?"))


tal3 = int(input("Mata in ett tal?"))


tal4 = int(input("Mata in ett tal?"))

my_Number_List = [tal1, tal2, tal3, tal4]

if tal1 >= tal2:
    if tal1 >= tal3:

            largest = tal1



elif tal2 >= tal3:

     largest = tal2

elif tal3 >= tal1:
      
      largest = tal3

else:
            largest = tal4

print(f"Det största talet är: {largest}")

# else:

#     largest = number3

# print(f"Det största talet är: {largest}")
