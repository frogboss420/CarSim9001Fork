from random import randint


class Car:
    def __init__(self):
        self.theEngine = Engine()
    def updateModel(self,dt):
        self.theEngine.updateModel(dt)


class Wheel:
    def __init__(self):
        self.orientation: int = randint(0,360)

#Modtager argumentet "revolutions" for at tillade en vilkårlig rotation, afhængende af omdrejninger i Engine.
    def rotate(self,revolutions):
        revs_in_degrees = 360 * revolutions
        self.orientation += revs_in_degrees
        self.orientation %= 360 #sikrer at hjulets orientation ikke overstiger 360


class Engine:
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


class Gearbox:


    def __init__(self):
        self.wheels: dict = {'frontLeft': Wheel(), 'frontRight': Wheel(), 'rearLeft': Wheel(), 'rearRight': Wheel()}
        self.currentGear: int = 0
        self.clutchEngaged: bool = False
        self.gears: list = [0, 0.8, 1, 1.4, 2.2, 3.8] #indeks svarer til hvilket gear bilen er i, elementerne er koefficienten til omdrejninger.


    def shiftUp(self):
        if self.clutchEngaged == False and self.currentGear != len(self.gears) - 1: #sikrer at koblingen ikke er koblet, og at nuværende gear ikke allerede er det højeste.
            self.currentGear += 1
        else: pass


    def shiftDown(self):
        if self.clutchEngaged == False and self.currentGear != 0: #sikrer at koblingen ikke er koblet, og at nuværende gear ikke allerede er det laveste.
            self.currentGear -= 1
        else: pass

#Ændrer orientationen af hver instansieret wheel afhængigt af hvilket gear bilen er i.
    def rotate(self,revolutions):
        if self.clutchEngaged:
            for wheel in self.wheels.values():
                wheel.rotate(revolutions * self.gears[self.currentGear])


class Tank:
    def __init__(self):
        self.capacity: int = 500
        self.contents: int = 500
    def remove(self,amount):
        self.contents -= amount
        if self.contents < 0:
            self.contents = 0
    def refuel(self):
        self.contents = self.capacity