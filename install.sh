#!/bin/sh

rm -rf /usr/local/bin/eblih /usr/local/bin/eblih_srcs /tmp/eblih.tar.gz

curl -sL https://github.com/hug33k/eblih/archive/v2.0.0.tar.gz > /tmp/eblih.tar.gz

mkdir /usr/local/bin/eblih_srcs

tar xf /tmp/eblih.tar.gz -C /usr/local/bin/eblih_srcs --strip=1

ln -s /usr/local/bin/eblih_srcs/eblih /usr/local/bin/eblih
