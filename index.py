class Car:
    color= None


def change_color(vehicle,color):
    vehicle.color=color

car=Car()
change_color(car,"red")
car_2=Car()
change_color(car_2,"green")
print(car_2.color)
print(car.color)