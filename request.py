import json
import requests

class	Request(object):

	def	__init__(self, url, method, data=None):
		super(Request, self).__init__()
		self._done = False
		self._url = url
		self._method = method
		self._data = bytearray(json.dumps(data), "utf8")
		self._error = None

	def	execute(self):
		self._done = True
		if self._method == "GET":
			self._request = requests.get(self._url, data=self._data, headers={"Content-Type": "application/json"})
			print(self._url)
			print(self._request.status_code)
		elif self._method == "POST":
			self._request = requests.post(self._url, data=self._data, headers={"Content-Type": "application/json"})
		elif self._method == "DELETE":
			self._request = requests.delete(self._url, data=self._data, headers={"Content-Type": "application/json"})
		if self._request.status_code == 200:
			return True
		else:
			return False

	def	parse(self):
		if self._done and not self._error and self._request.status_code == 200:
			data = {"code": self._request.status_code, "data": self._request.json()}
			return data
		return None

	def	getError(self):
		return {"code": self._request.status_code, "data": self._request.json()}
