def calculateSalary(hoursWorked, hourlySalary):

    Salary = hoursWorked * hourlySalary
    return Salary

def calculateBonus(age, name):
    if name == "Stefan":
         Bonus3 = "220kr"
         return Bonus3  
    if age >= 25 and age >= 45:
        Bonus1 = "6%"
        return Bonus1

    if age <= 45:
            Bonus2 = "5%"
            return Bonus2
    
  

    
