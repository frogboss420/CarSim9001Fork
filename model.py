from random import randint

class Car(object):
    def __init__(self):
        self.theEngine = Engine()
    def updateModel(self,dt):
        self.theEngine.updateModel(dt)

class Wheel(object):
    def __init__(self):
        self.orientation: int = randint(0,360)
    def rotate(self,revolutions):
        revs_in_degrees = 360 * revolutions
        self.orientation += revs_in_degrees
        self.orientation %= 360

class Engine(object):
    def __init__(self):
        self.throttlePosition: float = 0
        self.theGearbox = Gearbox()
        self.currentRpm: int = 0
        self.consumptionConstant: float = 0.0025
        self.maxRpm: int = 100
        self.theTank = Tank()

    def updateModel(self,dt):
        self.currentRpm = self.throttlePosition * self.maxRpm
        self.theTank.remove(self.currentRpm * self.consumptionConstant)
        if self.theTank.contents == 0:
            self.currentRpm = 0
        self.theGearbox.rotate(self.currentRpm * (dt / 60))


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