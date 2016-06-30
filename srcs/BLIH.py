import sys
import json
import hmac
import hashlib
import request

_routes = {
	"repository":
	[
		{
			"action": "create",
			"route": "/repositories",
			"arguments": None,
			"method": "POST",
			"data":
			[
				{
					"name": "name",
					"default": None,
					"optional": False
				},
				{
					"name": "type",
					"default": "git",
					"optional": False
				},
				{
					"name": "description",
					"default": None,
					"optional": True
				}
			]
		},
		{
			"action": "list",
			"route": "/repositories",
			"arguments": None,
			"method": "GET",
			"data": None
		},
		{
			"action": "delete",
			"route": "/repository/$",
			"arguments":
			[
				"name"
			],
			"method": "DELETE",
			"data": None
		},
		{
			"action": "info",
			"route": "/repository/$",
			"arguments":
			[
				"name"
			],
			"method": "GET",
			"data": None
		},
		{
			"action": "getacl",
			"route": "/repository/$/acls",
			"arguments":
			[
				"name"
			],
			"method": "GET",
			"data": None
		},
		{
			"action": "setacl",
			"route": "/repository/$/acls",
			"arguments":
			[
				"name"
			],
			"method": "POST",
			"data":
			[
				{
					"name": "user",
					"default": None,
					"optional": False
				},
				{
					"name": "acl",
					"default": None,
					"optional": False
				}
			]
		}
	],
	"sshkey":
	[
		{
			"action": "add",
			"route": "/sshkeys",
			"arguments": None,
			"method": "POST",
			"data":
			[
				{
					"name": "sshkey",
					"default": None,
					"optional": False
				}
			]
		},
		{
			"action": "delete",
			"route": "/sshkey/$",
			"arguments":
			[
				"sshkey"
			],
			"method": "DELETE",
			"data": None
		},
		{
			"action": "list",
			"route": "/sshkeys",
			"arguments": None,
			"method": "GET",
			"data": None
		}
	],
	"whoami":
	[
		{
			"action": "whoami",
			"route": "/whoami",
			"arguments": None,
			"method": "GET",
			"data": None
		}
	]
}

class	API(object):

	def	__init__(self, login, token, baseURL="https://blih.epitech.eu"):
		super(API, self).__init__()
		self._base = baseURL
		self._login = login
		self._token = bytearray(str(token), 'utf8')

	def	make_body(self, data=None):
		hash_signature = hmac.new(self._token, msg=bytearray(self._login, 'utf-8'), digestmod=hashlib.sha512)
		if data:
			hash_signature.update(bytearray(json.dumps(data, sort_keys=True, indent=4, separators=(',', ': ')), 'utf8'))
		signature = hash_signature.hexdigest()
		result = {"user": self._login, "signature": signature}
		if data:
			result["data"] = data
		return result

	def	make_route(self, route):
		return self._base + route

	def	get_action(self, user_mode, user_action):
		if user_mode in self._actions:
			for action in self._actions[user_mode]:
				if action["action"] == user_action:
					return action
		return None

	def	get_route(self, action, args):
		find = action["route"].find("$")
		index = 0
		while find != -1:
			action["route"] = action["route"].replace("$", args[index], 1)
			index += 1
			find = action["route"].find("$")
		return action["route"]

	def	get_data(self, action, args):
		index = 0
		data = {}
		if action["data"]:
			for arg in action["data"]:
				if len(args) > index:
					data[arg["name"]] = args[index]
				elif not arg["optional"] and arg["default"]:
					data[arg["name"]] = arg["default"]
				index += 1
		if data == {}:
			return None
		return data

	def	check_args(self, action, route, body):
		route_args = len(action["arguments"]) if action["arguments"] else 0
		data_args = 0
		if action["data"]:
			for arg in action["data"]:
				if not arg["optional"] and not arg["default"]:
					data_args += 1
		if len(route) < route_args or (action["data"] and (len(body) > len(action["data"]) or len(body) < data_args)):
			return None
		return action

	def	make_args(self, action, route=[], body=[]):
		result = self.check_args(action, route, body)
		if not result:
			return None
		final_route = self._base + self.get_route(action, route)
		data = self.get_data(action, body)
		final_body = self.make_body(data)
		req = request.Request(final_route, action["method"], final_body)
		return req

	def	execute(self, user_mode=None, user_action=None, route=[], body=[], req=None):

		def	execReq(req):
			try:
				status = req.execute()
				return req.parse() if status else req.getError()
			except Exception as e:
				print("\033[1;31mThere was an error\033[0m ({0})".format(str(e)))
				sys.exit(-1)

		if not req:
			action = self.get_action(user_mode, user_action)
			if action:
				req = self.make_args(action, route, body)
				if not req:
					return
		return execReq(req)

class	Repository(API):

	def	__init__(self, login, token, baseURL="https://blih.epitech.eu"):
		super(Repository, self).__init__(login, token, baseURL)
		self._actions = _routes["repository"]

	def	create(self, args):
		data = {"name": args[0], "type": "git", "description": ""}
		return self.execute(req=request.Request(self.make_route("/repositories"), "POST", self.make_body(data)))

	def	list(self, args=None):
		return self.execute(req=request.Request(self.make_route("/repositories"), "GET", self.make_body()))

	def	delete(self, args):
		return self.execute(req=request.Request(self.make_route("/repository/" + args[0]), "DELETE", self.make_body()))

	def	info(self, args):
		return self.execute(req=request.Request(self.make_route("/repository/" + args[0]), "GET", self.make_body()))

	def	getACL(self, args):
		return self.execute(req=request.Request(self.make_route("/repository/" + args[0] + "/acls"), "GET", self.make_body()))

	def	setACL(self, args):
		data = {"user": args[1], "acl": args[2] if len(args) == 3 else ""}
		return self.execute(req=request.Request(self.make_route("/repository/" + args[0] + "/acls"), "POST", self.make_body(data)))

class	SSHKey(API):

	def	__init__(self, login, token, baseURL="https://blih.epitech.eu"):
		super(SSHKey, self).__init__(login, token, baseURL)
		self._actions = _routes["sshkey"]

	def	upload(self, args):
		with open(args[0], "r") as key:
			data = {"sshkey" : key.read()}
		return self.execute(req=request.Request(self.make_route("/sshkeys"), "POST", self.make_body(data)))

	def	list(self, args=None):
		return self.execute(req=request.Request(self.make_route("/sshkeys"), "GET", self.make_body()))

	def	delete(self, args):
		return self.execute(req=request.Request(self.make_route("/sshkey/" + args[0]), "DELETE", self.make_body()))
