# for(int year = 1972;
# example 1
#for year in range(1972,1980):   # första värdet är inklusive och sista värdet är exklusive
 #   print(f"År /{year}")

# Skriva ut alla sommar-os år
# 1896, 1900, 1904, 1908

for(int year = 1972; year < 1980; year = year  + 1): 

for year  in range (1972,1980, 1): # (1) är onödig
    print(f"Ett år {year}")


for year  in range (1896,1949, 4): # plussa på med 4
    print(f"Sommar os {year}")

for year  in range (2000,1972, -4): # gå bakåt med 4
    print(f"Ett  år {year}")


#for i in range (10):
 #   print(f"Python är kul!")


#for i in range (0,10): # eller (10): som ovan men helst (0,10):  0,10, 1 är samma!
 #   print(f"Python är kul!")



 # While-loops

#year = 1972

# while year < 1980:
#     print(f"Ett år" {year})
#     year = year + 1


# oändlig

#while True:

    #print ("RAST!!!")

 # Kasta tärning 

# import random

# while True:
#     talet = random.randint(1, 7)
#     print(f"Talet blev {talet}")
#     svar = input("Vill du kasta en gpång till j/n?")
# if  svar == "n":
#     break


    #print("RAST!!!")



# for tal in range (10, 20 + 1):
#     tal1 = int(input("Ange start"))
#     tal2 = int(input("Ange slut"))
#     print(tal)

# exercise  loop4

import random

summa = 0
for i in range (0,10):  # (1,11)
    tal = int(input(f"Mata in tal nummer {i+1}"))

    print("Summan av alla talen blev {summa}")

