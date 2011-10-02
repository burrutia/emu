#!/usr/bin/python
# Copyright (c) 2011 Brian Urrutia <burrutia.biz@gmail.com> http://github.org/burrutia/emu
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
import os, re, string, ConfigParser
import sys
from shutil import *
import time
import fileinput
import IPy
from IPy import IP
import subprocess

config_file ='/etc/datacenter.ini'
config = ConfigParser.ConfigParser()
config.readfp(open(config_file))
basedir = config.get('master-conf','basedir')

class EC2_Dns(object):
    def __init__(self):
        self.object = object

    def backup_zone(self, object):
        """ 
        This will be a method to backup all dns data
        before each edit
        """
        self.bkup_date = bkup_date

    def rev_ip(self, ipaddr):
        self.ipaddr = ipaddr
        ip = IP(ipaddr)
        rev_zone = ip.reverseNames()
        for item in rev_zone:
            m = item.split(".")
            a = m[0]
            b = m[1]
            c = m[2]
            d = m[3]
            zone_name = ("%s.%s.%s.in-addr.arpa" %(b,c,d))
            self.zone_name = zone_name

    def a_seg(self, ipaddr ):
        ip = IP(ipaddr)
        rev_zone = ip.reverseNames()
        for item in rev_zone:
            m = item.split(".")
            a = m[0]
            self.a = a

    def t_out(self):
        template_out = ("%s/scripts/dns/workspace/%s" %(basedir, self.zone_name))
        self.template_out = template_out

    def p_zone(self):
        previous_zone = ("/var/named/zones/master/%s" %(self.zone_name))
        self.previous_zone =  previous_zone

    def prepare_conf(self, domain ):
        bind_conf = '/etc/named.conf'
        named_conf_tpl = ('%s/scripts/dns/workspace/named.conf' %(basedir))
        forward_zone = ('/var/named/zones/master/%s.internal.zone.db' %(domain))
        forward_zone_tpl = ('%s/scripts/dns/workspace/%s.internal.zone.db' %(basedir, domain))
        self.bind_conf = bind_conf
        self.named_conf_tpl = named_conf_tpl
        self.forward_zone = forward_zone
        self.forward_zone_tpl = forward_zone_tpl
        self.fzf = forward_zone
        self.fzn = forward_zone_tpl
        copy(self.forward_zone, self.forward_zone_tpl)

    def clean_zone(self, zone_file, zone_file_new, domain, thostname):
        self.prepare_conf( domain )
        f = open(zone_file, "r")
        g = open(zone_file_new, "w")
        for line in f:
            if thostname in line:
               print "omiting %s from %s" %(thostname, zone_file)
            if not thostname in line:
                print >> g, '%s' %(line)
        f.close()
        g.close()
        copy(self.fzn, self.fzf)

    def get_all_zfname(self, domain, thostname, ipaddr):
        self.rev_ip(ipaddr)
        print self.zone_name
        self.a_seg(ipaddr)
        print self.a
        self.p_zone()
        print self.previous_zone
        self.t_out()
        ## end changes
        zfname = 'in-addr.arpa'
        dirList=os.listdir('/var/named/zones/master')
        for rzf in dirList:
            print rzf
            if zfname in rzf:
                rzn = ("%s.NEW.txt" %(rzf))
                rzffile = ("/var/named/zones/master/%s" %(rzf))
                rznfile = ("%s/scripts/dns/workspace/%s" %( basedir, rzn ))
                self.clean_zone( rzffile, rznfile, domain, thostname )
                copy(rznfile,rzffile)

    def write_zone_entry(self):
        copy(self.bind_conf, self.named_conf_tpl)
        fileHandle = open ( self.bind_conf, 'r' )
	text = fileHandle.read()
	bind_conf_tpl = ('%s/scripts/dns/workspace/%s.zone' %( basedir, self.zone_name ))
        zone_file = text.find( self.zone_name )

        if zone_file > -1:
            print self.zone_name, "****Found at Index****", zone_file
        elif zone_file == -1:
            print "entry not in named.conf appending to %s" %(self.named_conf_tpl)
            new_zone_file = open(self.named_conf_tpl, 'a')
            print >> new_zone_file, '        zone "%s" {' %(self.zone_name)
            print >> new_zone_file, '            type master;'
            print >> new_zone_file, '            file "zones/master/%s";' %(self.zone_name)
            print >> new_zone_file, '        };'
            new_zone_file.close()
        fileHandle.close()
        copy(self.named_conf_tpl, self.bind_conf)

    def clean_files(self):
        subprocess.Popen( "%s/shell/clean_named.sh" %(basedir), shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).communicate()[0]

    def restart_named(self):
        named_restart = subprocess.Popen( "/etc/init.d/named restart", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).communicate()[0]
        print named_restart

    def set_fserialdate(self ):
        fileHandle = open ( self.template_out, "r" )
        regex = re.compile(r'\d{10}')
       
        for line in fileHandle:
            pattern = regex.findall(line)
            for zmatch in pattern:
                date = int(zmatch)
                ndate = date + 1
                print ndate
       
        fileHandle.close()
        
        print "Updated %s" %(self.template_out)
        
        sndate = str(ndate)
        print "serial date is %s" %(sndate)
        for line in fileinput.input(self.template_out, inplace=1):
            if zmatch in line:
                line = line.replace(zmatch, sndate)
            sys.stdout.write(line)

    def write_ptr_record(self, ipaddr, thostname, domain):
        self.get_all_zfname(domain, thostname, ipaddr)
        if os.path.isfile(self.previous_zone):
            template_in = ("/var/named/zones/master/%s" %(self.zone_name))
        if not os.path.exists(self.previous_zone):
            template_in = '%s/scripts/dns/workspace/rev.in-addr.arpa.tpl' %(basedir)

        copy(template_in,self.template_out)
        fileHandle = open ( self.template_out, 'a' )
        fileHandle.write ( '%s\t\tIN\tPTR\t%s.%s.internal.\n' %(self.a, thostname, domain) )
        fileHandle.close()
	self.set_fserialdate()
        copy(self.template_out, '/var/named/zones/master/')


    def write_a_record(self, ipaddr, thostname, domain ):
        self.clean_zone(self.forward_zone, self.forward_zone_tpl, domain, thostname )
        fileHandle = open ( self.forward_zone_tpl, 'a')
        print "opening %s" %(self.forward_zone_tpl)
        print "%s\t\tIN\tA\t%s\n" %(thostname,ipaddr)
        fileHandle.write ( '%s\t\tIN\tA\t%s\n' %(thostname,ipaddr))
        fileHandle.close()
        target_zone = ("/var/named/zones/master/%s" %(self.zone_name))
        copy(self.forward_zone_tpl, self.forward_zone)

    def sync_named(self):
        subprocess.call(['/usr/bin/sudo','/scripts/sync_named.sh'],shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
