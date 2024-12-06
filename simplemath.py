First_num = int(input("First Number : "))
Second_num = int(input("Second Number : "))


def sum(x,y):
    return x + y


def division(x, y):
    return x / y


def dif(x,y):
    return x - y


def mult(x,y):
    return x * y

print(f"{First_num} + {Second_num} = {sum(First_num, Second_num)}\n{First_num}  - {Second_num}  =  {dif(First_num, Second_num)}\n{First_num} * {Second_num} = {mult(First_num, Second_num)}\n{First_num} / {Second_num}  = {int(division(First_num, Second_num))}")



