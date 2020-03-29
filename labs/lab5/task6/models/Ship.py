from lab5.task6.models.TransportVehicle import TransportVehicle


class Ship(TransportVehicle):
    _passengers = 0
    _home_port = ""

    @property
    def passengers(self):
        return self._passengers

    @passengers.setter
    def passengers(self, passengers):
        self._passengers = passengers

    @property
    def home_port(self):
        return self._passengers

    @home_port.setter
    def home_port(self, home_port):
        self._home_port = home_port

    def move(self):
        print("Ship moving with speed %d km/h" % self.speed)