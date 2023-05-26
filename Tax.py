# Skapa en funktion som heter CalculateTaxesOnSalary

# Den tar som inparameter ett tal (lönen).  Om Månadslön >= 30000 tar man lön * 0,33

# om Månadslön < 15000 så lön * 0,12

# om Månadslön <30000 så lön * 0,28

# Returnera den beräknade skattesatsen.


def CalculateTaxesOnSalary (Månadslön):

    if Månadslön >= 30000:
        return Månadslön * 0.33

    if Månadslön < 15000:
        return Månadslön * 0.12

    if Månadslön < 30000:
        return Månadslön *0.28

Månadslön = int(input("Ange din Månadslön: "))
Månadslön = CalculateTaxesOnSalary(Månadslön)
print(f"Din skatt blir {Månadslön}")

if time >= 1600 and time >= 1700
return Price * 0.8

