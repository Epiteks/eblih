import sys
import os
import json
import getpass
import hashlib
import shell
import BLIH

class	ModeError(Exception):

	def __init__(self, value, type="Mode"):
		self.value = "{0} Error : {1}".format(type, value)

	def __str__(self):
		return repr(self.value)

class	Mode(object):

	def __init__(self, user, token, groups="./groups.json"):
		super(Mode, self).__init__()
		self._user = user
		self._token = token
		self._groups = groups

	def	printMessage(self, message):
		if "message" in message["data"]:
			print(message["data"]["message"])
		elif "error" in message["data"]:
			print(message["data"]["error"])

	def	getGroupsConfig(self):
		if not os.path.exists(self._groups):
			self.saveGroupsConfig({"groups":[]})
		with open(self._groups) as data:
			config = json.load(data)
		return config

	def	saveGroupsConfig(self, data):
		with open(self._groups, "w") as dataFile:
			dataFile.write(json.dumps(data))

	def	execute(self, args):
		return

class	Repository(Mode):

	def	__init__(self, user, token, groups="./groups.json", gitServer="git.epitech.eu"):
		super(Repository, self).__init__(user, token, groups)
		self._api = BLIH.Repository(self._user, self._token)
		self._gitServer = gitServer
		self._actions = {"create": self._api.create,
					"list": self._api.list,
					"info": self._api.info,
					"getacl": self._api.getACL,
					"setacl": self._api.setACL,
					"setgacl": self.setGroupACL,
					"delete": self._api.delete,
					"new": self.newRepo,
					"clone": self.cloneRepo,
					"link": self.linkRepo}
		self._callback = {"create": self.printMessage,
					"list": self.printList,
					"info": self.printMessage,
					"getacl": self.printACL,
					"setacl": self.printMessage,
					"setgacl": sys.exit,
					"delete": self.printMessage,
					"new": sys.exit,
					"clone": sys.exit,
					"link": sys.exit}

	def	execute(self, args):
		self._args = args
		if args[0] not in self._actions:
			raise ModeError("Action {0} not found".format(args[0]), type="Repository")
		result = self._actions[args[0]](args[1:])
		self._callback[args[0]](result)

	def	printList(self, data):
		repositories = []
		for name in data["data"]["repositories"]:
			if len(name):
				repositories.append(name)
		repositories.sort(key=lambda x:x.lower())
		for name in repositories:
			if len(self._args) == 2 and self._args[1] not in name:
				continue
			print(name)

	def	printACL(self, data):
		users = []
		for name in data["data"]:
			users.append(name)
		users.sort(key=lambda x:x.lower())
		for name in users:
			print("{0}:\t{1}".format(name, data["data"][name]))

	def	setGroupACL(self, args):
		config = self.getGroupsConfig()
		for group in config["groups"]:
			if group["name"] != args[1]:
				continue
			for user in group["users"]:
				result = self._api.setACL([args[0], user["name"], args[2] if len(args) == 3 else ""])
				result["data"]["message"] += " for {0}".format(user["name"])
				self.printMessage(result)
			return
		raise Exception("Group not found")

	def newRepo(self, args):
		res = self._api.create(args)
		self.printMessage(res)
		self.cloneRepo(args)

	def cloneRepo(self, args):
		author = self._user if len(args) == 1 else args[0]
		gitRoute = "{0}@{1}:/{2}/{3}".format(self._user, self._gitServer, author, args[-1])
		try:
			s = shell.Shell()
			s.execute(["git", "clone", gitRoute])
		except:
			pass

	def linkRepo(self, args):
		def ask():
			res = raw_input("""Git repository already initialized and will be deleted.
Type repo name to confirm [{0}]:""".format(args[-1]))
			return res == args[-1]

		def initGitRepo(shell):
			if os.path.isdir(".git"):
				response = ask()
				if not response:
					print("Link canceled")
					sys.exit(1)
				shell.execute(["rm", "-rf", ".git"])
			shell.execute(["git", "init"])

		def setGitRemote(shell):
			shell.execute(["git", "remote", "add", "origin", gitRoute])
		author = self._user if len(args) == 1 else args[0]
		gitRoute = "{0}@{1}:/{2}/{3}".format(self._user, self._gitServer, author, args[-1])
		try:
			s = shell.Shell()
			initGitRepo(s)
			setGitRemote(s)
		except:
			pass

