

class SessionStats:
    def __init__(self):
        self.__adCount = 0
        self.__currentAdName = ""
    
    def checkForNewAd(self, currentAdName):
        if currentAdName != self.getCurrentAdName():
            self.countNewAdd()
            self.setCurrentAdName(currentAdName)
    
    def countNewAdd(self):
        self.__adCount += 1

    def getCurrentAdName(self):
        return self.__currentAdName
    
    def getAdCount(self):
        return self.__adCount

    def setCurrentAdName(self, currentAdName):
        self.__currentAdName = currentAdName