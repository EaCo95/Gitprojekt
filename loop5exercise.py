# Skapa ett program där användaren får mata in ett tal. Låt sedan programmet skriva ut

# alla siffor som är mindre än det inmatade talet men större än 0. Lös detta med en

# loop.

# summa = 0
# for i in range (0,10):  # (1,11)
#     tal = int(input(f"Mata in tal nummer {i+1}"))

#     print("Summan av alla talen blev {summa}")




# tal = int(input("Mata in ett tal: "))


# while (tal > 0):
#     print(tal)
#     tal -= 1
    

    #print(f"Alla siffror som är mindre än 0 {tal}")


    # for year  in range (2000,1972, -4): # gå bakåt med 4
    # print(f"Ett  år {year}")


tal = int(input("Mata in ett tal: "))

for i in range(tal -1, 0, -1):
    print(i)

    #Done
