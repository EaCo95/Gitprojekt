Very_long= "Hej" * 65556
with open('output.txt', 'w') as file:
    file.write(Very_long)