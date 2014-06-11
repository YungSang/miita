#!/bin/sh

/usr/bin/mongod --fork -f /etc/mongod.conf
./runlocal.py