class	SSHKey(Mode):

	def	__init__(self, user, token, groups="./groups.json"):
		super(SSHKey, self).__init__(user, token, groups)
		self._api = BLIH.SSHKey(self._user, self._token)
		self._actions = {"upload": self._api.upload,
					"list": self._api.list,
					"delete": self._api.delete}
		self._callback = {"upload": self.printMessage,
					"list": self.printKeys,
					"delete": self.printMessage}

	def	execute(self, args):
		if args[0] not in self._actions:
			raise ModeError("Action {0} not found".format(args[0]), type="SSHKey")
		result = self._actions[args[0]](args[1:])
		self._callback[args[0]](result)

	def	printKeys(self, data):
		keys = []
		for key in data["data"]:
			keys.append(key)
		keys.sort(key=lambda x:x.lower())
		for key in keys:
			print("{0}\n{1}\n".format(key, data["data"][key]))

class	Group(Mode):

	def	__init__(self, user=None, token=None, groups="./groups.json"):
		super(Group, self).__init__(None, None, groups)
		self._config = self.getGroupsConfig()
		self._actions = {"create": self.create,
					"add": self.add,
					"delete": self.delete,
					"rename": self.rename,
					"list": self.show}

	def	execute(self, args):
		if args[0] not in self._actions:
			raise ModeError("Action {0} not found".format(args[0]), type="Group")
		self._actions[args[0]](args[1:])

	def	create(self, args):
		for group in self._config["groups"]:
			if group["name"] == args[0]:
				raise ModeError("Group {0} already exist".format(args[0]), type="Group")
		self._config["groups"].append({"name": args[0], "users": []})
		self.saveGroupsConfig(self._config)

	def	add(self, args):
		for group in self._config["groups"]:
			if group["name"] != args[0]:
				continue
			for user in group["users"]:
				if user["name"] == args[1]:
					user["acls"] = args[2]
					self.saveGroupsConfig(self._config)
					return
			group["users"].append({"name": args[1], "acls": args[2]})
			self.saveGroupsConfig(self._config)
			return
		raise ModeError("Group {0} not found".format(args[0]), type="Group")

	def	delete(self, args):
		for group in self._config["groups"]:
			if group["name"] != args[0]:
				continue
			if len(args) == 1:
				self._config["groups"].remove(group)
				self.saveGroupsConfig(self._config)
				return
			else:
				toRemove = []
				users = args[1:]
				for user in group["users"]:
					if user["name"] in users:
						toRemove.append(user)
						users.remove(user["name"])
				for user in users:
					print(user + " not found in group")
				for user in toRemove:
					group["users"].remove(user)
			self.saveGroupsConfig(self._config)
			return
		raise ModeError("Group {0} not found".format(args[0]), type="Group")

	def	show(self, args=None):
		for group in self._config["groups"]:
			if len(args) and group["name"] != args[0]:
				continue
			print(group["name"])
			for user in group["users"]:
				print("\t{0}: {1}".format(user["name"], user["acls"]))
			if len(args) and group["name"] == args[0]:
				return
		if len(args):
			raise ModeError("Group {0} not found".format(args[0]), type="Group")

	def	rename(self, args):
		for group in self._config["groups"]:
			if group["name"] != args[0]:
				continue
			group["name"] = args[1]
			self.saveGroupsConfig(self._config)
			return
		raise ModeError("Group {0} not found".format(args[0]), type="Group")

class	Config(Mode):

	def	__init__(self, user=None, token=None, groups="./groups.json"):
		super(Config, self).__init__(None, None, groups)
		self._actions = {"crypt": self.crypt,
						"disp": self.disp}

	def	execute(self, args):
		if args[0] not in self._actions:
			raise ModeError("Action {0} not found".format(args[0]), type="Config")
		self._actions[args[0]](args[1:])

	def	crypt(self, args):
		if sys.stdin.isatty():
			password = getpass.getpass("Your password :")
		else:
			password = sys.stdin.readline().rstrip()
		token = bytearray(hashlib.sha512(bytearray(password, 'utf8')).hexdigest(), 'utf8')
		print(token.decode("utf-8"))

	def	disp(self, args):

		def	show(var):
			print("{0}={1}".format(var, os.getenv(var)))

		var = ["EPITECH_LOGIN", "EPITECH_TOKEN", "EPITECH_FOLDER"]
		if len(args) == 1:
			if args[0] not in var:
				raise ModeError("Variable {0} not found".format(args[0]), type="Config")
			show(args[0])
			return
		for item in var:
			show(item)
