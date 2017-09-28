# oop- a cigarette that knows how to light itself, or an egg that knows how to fry itself.
# electric kettle- kettle runs itself and the user doesn't need to know how it all works. a lot more work goes
# into producing an electric kettle vs a regular stovetop kettle, but the end result is that it's easier to use
# everything in python is an object.
# oop uses classes and methods to provide objects that encapsulate data and functions that operate on that data
# method- function part of a class
# a class can be thought of as a template from which objects can be created
# instance- object created from a class definition


class Kettle(object):
    # power_source is a class attribute
    power_source = "electricity"

    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False

    def switch_on(self):  # what's up with self- in python, just the name of a parameter.  convention is 'self'
        # it's a reference to the instance of the class
        self.on = True


kenwood = Kettle("Kenwood", 8.99)
print(kenwood.make)
print(kenwood.price)
kenwood.price = 12.75
print(kenwood.price)

hamilton = Kettle("Hamilton", 14.55)
print(hamilton)

# when a variable is bound to an instance of a class, it's known as a data attribute: price and make below are examples
# known as fields in java, but attributes in python
print("Models: {} = {}, {} = {}".format(kenwood.make, kenwood.price, hamilton.make, hamilton.price))

# another way to do replacement fields with object's attributes
print("Models: {0.make} = {0.price}, {1.make} = {1.price}".format(kenwood, hamilton))

"""
class: template for creating objects.  all objects created using the same class with have the same characteristics.
object: an instance of a class.
instantiate: create an instance of a class.
method: a function defined in a class.
attribute: a variable bound to an instance of a class
constructor: special method that is executed when an instance of a class is created, in python, it's the init method
"""

print(hamilton.on)
hamilton.switch_on()
print(hamilton.on)

Kettle.switch_on(kenwood)
print(kenwood.on)

print("*" * 80)
kenwood.power = 1.5  # can add instance variables after instance is created
print(kenwood.power)
# print(hamilton.power)  # hamilton doesn't have a power attribute because it was created after the fact only for kenwood
print(Kettle.power_source)
print(kenwood.power_source)
print(hamilton.power_source)
print(Kettle.__dict__)
print(kenwood.__dict__)
print(hamilton.__dict__)
print("switch to atomic power")
Kettle.power_source = "atomic"
print(Kettle.__dict__)
print(kenwood.power_source)