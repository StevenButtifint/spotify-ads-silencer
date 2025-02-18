import psutil
import ctypes
from win32gui import GetWindowText, GetForegroundWindow, EnumWindows, IsWindowVisible
from win32process import GetWindowThreadProcessId
import pygetwindow as gw

class ProcessFunctions:

    @staticmethod
    def getProcessName(pid):
        try:
            process = psutil.Process(pid)
            process_name = process.name()
            return process_name
        except psutil.NoSuchProcess:
            return "None"
        except psutil.AccessDenied:
            return "Denied"
        except psutil.ZombieProcess:
            return "Zombie"
    
    @staticmethod
    def getProcessID(process_name):
        for proc in psutil.process_iter(['pid', 'name']):
            try:
                if proc.info['name'].lower() == process_name.lower():
                    return proc.info['pid']
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
        return None
    
    @staticmethod
    def hasProcessExpired(processName, processID):
        return processName != ProcessFunctions.getProcessName(processID)
