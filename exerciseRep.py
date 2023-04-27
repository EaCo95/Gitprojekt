# string test = "Hej!";
# int antal = test.Length();  #css


fult = "läxa"
fult2 = "grönsaker"
while True:

    txt = input("Skriv in: ")
    txt = txt.lower()
    txt = txt.replace(fult, "****")
    txt = txt.replace(fult2, "********")
    print(txt)





#Chatt

fult = "läxa"
fult2 = "grönsaker"
while True:

    txt = input("Skriv in: ")
    txt = txt.lower()
    if txt.find(fult) == -1: # finns inte
        if txt.find(fult2) == -1:
            print(txt)
            continue
    print("Inga fula ord i vår chat")
    break

    # if txt.find(fult) != -1 or txt.find(fult2) != -1:
    #     print("inga fula ord i vår chat")
    #     break
    print(txt)







namn = "Evie"
i = 1
namn = namn.lower()
i = i + 1
print(namn)

while True:
    namn = input("Mata in namn")

    if namn.isdigit():



    #
    cont = input("Vill du fortsätta ja eller nej?")

    # if len(cont) < 1:
    #     print("Du har skrivit för kort text")

    cont = cont.lower() #(upper)
    if cont == "nej":
        break


#slicing

namn = "Evie"
print(namn[1])
print(namn[1:3])


# namn = "Evie"

# namn = namn + " Compton" + " " + "is my name"
# antal = len(namn)  # len blir ett tal i detta fall.

# namn = "Hejsan"
# d = namn[0]


# namn = input("Vad heter du?")
# antal = len(namn)
# count_e = 0
# for e in range (0, antal):

#     if namn[e]== "e":
#         count_e = count_e + 1

# print(f"Du har {count_e} e:n i ditt namn!")



#     first =namn[0]
# print(f"Ditt namn börjar på {first}")
