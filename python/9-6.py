class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):  #此处需加上形参self
        print(self.restaurant_name)
        print(self.cuisine_type)
    def open_restaurant(self):      #此处需加上形参self
        print("the restaurant is open")
class IceCreamStand(Restaurant):
    def __init__(self,restaurant_name,cuisine_type):
        super().__init__(restaurant_name,cuisine_type)
        self.flavors = []
    def addIceCream(self,icecreams=[]):
        for icecream in icecreams:
            self.flavors.append(icecream)
    def showIceCream(self):
        for iceCream in self.flavors:
            print(iceCream)

HagonDaz = IceCreamStand('HagonDaz',"ICECREAM_restaurant")
HagonDaz.addIceCream(["big",'small',"shorts",'longs'])
HagonDaz.showIceCream()