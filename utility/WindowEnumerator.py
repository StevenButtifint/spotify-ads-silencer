import ctypes

from utility.ProcessFunctions import ProcessFunctions


class WindowEnumerator:
    def __init__(self):
        self.EnumWindows = ctypes.windll.user32.EnumWindows
        self.GetWindowTextW = ctypes.windll.user32.GetWindowTextW
        self.GetWindowTextLengthW = ctypes.windll.user32.GetWindowTextLengthW
        self.IsWindowVisible = ctypes.windll.user32.IsWindowVisible
        self.GetWindowThreadProcessId = ctypes.windll.user32.GetWindowThreadProcessId
    
    def getWindowTitle(self, processName):
        active_user_processes = ctypes.WINFUNCTYPE(ctypes.c_bool, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int))

        titles = []

        def for_each_window(hwnd, _):
            if self.IsWindowVisible(hwnd):
                length = self.GetWindowTextLengthW(hwnd)
                buff = ctypes.create_unicode_buffer(length + 1)
                self.GetWindowTextW(hwnd, buff, length + 1)
                title = buff.value
                
                pid = ctypes.c_int()
                self.GetWindowThreadProcessId(hwnd, ctypes.byref(pid))
                               
                if processName == ProcessFunctions.getProcessName(pid.value):
                    titles.append((title))
                    return True
                 
            return True

        self.EnumWindows(active_user_processes(for_each_window), 0)
        
        title = titles[0] if titles else ''

        return title