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

import os, re, string, subprocess, sys
import optparse

def controller():
    p = optparse.OptionParser()
    global options
    global hostname
    p.add_option('--hostname','-H', action="store", type="string", help="target hostname")

    options, arguments = p.parse_args()
    if options.hostname:
         print "Hostname is %s" %(options.hostname)
    else:
        p.print_help()

def main():
    controller()

if __name__ == '__main__':
    main()

hostname = options.hostname

dsa_key_arg = "'ssh -i /root/.ssh/id_dsa -oPermitLocalCommand=yes'"

script_base = '/home/emu/scripts/fixup'
sconfig_file = '/home/emu/scripts/fixup/puppet'
sudoers_file = '/home/emu/scripts/fixup/sudoers'
crond_target = '/home/emu/scripts/fixup/root'

sysconf_dir = '/etc/sysconfig/'
resolv_cnf = '/etc/resolv.conf'
cron_dir = '/var/spool/cron/'

hostname_etc = ("%s:/etc/" %( hostname ))
host_sys_path = ("%s:%s" %( hostname, sysconf_dir ))
host_cron_path = ("%s:%s" %( hostname, cron_dir ))

set_target = ("/usr/bin/rsync -ave %s %s %s" %( dsa_key_arg, sconfig_file, host_sys_path ))
set_sudoers = ("/usr/bin/rsync -ave %s %s %s" %( dsa_key_arg, sudoers_file, hostname_etc ))
set_crontab =  ("/usr/bin/rsync -ave %s %s %s" %( dsa_key_arg, crond_target, host_cron_path ))
set_resolv_conf = ("/usr/bin/rsync -ave %s %s %s" %( dsa_key_arg, resolv_cnf, hostname_etc ))

subprocess.Popen( set_target, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).communicate()[0]
subprocess.Popen( set_sudoers, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).communicate()[0]
subprocess.Popen( set_crontab, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).communicate()[0]
subprocess.Popen( set_resolv_conf, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).communicate()[0]
