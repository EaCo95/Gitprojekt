# Kasta två tärningar” och visa resultatet enligt skärmdump 
# ända tills man INTE svarar ”y” eller ”yes” på frågan om igen

# Kasta tärning 

# import random

# while True:
#     talet = random.randint(1, 7)
#     print(f"Talet blev {talet}")
#     svar = input("Vill du kasta en gång till j/n?")
# if  svar == "n":
#     break

import random

while True:
    Tärning1 = random.randint (1, 6)
    Tärning2 = random.randint (1, 6)
    print(f"Summan av kasten blev: {Tärning1} + {Tärning2}")
    svar = input("Vill du kasta igen y/yes?")

    if svar != "y":
    
        if svar !="yes":    
            break
    
    #Done