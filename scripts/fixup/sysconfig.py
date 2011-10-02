#!/usr/bin/python
import os, re, string, subprocess, sys
import optparse
def controller():
    global VERBOSE
    p = optparse.OptionParser()
    global options
    global hostname
    global secgroup
    global inst_type
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

hostname_etc = ("%s:/etc/" %( hostname ))
script_base = '/home/emu/scripts/fixup'
sysconfig_file = '/home/emu/scripts/fixup/puppet'
sysconf_dir = '/etc/sysconfig/'
resolv_cnf = '/etc/resolv.conf'
cron_file = '/home/emu/scripts/fixup/root'
cron_dir = '/var/spool/cron/'

hostname_sysconfig_path = ("%s:%s" %( hostname, sysconf_dir ))
hostname_cron_path = ("%s:%s" %( hostname, cron_dir ))

root_pemkey_args = "'ssh -i /root/.ssh/id_dsa.pub -oPermitLocalCommand=yes'"
set_puppet_target = ("/usr/bin/rsync -ave %s %s %s" %( root_pemkey_args, sysconfig_file, hostname_sysconfig_path ))
set_puppet_crontab =  ("/usr/bin/rsync -ave %s %s %s" %( root_pemkey_args, cron_file, hostname_cron_path ))
set_resolv_conf = ("/usr/bin/rsync -ave %s %s %s" %( root_pemkey_args, resolv_cnf, hostname_etc ))

subprocess.Popen( set_puppet_target, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).communicate()[0]
subprocess.Popen( set_puppet_crontab, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).communicate()[0]
subprocess.Popen( set_resolv_conf, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).communicate()[0]
