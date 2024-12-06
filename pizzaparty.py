people = int(input("How many people? : "))
pizza = int(input("How many pizzas do you have? : "))
slices = int(input("how many slices per pizza? : "))


def perpizza(x,y,z):
    perpizza_double = (x * y)
    perpizza_double_dif = perpizza_double / z
    return perpizza_double_dif

def pizza_nashti(x,y):
    return x%y

print(f" {people} people with {pizza} piza \n each person gets {int(perpizza(slices, pizza,slices))} pieces of pizza \n there are {pizza_nashti(slices,pizza)} nashti")