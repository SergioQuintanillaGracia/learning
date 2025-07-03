def add(*args):
    s = 0
    for num in args:
        s += num
    return s

print(add(1, 2, 2, 45))

def calculate(n, **kwargs):
    print(kwargs)
    # print(type(kwargs))
    #
    # for (key, value) in kwargs.items():
    #     print(key, value)
    #
    # print(kwargs["add"])

    n += kwargs["add"]
    n *= kwargs["multiply"]
    return n

print(calculate(2, add=3, multiply=5))

class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")  # This is the same as kw["make"], but if the key doesn't exist,
                                    # it won't produce an error, it will return None
        self.model = kw.get("model")

car = Car(make="Nissan")
print(car.make, car.model)