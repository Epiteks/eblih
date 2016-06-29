#!/bin/sh

for _file in /usr/local/bin/eblih /usr/local/bin/eblih_srcs /tmp/eblih.tar.gz
do
	[ -w $_file ] && rm -rf $_file || sudo rm -rf $_file
done

curl -sL https://github.com/hug33k/eblih/archive/v2.0.0.tar.gz > /tmp/eblih.tar.gz

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