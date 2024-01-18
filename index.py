from abc import ABC ,abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass
    @abstractmethod
    def stop(self):
        print("This car has stopped!!")
class Car(Vehicle):
    def go(self):
        print("This car is drove!!")


class motorcycle(Vehicle):
    def go(self):
        print("this motorcycle is going!!")



car=Car()
car.stop()
car.go()