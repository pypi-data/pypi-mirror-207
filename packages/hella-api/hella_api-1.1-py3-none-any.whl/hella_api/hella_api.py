import requests


def status_codes(code):
	try:
		codes = {
			404: "[404] Method not found",
			405: "[405] Params invalid",
			500: "[500] Method Truble"
		}
		return codes[code]
	except:
		return f"[{code}] Status Code"

class HellaError(Exception):
	pass
class HellaApi():
	
	def __init__(self, token: str):
		self.token = token
		
	def methods(self, method, **params):
		url = 'https://api.hella.team/method/'+ method
		params['access_token'] = self.token
		if 'v' not in params:
			params['v'] = 2
		if method == 'GenerationQuotes':
			ava = params['ava']
			ava = requests.get(ava).content
			files = [('ava_bytes', ('file.jpg', ava))]			
			response = requests.post(url=url, files=files, params=params)
			if response.status_code != 200:
				code_info = status_codes(response.status_code)
				raise HellaError(code_info)
			else:
				return response.content
		response = requests.get(url=url, params=params)
		if response.status_code == 200:
			if method == 'GenerationTTS':
				return response.content
			else:
				if response.json()['ok'] == False:
					raise HellaError(f"[{response.json()['error_code']}] {response.json()['error_description']}")
				else:
					return response.json()
		else:
			code_info = status_codes(response.status_code)
			raise HellaError(code_info)
