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
import os, string, sys
import optparse, ConfigParser
import fileinput

config_file ='/etc/datacenter.ini'

config = ConfigParser.ConfigParser()
config.readfp(open(config_file))
basedir = config.get('master-conf','basedir')

host_ini_dir = ('%s/host_ini' %(basedir) )

def controller():
    p = optparse.OptionParser()
    global options
    global hostname
    global inst_id
    p.add_option('--hostname','-H', action="store", type="string", help="target hostname")
    p.add_option('--inst_id','-i', action="store", type="string", help="target hostname")

    options, arguments = p.parse_args()
    if options.hostname:
        hostname = options.hostname
    else:
        p.print_help()

def main():
    controller()

if __name__ == '__main__':
    main()

inst_id = options.inst_id
hostname_ini = ("%s/%s.ini" %( host_ini_dir, hostname ))
fileHandle = open ( hostname_ini, 'w' )
print >> fileHandle, '[%s]' %(hostname)
print >> fileHandle, 'instance_id = %s' %(inst_id)
fileHandle.close()
