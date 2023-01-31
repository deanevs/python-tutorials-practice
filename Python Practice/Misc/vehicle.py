

class Vehicle:

    def __init__(self):
        self._max_speed = 0
        self._mileage = 0

    def set_mileage(self, m):
        self._mileage = m

    def set_speed(self, s):
        self._max_speed = s

    def __str__(self):
        return f"Max speed = {self._max_speed}\n" + f"Mileage = {self._mileage}\n"


if __name__ == '__main__':
    car = Vehicle()
    print(car)

    car.set_speed(100)
    car.set_mileage(1000000)

    print(car)
