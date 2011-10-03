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
import string, sys, ConfigParser
import optparse

cconfig_file ='/etc/config.ini'
cconfig = ConfigParser.ConfigParser()
cconfig.readfp(open(cconfig_file))

image = cconfig.get('baseimage','ami')
aws_keypair = cconfig.get('cluster', 'puppetkey')
cluster = cconfig.get('cluster','env')

config_file ='/etc/datacenter.ini'

config = ConfigParser.ConfigParser()
config.readfp(open(config_file))
basedir = config.get('master-conf','basedir')
mdir = ('%s/modules' %(basedir))
sys.path.append(mdir)

from emu import conn

def controller():
    p = optparse.OptionParser()
    global options
    global hostname
    p.add_option('--hostname','-H', action="store", type="string", help="target hostname")

    options, arguments = p.parse_args()
    if options.hostname:
        hostname = options.hostname
    else:
        p.print_help()

def main():
    controller()

if __name__ == '__main__':
    main()

thishost = getoutput("/bin/hostname")

if thishost in hostname:
    print "--------------------------------------------------------------------"
    print "Please, Do not attempt to shutdown THIS host!"
    print "Please check the host you would like to shutdown and try again!"
    print "--------------------------------------------------------------------"
    print ""
    print "Have a nice day!"
    sys.exit(2)

hostname_ini_dir = ('%s/host_ini' %(basedir))
hostname_ini = ("%s/%s.ini" %( hostname_ini_dir, hostname ))

inst = ConfigParser.ConfigParser()
inst.readfp(open(hostname_ini))

instance_id  = inst.get(hostname,'instance_id')

try:
    conn.stop_instances(instance_id)
except Exception, err:
    print err

print "Done"
