#BLIH API

##Informations

###Base URL

https://blih.epitech.eu/

###Token

Your token is your UNIX password crypted in sha512.

###Signed Data

Data for requests must be signed like this :

````json
{
    'user': 'YOUR_LOGIN',
    'signature': 'SIGNATURE',
    'data': {"YOUR DATA"}
}
````
data is used only for POST requests.

SIGNATURE can be created like this :
````python
signature = hmac.new("TOKEN", msg=bytes("YOUR LOGIN", 'utf-8'), digestmod=hashlib.sha512)
#If you have data
if data:
    signature.update(bytes(json.dumps(data, sort_keys=True, indent=4, separators=(',', ': ')), 'utf8'))
result = signature.hexdigest()
````

Data must be in body request (Even for GET).

##Actions

###GET

####List

Route : /repositories

####Info

Route : /repository/[REPO]

####ACL

Route : /repository/[REPO]/acls

####SSHKEY

Route : /sshkeys

####WHOAMI

Route : /whoami

###POST

####Create

Route : /reposotiries

Data :
````json
{
    'name': 'REPO_NAME',
    'type' : 'git'
}
````
####ACL

Route : /repository/[REPO]/acls

Data :
````json
{
    'user': 'USERNAME',
    'acl': 'ACL'
}
````

####SSHKEY

Route : /sshkeys

Data :
````json
{
    'sshkey': 'YOUR_KEY'
}
````

###DELETE

####Repo

Route : /repository/[REPO]

####SSHKEY

Route : /sshkey/[key]