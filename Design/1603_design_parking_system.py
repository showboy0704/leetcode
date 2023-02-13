class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.cars = [0, big, medium, small]

    def addCar(self, carType: int) -> bool:
        if self.cars[carType] > 0:
            self.cars[carType] -= 1
            return True
        else:
            return False


if __name__ == '__main__':
    obj = ParkingSystem(1, 1, 0)
    param_1 = obj.addCar(1)
