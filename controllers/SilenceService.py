import threading
import time

from utility.ProcessFunctions import ProcessFunctions
from utility.WindowEnumerator import WindowEnumerator
from enums.ProcessState import ProcessState

class SilenceService:
    def __init__(self, process, audioManager, updatePeriod, stats, update_callback: callable):
        self.stats = stats
        self.running = False
        self.updatePeriod = updatePeriod
        self.update_callback = update_callback

        self.windowEnum = None
        self.process = process
        self.audioManager = audioManager

    def start(self):
        def run():
            while self.running:
                if ProcessFunctions.hasProcessExpired(self.process.getExecutableName(), self.process.getID()):
                    self.process.setID(ProcessFunctions.getProcessID(self.process.getExecutableName()))
                    self.windowEnum = WindowEnumerator()

                self.process.setTitle(self.windowEnum.getWindowTitle(self.process.getExecutableName()))
                if len(self.process.getTitle()) == 0:
                    self.process.setState(ProcessState.CLOSED)
                elif self.isAdvert(self.process):
                    self.audioManager.mute()
                    self.process.setState(ProcessState.PLAYING_AD)
                    self.stats.checkForNewAd(self.process.getTitle())
                else:
                    self.audioManager.unmute()
                    self.process.setState(ProcessState.PLAYING_MUSIC)

                time.sleep(self.updatePeriod)
                self.update_callback(self.process)

        self.thread = threading.Thread(target=run, daemon=True)
        self.running = True
        self.thread.start()

    def stop(self):
        self.running = False

    @staticmethod
    def isAdvert(process):
        title = process.getTitle()
        return '-' not in title and title != process.getProcessName()+" Free"