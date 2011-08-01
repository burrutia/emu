#!/usr/bin/python
# example usage for using coroutines

import os, sys, string, re
sys.path.append("/home/emu/modules")

import unix_util2

target  = "myproject 192.168.1.2 dev t1.large"
z = echo(grep('dev', awk()))
z.send((target))
z.close()
