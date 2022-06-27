
def modulus(number):
    if number < 0:
        return -1 * number
    return number

def getNextAnimation(vector):  
    x = vector[0]
    y = vector[1]
    if x == 0:
        if y == 0:
            return "coffeeBreak"
        elif y < 0:
            return "walkingUp"
        elif y > 0:
            return "walkingDown"
    elif y == 0:
        if x < 0: 
            return "walkingLeft"
        elif x > 0:
            return "walkingRight"
    modY = modulus(y)
    if modY == 2:
        if y < 0:
            return "walkingUp"
        elif y > 0:
            return "walkingDown"
    if x < 0:
        return "walkingLeft"
    elif x > 0:
        return "walkingRight"