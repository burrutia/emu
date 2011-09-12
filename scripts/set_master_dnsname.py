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
from  commands import getoutput
import os, re, string, ConfigParser
import sys
from shutil import *
import optparse
import fileinput
import IPy
from IPy import IP
import subprocess

config_file ='/etc/datacenter.ini'

config = ConfigParser.ConfigParser()
config.readfp(open(config_file))

setupdir = config.get('master-conf','setup')
basedir = config.get('master-conf','basedir')
bizunit = config.get('master-conf','unit')
env = config.get('master-conf','env')

mdir = ('%s/modules' %(basedir))

sys.path.append(mdir)

domain = bizunit + env

from dns import EC2_Dns

def controller():
    global VERBOSE
    p = optparse.OptionParser()
    global options
    global thostname
    global ipaddr
    p.add_option('--ipaddr','-i', action="store", type="string", help="ip address")
    p.add_option('--thostname','-H', action="store", type="string", help="target hostname")
    p.add_option('--verbose', '-v', action = 'store_true', help='prints verbosely', default=False)

    options, arguments = p.parse_args()
    if options.verbose:
        VERBOSE=True
    if options.ipaddr:
        VERBOSE=False
    else:
        p.print_help()

def main():
    controller()

if __name__ == '__main__':
    main()

ipaddr = options.ipaddr
thostname = options.thostname

dns = EC2_Dns()

try:
    dns.write_ptr_record(ipaddr, thostname, domain )
except Exception, err:
    print err

try:
    dns.write_zone_entry()
except Exception, err:
    print err

try:
    dns.write_a_record(ipaddr, thostname)
except Exception, err:
    print err


try:
    dns.clean_files()
except Exception, err:
    print err

