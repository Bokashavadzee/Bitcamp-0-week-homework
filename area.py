lenght  = int(input("What is the length of the room in feet? "))
width = int(input("What is the width of the room in feet? "))

def area(x,y):
  return x * y

def meter(x,y):
  meter_without_double = (x * y) * 0.3048 / 1
  return meter_without_double

print(f" the area is \n {area(lenght,width)} Feet \n {int(meter(lenght, width))} meters ")