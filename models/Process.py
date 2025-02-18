from enums.ProcessState import ProcessState


class Process:
    def __init__(self, executableName, processName, id = None):
        self.__executableName = executableName
        self.__processName = processName
        self.__id = id
        self.__title = ""
        self.__state = ProcessState.CLOSED
    
    def getExecutableName(self):
        return self.__executableName
    
    def getProcessName(self):
        return self.__processName

    def getID(self):
        return self.__id
    
    def getTitle(self):
        return self.__title

    def getState(self):
        return self.__state
    
    def setID(self, id):
        self.__id = id
    
    def setTitle(self, title):
        self.__title = title
    
    def setState(self, state):
        self.__state = state