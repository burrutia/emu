#!/usr/bin/python
# Copyright (c) 2011 Brian Urrutia <burrutia.biz@gmail.com>
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish, dis-
# tribute, sublicense, and/or sell copies of the Software, and to permit
# persons to whom the Software is furnished to do so, subject to the fol-
# lowing conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABIL-
# ITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT
# SHALL THE AUTHOR BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, 
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS

import os, sys, string

class shell_utils(object):
    def __init__(self):
        self.object = object

    def grep(self, object, smatch):
	self.smatch = smatch
	if smatch in object:
	    return object

    def awk(self, ph, smatch, object):
        self.ph = ph
	self.grep(smatch, object)
        mymatch = object.split()
	print mymatch[ph]

    def host(self, object, ip):
        import socket
        self.ip = ip
        hostaddress = socket.gethostbyaddr(ip)
        hostname = hostaddress[0]
        return hostname
