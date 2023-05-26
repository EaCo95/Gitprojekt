from services import calculateSalary 
def Salary():
    while True:
        age = int(input("Ange ålder:"))
        namn = input("Ange namn:")
        hourlySalary = int(input("Ange timlön:"))
        hoursWorked = int(input("Ange hur många timmar du arbetat:"))
        #calculateSalary ...
        pass
 
def calculateSalary(hourlySalary, hoursWorked):
    hourlySalary * hoursWorked == Salary


def menu():
    while True:
        print("1. Shapes")
        print("2. Salary")    
        print("0. Exit")    
        action = input("Val:")
        if action == "1":
            shapes()
        if action == "2":
            Salary()
        if action == "02":
            return

if __name__ == "__main__":
    menu()