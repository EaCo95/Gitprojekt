# email = input("Please enter your email address")

def IsValidEmail(input):
    if not  '@' in input:
        return False
    lastPoint = input.rfind('.')
    if lastPoint == -1:
        return False
    antalEfter = len(input) - lastPoint -1
    if antalEfter == 2 or antalEfter == 3:
        return True
    return False
