from time import time


class FakeTimer:
    def __init__(self):
        self.baseTime = time()

    def getElapsedTime(self):
        return time() - self.baseTime

    def resetBaseTime(self):
        self.baseTime = time()


myTimer = FakeTimer()


class Blobber:
    def __init__(self, name, color, radius, height):
        self.name = name
        self.color = color
        self.radius = radius
        self.height = height
        self.ogVolume = radius * height
        self.vitals = 100
    
    def getName(self):
        self.radius -= myTimer.getElapsedTime() // 5
        myTimer.resetBaseTime()
        return self.name

    def setName(self, name):
        self.radius -= myTimer.getElapsedTime() // 5
        myTimer.resetBaseTime()
        self.name = name.capitalize()

    def getColor(self):
        self.radius -= myTimer.getElapsedTime() // 5
        myTimer.resetBaseTime()
        return self.color
    
    def setColor(self, color):
        self.radius -= myTimer.getElapsedTime() // 5
        myTimer.resetBaseTime()
        self.color = color.lower()

    def feedBlobber(self, food):
        self.radius -= myTimer.getElapsedTime() // 5
        myTimer.resetBaseTime()
        self.radius += food

    def vitalsOK(self):
        self.vitals = (self.radius * self.height / self.ogVolume) * 100
        return self.radius * self.height / self.ogVolume, (not (self.vitals > 110)) and  (not (self.vitals < 90))

    def getVitals(self):
        return format((self.radius * self.height / self.ogVolume), ".2%")
