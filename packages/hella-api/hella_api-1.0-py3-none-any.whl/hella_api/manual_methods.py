from .hella_api import HellaApi

class Handler():
	
	def __init__(self, token: str):
		self.token = token
		
	def getStickers(self, **kwargs):
		getStickers = HellaApi(self.token).methods(method='getStickers', **kwargs)
		return getStickers
	
	def getGroups(self, **kwargs):
		getGroups = HellaApi(self.token).methods(method='getGroups', **kwargs)
		return getGroups
		
	def GenerationTTS(self, **kwargs):
		GenerationTTS = HellaApi(self.token).methods(method='GenerationTTS', **kwargs)
		return GenerationTTS
	
	def GenerationQuotes(self, **keargs):
		GenerationQuotes = HellaApi(self.token).methods(method='GenerationQuotes', **kwargs)
		return GenerationQuotes
	
		
