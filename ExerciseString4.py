# Du har en sträng med texten ”Detta är en sträng som du skall ändra”. Ersätt via kod

# alla blanktecken i strängen med tecknet * . Räkna sedan ut via kod hur många

# förekomster det finns av tecknet * i strängen.

string = "Detta är en sträng som du skall ändra."

result = string.replace(" ", "*")
print(result)

antal = len(result)
count = 0
for i in range(0, antal):
    if result[i] == "*":
        count = count + 1
        print(f"Det finns {count} i meningen: ")


# mellanslag = "*"
# if string.find(" ") == -1:
#     print

#     print("Det finns antal * : ")

#Done