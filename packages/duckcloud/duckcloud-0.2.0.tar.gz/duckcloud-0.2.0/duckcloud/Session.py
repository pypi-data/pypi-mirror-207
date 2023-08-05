from .VM import VM
import requests

class Session:
	def __init__(self, cookie):
		self.token = cookie["token"]
		self._cookie = cookie
	def listVMS(self):
		r = requests.get("https://duckcloud.pcprojects.tk/listContainer", headers={"cookie": "token="+self.token}, allow_redirects=False)
		containers = r.json()
		def generator(containers):
			for i in range(len(containers)):
				yield VM(i, containers[i], self.token)
		return generator(containers)