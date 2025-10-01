from random import randint

class Car(object):
    pass

class Wheel(object):
    def __init__(self):
        self.orientation: int = randint(0,360)
    def rotate(self,revolutions):
        revs_in_degrees = 360 * revolutions
        self.orientation += revs_in_degrees
        self.orientation %= 360

class Engine(object):
    pass

class Gearbox(object):
    def __init__(self):
        self.wheels: dict = {'frontLeft': Wheel(), 'frontRight': Wheel(), 'rearLeft': Wheel(), 'rearRight': Wheel()}
        self.currentGear: int = 0
        self.clutchEngaged: bool = False
        self.gears: list = [0, 0.8, 1, 1.4, 2.2, 3.8]

    def shiftUp(self):
        if self.clutchEngaged == False and self.currentGear != len(self.gears) - 1:
            self.currentGear += 1
        else: pass

    def shiftDown(self):
        if self.clutchEngaged == False and self.currentGear != 0:
            self.currentGear -= 1
        else: pass

    def rotate(self,revolutions):
        if self.clutchEngaged:
            for wheel in self.wheels.values():
                wheel.rotate(revolutions * self.gears[self.currentGear])



class Tank(object):
    def __init__(self):
        self.capacity: int = 500
        self.contents: int = 500
    def remove(self,amount):
        self.contents -= amount
        if self.contents < 0:
            self.contents = 0
    def refuel(self):
        self.contents = self.capacity