from .hella_api import HellaApi

class Handler():
	
	def __init__(self, token: str):
		self.token = token
		
	def getStickers(self, user_id: int, v=None):
		if v is None:
			v = 2
		getStickers = HellaApi(self.token).methods(method='getStickers', user_id=user_id, v=v)
		return getStickers
	
	def getSticker(self, product_id: int, sticker_id=None, v=None):
		if v is None:
			v = 2
		getSticker = HellaApi(self.token).methods(method='getSticker', product_id=product_id, sticker_id=sticker_id, v=v)
		return getSticker
	
	def getGroups(self, user_id: int, v=None):
		if v is None:
			v = 2
		getGroups = HellaApi(self.token).methods(method='getGroups', user_id=user_id, v=v)
		return getGroups
		
	def GenerationTTS(self, text: str, speaker=None, v=None):
		if v is None:
			v = 2
		GenerationTTS = HellaApi(self.token).methods(method='GenerationTTS', text=text, speaker=speaker, v=v)
		return GenerationTTS
	
	def GenerationQuotes(self, **kwargs):
		if v is None:
			v = 2
		GenerationQuotes = HellaApi(self.token).methods(method='GenerationQuotes', **kwargs)
		return GenerationQuotes
	
