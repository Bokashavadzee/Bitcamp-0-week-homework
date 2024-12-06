age = int(input("How Old Are Your? : "))
retire = int(input("At what age would you like to retire? : "))


def pension(x, y):
    return y - x


print(f" You have {pension(age, retire)} years left until you can retire. \n Its 2024, so you can retire in {2024 + pension(age,retire)}.")