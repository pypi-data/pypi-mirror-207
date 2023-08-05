import requests, urllib, socketio

class VMstream:
	def __init__(self, VM, connectcallback, msgcallback):
		self.vm = VM
		self.sio = socketio.Client()
		self.connectcallback = connectcallback
		self.msgcallback = msgcallback
		@self.sio.event
		def connect():
			self.sio.emit("vmselect", (self.vm.index,))
			self.connectcallback(self)
		@self.sio.event
		def datad(data):
			self.msgcallback(self,data)
	def send(self, data):
		self.sio.emit("datad", data)
	def open(self):
		self.sio.connect("https://duckcloud.pcprojects.tk", headers={"cookie": "token="+self.vm.token})
		self.sio.wait()
	def close(self):
		self.sio.disconnect()
		del self
	
# note to self: improve the repetitive shit code

class VM:
	def __init__(self, index, data, token):
		self.token = token
		self.index = index
		self.name = data["vmname"]
		self.name_encoded = data["vmname_encoded"]
		self.status = data["status"]
	def delete(self):
		r = requests.get("https://duckcloud.pcprojects.tk/burn/"+str(self.index), headers={"cookie": "token="+self.token}, allow_redirects=False)
		if "Location" in r.headers:
			return True
		else:
			return False
	def chown(self, username):
		r = requests.post("https://duckcloud.pcprojects.tk/chown/"+str(self.index)+"?username="+username, headers={"cookie": "token="+self.token}, allow_redirects=False)
		if "Location" in r.headers:
			return True
		else:
			return False
	def whitelist(self, username):
		r = requests.post("https://duckcloud.pcprojects.tk/whitectl/"+str(self.index)+"?based=0&username="+username, headers={"cookie": "token="+self.token}, allow_redirects=False)
		if "Location" in r.headers:
			return True
		else:
			return False
	def clear_whitelist(self):
		r = requests.get("https://duckcloud.pcprojects.tk/whitectlreset/"+str(self.index), headers={"cookie": "token="+self.token}, allow_redirects=False)
		if "Location" in r.headers:
			return True
		else:
			return False
	def ramset(self, mb):
		r = requests.post("https://duckcloud.pcprojects.tk/ramset/"+str(self.index)+"?ramset="+mb, headers={"cookie": "token="+self.token}, allow_redirects=False)
		if "Location" in r.headers:
			return True
		else:
			return False
	def resize(self, width, height):
		r = requests.post(f"https://duckcloud.pcprojects.tk/resize/{self.index}?w={width}&h={height}" headers={"cookie": "token="+self.token}, allow_redirects=False) # notepad++ doesnt highlight f strings bruh
		if "Location" in r.headers:
			return True
		else:
			return False
	def rename(self, newname):
		r = requests.post("https://duckcloud.pcprojects.tk/ren/"+str(self.index), json={"vmname": newname}, headers={"cookie": "token="+self.token}, allow_redirects=False)
		if r.headers["Location"] == "/settings/"+str(self.index):
			return True
		else:
			return False
	def toggle(self):
		r = requests.get("https://duckcloud.pcprojects.tk/shutoff/"+str(self.index), headers={"cookie": "token="+self.token}, allow_redirects=False)
		if "Location" in r.headers:
			if r.headers["Location"] == "/settings/"+str(self.index):
				if self.status == "online": self.status = "offline"
				if self.status == "offline": self.status = "online"
				return True
			else:
				return False
		else:
			return False
	def getStream(self, connect, msg):
		return VMstream(self, connect, msg)