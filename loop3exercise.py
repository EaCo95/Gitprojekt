

# while True:
#     talet = random.randint(1, 7)
#     print(f"Talet blev {talet}")
#     svar = input("Vill du kasta en gång till j/n?")
# if  svar == "n":
#     break

# antalPaket = int(input("Mata in hur många mjökpaket som finns kvar: "))

# if antalPaket < 10:
    
#     print("Beställ 30 paket")

# elif antalPaket > 10-20:

#     print("Beställ 20 paket")

# else:

#     print("Du behöver inte beställa någon mjölk.")

# Skapa ett program där användaren

#     Får mata in två tal.
#     Skriv sedan till skärmen summan av de två talen.
#     Skriv sedan en fråga- Vill du fortsätta(J/N)?.
#     Svarar användaren J återupprepas punkt a-c
#     Svarar användaren N avbryts programmet


while True:

    tal1 = int(input("Mata in ett tal: "))
    tal2 = int(input("Mata in ett till tal:"))

    summa = tal1 + tal2
    print(f"Summan blev {summa}")
    svar = input("Vill du fortsätta j/n?")

    if svar == "n":
        break
  

# Done

# print(f"Summan av de två talen blir: {tal}")
# svar == input("Vill du fortsätta j/n?")
# # if svar == "n":
# #     break
