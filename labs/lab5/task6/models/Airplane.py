from lab5.task6.models.TransportVehicle import TransportVehicle


class Airplane(TransportVehicle):
    _altitude = 0
    _passengers = 0

    @property
    def altitude(self):
        return self._altitude

    @altitude.setter
    def altitude(self, altitude):
        self._altitude = altitude

    @property
    def passengers(self):
        return self._passengers

    @passengers.setter
    def passengers(self, passengers):
        self._passengers = passengers

    def move(self):
        print("Plane moving with speed %d km/h" % self.speed)
