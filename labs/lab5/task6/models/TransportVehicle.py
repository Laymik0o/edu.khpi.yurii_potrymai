class TransportVehicle:

    _speed = 0

    def __init__(self, cost, speed, manufacture_year):
        self._cost = cost
        self._max_speed = speed
        self._manufacture_year = manufacture_year

    @property
    def cost(self):
        return self._cost

    @cost.setter
    def cost(self, cost):
        self._cost = cost

    @property
    def max_speed(self):
        return self._max_speed

    @property
    def manufacture_year(self):
        return self._manufacture_year

    @manufacture_year.setter
    def manufacture_year(self, manufacture_year):
        self._manufacture_year = manufacture_year

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, speed):
        self._speed = speed


    def move(self): pass
