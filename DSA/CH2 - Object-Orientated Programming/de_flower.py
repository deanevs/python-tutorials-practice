

class Flower:
    _name: str
    _petals: int
    _price: float

    def __init__(self, name='Rose', petals=5, price=1.0):
        self._name = name
        self._petals = petals
        self._price = price

    def set_name(self, new_name):
        self._name = new_name

    def get_name(self):
        return self._name

    def __str__(self):
        return f"Name = {self._name}, petals = {self._petals}, price = {self._price}"


if __name__ == '__main__':

    flower = Flower('daffodil', 20, 1.50)
    print(flower)

    flower.set_name('Tulip')
    print(flower.get_name())
    print(flower)
    flower.name = 'Lavendar'
    print(flower)

