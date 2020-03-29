from labs.lab5.task6.models.Airplane import Airplane
from labs.lab5.task6.models.Auto import Auto
from labs.lab5.task6.models.Ship import Ship


def demo():
    plane = Airplane(10000000, 10000, 2010)
    plane.passengers = 45
    plane.altitude = 5000
    plane.speed = 2500

    car = Auto(5000, 120, 2003)
    car.speed = 59

    ship = Ship(315000, 70, 1998)
    ship.passengers = 5
    ship.home_port = "Manchester"
    ship.speed = 35

    print("Vehicles speed:")
    plane.move()
    car.move()
    ship.move()
    print("-----------------------------")
    print("Car parameters:")
    print("Cost: %d $" % car.cost)
    print("Manufactured in %d" % car.manufacture_year)
    print("Maximum speed: %d km/h" % car.max_speed)
    print("-----------------------------")
    print("Airplane parameters:")
    print("Cost: %d $" % plane.cost)
    print("Manufactured in %d" % plane.manufacture_year)
    print("Maximum speed: %d km/h" % plane.max_speed)
    print("Plane maximum altitude: %d km" % plane.altitude)
    print("Passengers capacity: ", plane.passengers)
    print("-----------------------------")
    print("Ship parameters:")
    print("Cost: %d $" % ship.cost)
    print("Manufactured in %d" % ship.manufacture_year)
    print("Maximum speed: %d km/h" % ship.max_speed)
    print("Home port: ", ship.home_port)
    print("Passengers capacity: ", ship.passengers)


if __name__ == "__main__":
    demo()
