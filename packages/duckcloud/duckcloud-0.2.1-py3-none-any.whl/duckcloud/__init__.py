from .Session import Session
import requests, json, os, datetime, calendar

# goo goo gaa gaa

class cookieError(Exception):
	pass

def _parseCookie(cstr): # parse set-token string
	segments = cstr.split("; ")
	out = {}
	for segment in segments:
		h = segment.split("=")
		out[h[0]] = h[1]
	return out

def _parseTime(time):
	monthmap = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
	stringdate = time[5:16] # get datetime
	stringdate = stringdate.split(" ")
	year = int(stringdate[2])
	month = monthmap.index(stringdate[1])+1
	day = int(stringdate[0])
	times = time[17:25].split(":")
	#print(time[17:25])
	h,m,s = int(times[0]), int(times[1]), int(times[2])
	#print(year,month,day,h,m,s)
	return calendar.timegm(datetime.datetime(year, month, day, h, m, s).timetuple())

def _timeNow():
	return calendar.timegm(datetime.datetime.now().timetuple())

def login(path, id, secret):
	if os.path.exists(path):
		f = open(path)
		data = json.loads(f.read())
		f.close()
		expiration = _parseTime(data["Expires"])
		if expiration > _timeNow():
			return Session(data)
	r = requests.post("https://duckcloud.pcprojects.tk/login", json={"username": id, "password": secret}, allow_redirects=False)
	if "set-cookie" in r.headers:
		cookie = _parseCookie(r.headers["set_cookie"])
		f = open(path,"w+")
		f.write(json.dumps(cookie))
		f.close()
		return Session(cookie)
	else:
		raise cookieError("Something went wrong in generating the new cookie!")	
