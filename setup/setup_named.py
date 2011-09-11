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

config_file ='/etc/datacenter.ini'
config = ConfigParser.ConfigParser()
config.readfp(open(config_file))

ip = subprocess.Popen( "/usr/bin/facter ipaddress", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).communicate()[0]
ipaddr = ip.strip("\n")

setupdir = config.get('master-conf','setup')
bizunit = config.get('master-conf','unit')
env = config.get('master-conf','env')
domain = bizunit + env

os.chdir('%s/named' %(setupdir))


copy('named.root.hints', '/etc/named.root.hints')
copy('named.rfc1912.zones', '/etc/named.rfc1912.zones')
copy('named.root', '/etc/named.root')
copy('zones/master/localdomain.zone', '/var/named/zones/master/localdomain.zone')
copy('zones/master/localhost.zone', '/var/named/zones/master/localhost.zone')
copy('zones/master/named.local', '/var/named/zones/master/named.local')
copy('zones/master/named.broadcast', '/var/named/zones/master/named.broadcast')
copy('zones/master/named.zero', '/var/named/zones/master/named.zero')

if not os.path.isdir('/var/named/etc/namedb/client_zones'):
    os.mkdir('/var/named/etc', 0775)
    os.mkdir('/var/named/etc/namedb', 0775)
    os.mkdir('/var/named/etc/namedb/client_zones', 0775)

if not os.path.isdir('/var/named/zones/templates'):
    os.mkdir('/var/named/zones/templates', 0775)

if not os.path.isfile('/var/named/etc/namedb/client_zones/zones.include'):
    f = open('/var/named/etc/namedb/client_zones/zones.include', 'w')
    f.write('')
    f.close()

zonefile_in = 'zones/master/main.internal.zone.db.tpl'
zonefile_out = ('zones/master/%s.internal.zone.db' %(domain))
zonefile_prd = ('/var/named/zones/master/%s.internal.zone.db' %(domain))

rev_zone_in = 'zones/templates/rev.in-addr.tpl'
rev_zone_out = '/var/named/zones/templates/rev.in-addr.tpl'
def make_conf( template_in, template_out, ipaddr=''):
    copy( template_in,template_out )
    f = io.open( template_out, "w" )
    for line in io.open( template_in, "r" ):
        if '$domain' in line:
            line = line.replace('$domain', domain)
            f.write(line)
        if '$ipaddr' in line:
            line = line.replace('$ipaddr', ipaddr)
            f.write(line)
        if not domain in line:
            f.write(line)
    f.close()

try:
    make_conf(template_in='named.conf.tpl', template_out='named.conf' )
except Exception, err:
    print err

copy('named.conf', '/etc/named.conf')

try:
    make_conf(template_in=zonefile_in, template_out=zonefile_out, ipaddr=ipaddr )
except Exception,err:
    print err
    
copy(zonefile_out, zonefile_prd)

try:
    make_conf(template_in=rev_zone_in, template_out=rev_zone_out )
except Exception,err:
    print err



