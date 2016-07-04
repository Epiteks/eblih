#!/bin/sh

for _file in /usr/local/bin/eblih /usr/local/bin/eblih_srcs /tmp/eblih.tar.gz
do
	[ -w $_file ] && rm -rf $_file || sudo rm -rf $_file
done

_version="$(curl -s https://raw.githubusercontent.com/epiteks/eblih/v2.0.6/.version)"
curl -sL https://github.com/epiteks/eblih/archive/v$_version.tar.gz > /tmp/eblih.tar.gz

if [ -w /usr/local/bin ]; then
	mkdir /usr/local/bin/eblih_srcs
	tar xf /tmp/eblih.tar.gz -C /usr/local/bin/eblih_srcs --strip=1
	ln -s /usr/local/bin/eblih_srcs/eblih /usr/local/bin/eblih
else
	sudo mkdir /usr/local/bin/eblih_srcs
	sudo tar xf /tmp/eblih.tar.gz -C /usr/local/bin/eblih_srcs --strip=1
	sudo ln -s /usr/local/bin/eblih_srcs/eblih /usr/local/bin/eblih
fi

rm -rf /tmp/eblih.tar.gz

for _pip in pip pip2 pip2.7
do
	if ! [ type $_pip 2&>1 >/dev/null ]; then
		_out="$(eval "$_pip -V")"
		if grep -q "python 2.7" <<< $_out; then
			[ -w $(which $_pip) ] && eval "$_pip install -Ur /usr/local/bin/eblih_srcs/requirements.txt" || eval "sudo $_pip install -Ur /usr/local/bin/eblih_srcs/requirements.txt"
			exit
		fi
	fi
done
echo "pip for Python 2.7 not found, you may have dependencies issues. (https://pip.pypa.io/en/stable/installing/)"
