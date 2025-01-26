def calculate (n, **kwargs):
    print(kwargs)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    #print(n)

#n = int(input("Enter initial number: "))

#calculate(n, add = 3, multiply = 5)

class Car:
    def __init__(self, **kw):
        self.model = kw["model"]
        self.make = kw.get("make") #diff bw get and [] is get will return none and not error if key doesnt exist

mycar = Car(make = "Nissan", model = "GT-R")
print(mycar.model)