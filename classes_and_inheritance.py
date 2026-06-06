class Vehicle:
    def __init__(self, brand: str, model: str):
        self.brand = brand
        self.model = model

    def startEngine(self):
        return "Vroom Vroom, engine is starting !!!!"
    
    def displayInfo(self):
        return f"This car of brand -{self.brand} and model - {self.model}"
    

class Car(Vehicle):
    def openTrunk(self):
        return "The trunk is open now!!!"
    
class ElectricCar(Vehicle):
    def __init__(self, brand: str, model :str, battery_size :int):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def startEngine(self):
        return "NO SOUND...... Engine already started!!!!"
    
    def displayInfo(self):
        return f"This is Electric car of brand -{self.brand} , model - {self.model} and battery capacity - {self.battery_size} "
    

def main():
    print("Standard ICE Car")
    my_car = Car(brand="TOYOTA" , model="Carolla")
    print(my_car.displayInfo())
    print(my_car.startEngine())
    print(my_car.openTrunk())

    print("\n\n ELECTRIC Car")
    my_ev_car = ElectricCar(brand="TATA",model="Nexon",battery_size=45)
    print(my_ev_car.displayInfo())
    print(my_ev_car.startEngine())

if __name__ == "__main__":
    main()
