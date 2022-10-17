# Python 3.6.8, >=3.9 not supported

import tkinter as tk
import ctypes
import time
import datetime

from pycaw.pycaw import AudioUtilities
from PIL import Image, ImageTk


class SpotifyAdsSilencer:
    def __init__(self):
        self.window = tk.Tk()
        self.window.resizable(0, 0)
        self.window.geometry("425x140")
        self.window.title("Spotify Ads Silencer")
        self.window.iconbitmap("ico.ico")
        self.newAd = True
        self.soundState = True
        self.adCount = 0
        self.adStart = datetime.datetime.now()
        self.canvas = tk.Canvas(self.window, width=425, height=140, bg="#212121", highlightthickness=0)
        self.canvas.pack(fill="both", expand=True, anchor="center")
        image = Image.open("logo.png")
        img = image.resize((120, 120))
        self.logoImg = ImageTk.PhotoImage(img)
        self.canvas.create_image(75, 70, image=self.logoImg, anchor="center")
        self.songName = self.canvas.create_text(150, 40, text="Spotify Ads Silencer", anchor="w", font=("Ubuntu", 22), fill="white")
        self.soundStateText = self.canvas.create_text(150, 80, text="Spotify is currently: Audible", anchor="w", font=("Ubuntu", 16), fill="#b3b3b3")
        self.adCountText = self.canvas.create_text(150, 110, text="Ads Silenced: " + str(self.adCount), anchor="w", font=("Ubuntu", 16), fill="#b3b3b3")
        self.window.update_idletasks()
        self.run()

    def update_ad_count(self):
        self.adCount += 1
        self.canvas.itemconfigure(self.adCountText, text="Ads Silenced: " + str(self.adCount))
        self.adStart = datetime.datetime.now()

    def run(self):
        active_user_windows = ctypes.windll.user32.EnumWindows
        active_user_processes = ctypes.WINFUNCTYPE(ctypes.c_bool, ctypes.POINTER(ctypes.c_int),
                                                   ctypes.POINTER(ctypes.c_int))


if __name__ == "__main__":
    SpotifyAdsSilencer()
