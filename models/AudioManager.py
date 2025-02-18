from pycaw.pycaw import AudioUtilities


class AudioManager:
	def __init__(self, sessionName):
		self.sessions = AudioUtilities.GetAllSessions()
		self.sessionName = sessionName
		self.session = None
		self.setSession()

	def setSession(self):
		for session in self.sessions:
			if str(session) == self.sessionName:
				self.session = session

	def mute(self):
		self.changeVolume(1)
	
	def unmute(self):
		self.changeVolume(0)

	def changeVolume(self, amount):
		if self.session != None:
			volume = self.session.SimpleAudioVolume
			volume.SetMute(amount, None)