#!/usr/bin/python2.6
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

### super simple setup bind only reason this exists it to not have to document 
## how to setup bind.
#named/
#|-- etc
#|   `-- namedb
#|       `-- client_zones
#|           `-- zones.include
#|-- named.conf.tpl
#|-- named.rfc1912.zones
#|-- named.root
#|-- named.root.hints
#`-- zones
#    |-- master
#    |   |-- localdomain.zone
#    |   |-- localhost.zone
#    |   |-- main.internal.zone.db.tpl
#    |   |-- named.broadcast
#    |   |-- named.local
#    |   `-- named.zero
#    `-- templates
#        `-- rev.in-addr.tpl

#./named/zones/templates/rev.in-addr.tpl
#./named/zones/master/main.internal.zone.db.tpl
#./named/named.conf.tpl
import os, sys, io, subprocess
import ConfigParser
import fileinput
from shutil import *

if os.path.isfile('/etc/named.conf'):
    print "Please don't run this on an existing installation!"
    print "please remove /etc/named.conf & start again"
    sys.exit(2)

zonefile = 'named/zones/master/main.internal.zone.db.tpl'
config_file ='/etc/datacenter.ini'
config = ConfigParser.ConfigParser()
config.readfp(open(config_file))

setupdir = config.get('master-conf','setup')
bizunit = config.get('master-conf','unit')
env = config.get('master-conf','env')
domain = bizunit + env

def make_conf(template_in='',template_out=''):
    copy(template_in,template_out)
    f = io.open(template_out, "w")
    for line in io.open(template_in, "r"):
        if '$domain' in line:
            line = line.replace('$domain', domain)
            f.write(line)
        if not domain in line:
            f.write(line)
    f.close()


ip = subprocess.Popen( "/usr/bin/facter ipaddress", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).communicate()[0]
ipaddr = ip.strip("\n")

make_conf(template_in='named.conf.tpl', template_out='named.conf')
copy('named.conf', '/etc/named.conf')

# Change to whereever U want to store everything.
###
#/bin/cp -var ${TOPDIR}/setup/named/named.conf /etc/named.conf
