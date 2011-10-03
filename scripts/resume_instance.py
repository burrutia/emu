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
import optparse, sys
import subprocess

config_file ='/etc/datacenter.ini'

config = ConfigParser.ConfigParser()
config.readfp(open(config_file))
basedir = config.get('master-conf','basedir')
mdir = ('%s/modules' %(basedir))
sys.path.append(mdir)

cluster_file = '/etc/cluster.ini'
cluster_config = ConfigParser.ConfigParser()
cluster_config.readfp(open(cluster_file))

cconfig_file = ( '/etc/config.ini' )
cconfig = ConfigParser.ConfigParser()
cconfig.readfp(open(cconfig_file))

aws_keypair = cconfig.get('cluster', 'puppetkey')
bizunit = config.get('master-conf','unit')
env = config.get('master-conf','env')
domain = bizunit + env

import emu
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

inst = ConfigParser.ConfigParser()
inst.readfp(open(hostname_ini))
my_inst  = inst.get(hostname,'instance_id')

hostname_ini_dir = ('%s/host_ini' %(basedir))
hostname_ini = ("%s/%s.ini" %( hostname_ini_dir, hostname ))
print "Starting instance %s" %(my_inst)

try:
    conn.start_instances(my_inst)
except Exception, err:
    print err

dns_lock = ("/tmp/dns.lock")

if os.path.isfile(dns_lock):
    print "Sleeping on Dns Lock file"
    time.sleep(40)

if not os.path.exists(dns_lock):
    open(dns_lock, 'w').close()

from dns import EC2_Dns
from emu import EC2_info

dns = EC2_Dns()
ec2_info = EC2_info()

try:
    ipaddr = str(ec2_info.get_instip_by_id(my_inst))
    dns.write_ptr_record(ipaddr, hostname, domain )
except Exception, err:
    print err

try:
    dns.write_zone_entry()
except Exception, err:
    print err

try:
    dns.write_a_record(ipaddr, hostname, domain)
except Exception, err:
    print err

try:
    dns.clean_files()
except Exception, err:
    print err

try:
    dns.restart_named()
except Exception, err:
    print err

fqdn = ("%s.%s.internal" %( hostname, domain ))
subprocess.call(['/usr/bin/sudo', '/home/emu/scripts/tpl/sysconfig.py', '-H', fqdn],shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
getoutput("/usr/bin/python %s/scripts/agent/agent_resume.py -H %s.%s.internal" %( basedir, hostname, domain ))
