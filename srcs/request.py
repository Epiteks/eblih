import json
import requests

class RequestError(Exception):

	def __init__(self, value):
		self.value = "Request Error : " + value

	def __str__(self):
		return repr(self.value)

class	Request(object):

	def	__init__(self, url, method, data=None):
		super(Request, self).__init__()

		self._done = False
		self._url = url
		self._types = {"GET": requests.get,
					"POST": requests.post,
					"DELETE": requests.delete}
		if method not in self._types:
			raise RequestError("Wrong method")
		self._method = method
		self._data = bytearray(json.dumps(data), "utf8")
		self._error = None
		self._request = None
		self._cookies = {}
		self._headers = {"Content-Type": "application/json"}

	def	execute(self):
		try:
			self._done = True
			self._request = self._types[self._method](self._url, data=str(self._data), headers=self._headers, cookies=self._cookies)
			return True if self._request.status_code == 200 else False
		except Exception as e:
			raise RequestError(str(e))

	def	parse(self):
		if self._done and not self._error and self._request.status_code == 200:
			return {"code": self._request.status_code, "data": self._request.json()}
		return None

	def getCode(self):
		if self._done:
			return self._request.status_code
		return None

	def getText(self):
		if self._done:
			return self._request.text
		return None

	def	getError(self):
		return {"code": self._request.status_code, "data": self._request.json()} if self._request else None

	def	getCookies(self):
		return self._request.cookies if self._request else None

	def	getCookie(self, key):
		try:
			return self._request.cookies[key] if self._request else None
		except Exception as e:
			raise RequestError(str(e))

	def	getHeaders(self):
		return self._request.headers if self._request else None

	def	getHeader(self, key):
		try:
			return self._request.headers[key] if self._request else None
		except Exception as e:
			raise RequestError(str(e))

	def	setCookie(self, key, value):
		self._cookies[key] = value

	def	setHeader(self, key, value):
		self._headers[key] = value

def executeRequest(req, parse=True):
	status = req.execute()
	if parse:
		return req.parse() if status else req.getError()
	return status

	@staticmethod
	def executeRequest(req, parse=True):
		status = req.execute()
		if parse:
			return req.parse() if status else req.getError()
		return status

	@staticmethod
	def get(url, parse=True):
		return Request.executeRequest(Request(url, "GET"), parse=parse)

	@staticmethod
	def post(url, data=None, parse=True):
		return Request.executeRequest(Request(url, "POST", data), parse=parse)

	@staticmethod
	def delete(url, data=None, parse=True):
		return Request.executeRequest(Request(url, "DELETE", data), parse=parse)