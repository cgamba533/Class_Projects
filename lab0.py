class Flower:
#Common base class for all Flowers
    def __init__(self, petalName, petalNumber, petalPrice):
        self.name = petalName
        self.petals = petalNumber
        self.price = petalPrice

    def setName(self, petalName):
        self.name = petalName
    def setPetals(self, petalNumber):
        self.petals = petalNumber
    def setPrice(self, petalPrice):
        self.price = petalPrice
    def getName(self):
        return self.name
    def getPetals(self):
        return self.petals
    def getPrice(self):
        return self.price
#This would create first object of Flower class
f1 = Flower("Sunflower", 2, 1000)
print ("Flower Details:")
print ("Name: ", f1.getName())
print ("Number of petals:", f1.getPetals())
print ("Price:",f1.getPrice())
print ("\n")
#This would create second object of Flower class
f2 = Flower("Rose", 5, 2000)
f2.setPrice(3333)
f2.setPetals(6)
print ("Flower Details:")
print ("Name: ", f2.getName())
print ("Number of petals:", f2.getPetals())
print ("Price:",f2.getPrice())

"""
Flower Details:
Name:  Sunflower
Number of petals: 2
Price: 1000


Flower Details:
Name:  Rose
Number of petals: 6
Price: 3333
"""

class Product:
    def __init__(self, name, amount, price, balance):
        self.name = name
        self.amount = amount
        self.price = price
        self.balance = balance

    def get_price(self):
        price = 0
        if self.amount < 10:
            price = self.amount * self.price
            return price
        elif self.amount >= 10 and self.amount < 99:
            price = (self.amount * self.price) * 0.9
            return price
        else:
            price = (self.amount * self.price) * 0.8
            return price

    def make_purchase(self, quantity):
        purchase_price = quantity * self.price
        if self.balance > purchase_price:
            self.balance = self.balance - purchase_price
        else:
            raise ValueError("Purchase price of item(s) exceeds current balance")
        return self.balance

class Converter:
    def __init__(self, length, unit):
        self.length = length
        self.unit = unit
        self.universal = 0

    def convert(self):
        self.universal = 0
        if self.unit == "inches":
            self.universal = self.length
        if self.unit == "feet":
            self.universal = self.length * 12
        if self.unit == "yards":
            self.universal = self.length * 36
        if self.unit == "miles":
            self.universal = self.length * 63360
        if self.unit == "kilometers":
            self.universal = self.length * 39370.1
        if self.unit == "meters":
            self.universal = self.length * 39.37
        if self.unit == "centimeters":
            self.universal = self.length * 0.3937
        if self.unit == "milimeters":
            self.universal = self.length * 0.0394
        return self.universal


    def inches(self):
        return self.universal

    def feet(self):
        return self.universal / 12

    def yards(self):
        return self.universal / 36

    def miles(self):
        return self.universal / 63360

    def kilometers(self):
        return self.universal / 39370.1

    def meters(self):
        return self.universal / 39.37

    def centimeters(self):
        return self.universal / 0.3937

    def milimeters(self):
        return self.universal / 0.0394




