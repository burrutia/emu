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
import commands
import os, sys, re, string
import optparse

dsa_key = "-i /root/.ssh/id_dsa"

def controller():
    global VERBOSE
    p = optparse.OptionParser()
    global options
    global fqdn_host 
    p.add_option('--fqdn_host','-H', action="store", type="string", help="fqdn hostname")

    options, arguments = p.parse_args()
    if options.fqdn_host:
        print "--------"
    else:
        p.print_help()

def main():
    controller()

if __name__ == '__main__':
    main()

fqdn_host = options.fqdn_host

h = re.compile("\.").split(fqdn_host)
hostname =h[0]
domainname =  ("%s.%s" %(h[1], h[2]))
print "Hostname is %s" %(hostname)
print "Domainname is %s" %(domainname)
print "Setting domainname"
set_domain = commands.getoutput("/usr/bin/ssh %s %s.%s '/usr/bin/sudo  /bin/domainname %s;exit'" %( dsa_key, hostname, domainname, domainname ))
set_hostname = commands.getoutput("/usr/bin/ssh %s  %s.%s '/usr/bin/sudo  /bin/hostname %s;exit'" %( dsa_key, hostname, domainname, hostname ))
clear_oldcert = commands.getoutput("/usr/bin/ssh %s %s.%s '/usr/bin/sudo find /var/lib/puppet -name *.pem -exec rm -f '{}' +'")
restart_syslog = commands.getoutput("/usr/bin/ssh %s %s.%s '/usr/bin/sudo /etc/init.d/*syslog* restart'" %( dsa_key, hostname, domainname ))
start_puppet = commands.getoutput("/usr/bin/ssh %s %s.%s '/usr/bin/sudo /etc/init.d/puppet restart'" %( dsa_key, hostname, domainname ))

try:
    print set_domain
    print set_hostname
    print clear_oldcert
    print restart_syslog
    print restart_syslog
    print start_puppet
except ValueError:
    print "oops error can't change hostname domainame check tty setting on sudoers"
