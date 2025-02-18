import tkinter as tk
from models.SessionStats import SessionStats
from controllers.SilenceService import SilenceService
from enums.ProcessState import ProcessState
from PIL import Image, ImageTk
import os

class Window(tk.Tk):
    def __init__(self, silence_service: SilenceService, stats: SessionStats):
        super().__init__()
        self.silence_service = silence_service
        self.stats = stats

        self.title("Spotify Ads Silencer")
        self.geometry("425x140")
        self.resizable(0, 0)
        self.iconbitmap(self.resource_path("images/ico.ico"))
        self.canvas = tk.Canvas(self, width=425, height=140, bg="#212121", highlightthickness=0)
        self.canvas.pack(fill="both", expand=True, anchor="center")
        image = Image.open(self.resource_path("images/logo.png"))
        img = image.resize((120, 120))
        self.logoImg = ImageTk.PhotoImage(img)
        self.canvas.create_image(75, 70, image=self.logoImg, anchor="center")
        self.soundStateText = self.canvas.create_text(150, 40, text="Spotify is Audible", anchor="w", font=("Ubuntu", 16), fill="#b3b3b3")
        self.adCountText = self.canvas.create_text(150, 70, text="Ads Silenced: " + str(self.stats.getAdCount()), anchor="w", font=("Ubuntu", 12), fill="#b3b3b3")
        self.songName = self.canvas.create_text(150, 110, text="", anchor="w", font=("Ubuntu", 9), fill="#d3d3d3")
        self.silence_service.start()
        self.protocol("WM_DELETE_WINDOW", self.on_close)

    def update_canvas(self, process):
        self.canvas.after(0, self.updateTextElements, process)

    def updateTextElements(self, process):
        titleSuffix = ""
        heading = ""

        match process.getState():
            case ProcessState.CLOSED:
                 titleSuffix = " is Closed"
                 heading = "Looking for " + process.getProcessName()
            case ProcessState.PLAYING_MUSIC:
                 titleSuffix = " is Audible"
                 heading = "Playing: " + process.getTitle()
            case ProcessState.PLAYING_AD:
                 titleSuffix = " is Silenced"
                 heading = "Advert is Playing"

        self.canvas.itemconfigure(self.soundStateText, text=process.getProcessName() + titleSuffix)
        self.canvas.itemconfigure(self.adCountText, text="Ads Silenced: " + str(self.stats.getAdCount()))
        self.canvas.itemconfigure(self.songName, text=heading)

    def on_close(self):
        self.silence_service.stop()
        self.after(100, self.destroy)
    
    @staticmethod
    def resource_path(relative_path):
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
        return os.path.join(base_path, relative_path)