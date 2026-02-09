class prac :
    wheel = 4
    def __init__(self, brand, milage):
        self.brand = brand
        self.milage = milage
    def details(self):
        print(f"The car naem is {self.brand} and it has {self.wheel} wheels its milage is {self.milage}")

p1 = prac("merceds",20)
p1.wheel=8
p1.details()



    
