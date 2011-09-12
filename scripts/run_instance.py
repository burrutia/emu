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
import os, re, string, ConfigParser, sys, boto.ec2

config_file ='/etc/datacenter.ini'

config = ConfigParser.ConfigParser()
config.readfp(open(config_file))
basedir = config.get('master-conf','basedir')
mdir = ('%s/modules' %(basedir))
sys.path.append(mdir)

from shutil import *
import time
import optparse
import fileinput
import IPy
from IPy import IP
import subprocess

cluster_file = '/etc/cluster.ini'
cluster_config = ConfigParser.ConfigParser()
cluster_config.readfp(open(cluster_file))

cconfig_file = ( '%s/conf/config.ini' %(basedir)
cconfig = ConfigParser.ConfigParser()
cconfig.readfp(open(cconfig_file))

image = cconfig.get('baseimage','ami')

"""
Name of key set via awsconsole or other tools
"""
aws_keypair = 'puppetkey'


ccluster = config.get('cluster','env')

import emu
from emu import conn


def controller():
    global VERBOSE
    p = optparse.OptionParser()
    global options
    global hostname
    global secgroup
    p.add_option('--secgroup','-s', action="store", type="string", help="Security Group")
    p.add_option('--hostname','-H', action="store", type="string", help="target hostname")
    p.add_option('--verbose', '-v', action = 'store_true', help='prints verbosely', default=False)

    options, arguments = p.parse_args()
    if options.verbose:
        VERBOSE=True
    if options.hostname:
        VERBOSE=False
    else:
        p.print_help()

def main():
    controller()

if __name__ == '__main__':
    main()

from  commands import getoutput

hostname = options.hostname
thishost = getoutput("/bin/hostname")

if thishost in hostname:
    print "--------------------------------------------------------------------"
    print "Please, Do not attempt to shutdown THIS host!"
    print "Please check the host you would like to shutdown and try again!"
    print "--------------------------------------------------------------------"
    print ""
    print "Have a nice day!"
    sys.exit(2)

secgroup = options.secgroup
instance_size = cluster_config.get( secgroup, 'inst_size' )

zone = ec2_region_data.lnfoRegion(secgroup)

try:
    reservation = conn.run_instances(image, min_count=1, max_count=1, instance_type=instance_size, key_name=aws_keypair, security_groups=[secgroup], placement=zone)
except:
    print "unknown error aborting!"
    sys.exit(2)

instance = reservation.instances[0]
time.sleep(25)
while not instance.update() == 'running':
  time.sleep(15)

instance_id = str(instance)
m = instance_id.split(":")
my_inst = str(m[1])

dns_lock = ("/tmp/dns.lock")

if os.path.isfile(dns_lock):
    print "Sleeping on Dns Lock file"
    time.sleep(40)

if not os.path.exists(dns_lock):
    open(dns_lock, 'w').close()

dns = EC2_Dns()

try:
    ipaddr = str(emu.get_instip_by_id(my_inst))
    dns.write_ptr_record(ipaddr, hostname, domain )
except Exception, err:
    print err

try:
    dns.write_zone_entry()
except Exception, err:
    print err

try:
    dns.write_a_record(ipaddr, hostname)
except Exception, err:
    print err


try:
    dns.clean_files()
except Exception, err:
    print err

print "sleeping to allow host to come up"
time.sleep(65)

fqdn = ("%s.%s.internal" %(hostname, domain))

subprocess.call(['/usr/bin/sudo', '/usr/sbin/puppetca', '--clean', fqdn],shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
subprocess.call(['/usr/bin/sudo','/scripts/sysconfig.py', '-H', fqdn],shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
agent_cmd = ("/usr/bin/python %s/scripts/agent/agent_fixup.py -H %s.%s.internal" % ( basedir, hostname, domain ))
subprocess.Popen( agent_cmd , shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).communicate()[0]

print "Calling puppetca to see if we have a cert request"
chk_puppet_req =  subprocess.Popen( "/usr/bin/sudo /usr/sbin/puppetca --list", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).communicate()[0]

count = 0
while (count < 10):
    print "count is:", count
    count = count +1
    time.sleep(5)
    print chk_puppet_req
    if hostname in chk_puppet_req:
        fqdn = ("%s.%s.internal" %( hostname, domain ))
        print "found %s signing cert" %( fqdn )
        time.sleep(5)
        break
    if not hostname in chk_puppet_req:
        print "Host not found attempting to fix"
        root_pemkey = '/home/control/ec2/keys/id_puppetkey'
        fqdn = ("%s.%s.internal" %( hostname, domain ))
        subprocess.Popen(['/usr/bin/ssh', '-i', root_pemkey, '-l', 'root', fqdn, '/etc/init.d/syslog', 'restart' ],shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        getoutput("/usr/bin/python /home/control/scripts/agent/agent_fixup.py -H %s.%s.internal" %(hostname, domain))
        time.sleep(10)

getoutput("/usr/bin/sudo /usr/sbin/puppetca --sign %s" %(fqdn))

subprocess.call(['/usr/bin/sudo', '/scripts/clean_named.sh'],shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
subprocess.call(['/home/control/scripts/bin/make_ini.py', '-H', hostname],shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
os.remove(dns_lock)
