def add(*args):
    sum = 0 #args is stored as a tuple
    for num in args:
        sum += num
    return sum

def calculate(n,**kwargs):
#kwargs is stored as a dictionary - often written as **kw
    # print(kwargs)
    # for (key,value) in kwargs.items():
    #     print(key,":",value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

class Car:
    def __init__(self,**kwargs):
        # self.make = kwargs["make"] #my this way if "make" is not specified gives error
        self.make = kwargs.get("make") #this gives none of not specified so use this
        self.model = kwargs["model"]


print(add(1, 2, 3, 4, 5, 6, 7, 8, 9))
calculate(1,add=2,multiply=3)