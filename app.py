from controllers.SilenceService import SilenceService
from models.AudioManager import AudioManager
from models.SessionStats import SessionStats
from models.Process import Process
from window.Window import Window


def main():
    updatePeriod = 3
    process = Process("Spotify.exe", "Spotify")
    audioManager = AudioManager("DisplayName: Spotify")
    sessionStats = SessionStats()
    silence_service = SilenceService(process, audioManager, updatePeriod, sessionStats, update_callback=lambda new_value: window.update_canvas(new_value))
    window = Window(silence_service, sessionStats)
    window.mainloop()

if __name__ == "__main__":
    main()