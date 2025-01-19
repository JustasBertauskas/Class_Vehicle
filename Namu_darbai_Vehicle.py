class Vehicle:
    def __init__(self, brand, age, mark, color="blue", weight="2000kg"):
        self.brand = brand
        self.age = age
        self.mark = mark
        self.color = color
        self.weight = weight

    def move(self):
        print("move")

    def stop(self):
        print("stop")

    def birthday(self):
        self.age += 1

# Pavyzdys, kaip naudoti klasę:
car = Vehicle(brand="audi", age=5, mark="r6", color="red", weight="2000kg")
car.move()  
car.stop()  
print(car.age)  
car.birthday()
print(car.age)  
