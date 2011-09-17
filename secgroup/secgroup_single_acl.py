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
# 
import boto.ec2
import string, sys, os, optparse
import ConfigParser

config_file ='/etc/datacenter.ini'
config = ConfigParser.ConfigParser()
config.readfp(open(config_file))

basedir = config.get('master-conf','basedir')
mdir = ('%s/modules' %(basedir))
sys.path.append(mdir)

cconfig_file = ( '%s/conf/config.ini' %(basedir) )
cconfig = ConfigParser.ConfigParser()
cconfig.readfp(open(cconfig_file))

userid = cconfig.get('aws_creds', 'aws_userid')

from emu import conn

def controller():
    global VERBOSE
    p = optparse.OptionParser()
    global options
    global tsecgroup
    global dsecgroup
    p.add_option('--tsecgroup','-t', action="store", type="string", help="target security group")
    p.add_option('--dsecgroup','-d', action="store", type="string", help="destination secgroup")
    p.add_option('--verbose', '-v', action = 'store_true', help='prints verbosely', default=False)

    options, arguments = p.parse_args()
    if options.verbose:
        VERBOSE=True
    if options.tsecgroup:
        VERBOSE=False
    else:
        p.print_help()

def main():
    controller()

if __name__ == '__main__':
    main()


tsecgroup = options.tsecgroup
dsecgroup = options.dsecgroup

def modify_acl():
        try:
            conn.authorize_security_group(tsecgroup,dsecgroup,userid)
        except:
            print "secgroup has already been added"

modify_acl()
