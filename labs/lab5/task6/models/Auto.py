from lab5.task6.models.TransportVehicle import TransportVehicle


class Auto(TransportVehicle):

    def move(self):
        print("Car moving with speed %d km/h" % self.speed)
