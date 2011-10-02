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

import os, sys, re, string, ConfigParser
import boto.ec2

config_file ='/etc/datacenter.ini'
config = ConfigParser.ConfigParser()
config.readfp(open(config_file))
basedir = config.get('master-conf','basedir')
#cconfig_file = ('%s/conf/config.ini' %(basedir))
cconfig_file = ('/etc/config.ini')
cconfig = ConfigParser.ConfigParser()
cconfig.readfp(open(cconfig_file))

AWS_ACCESS_KEY_ID = cconfig.get('aws_creds', 'aws_access_key')
AWS_SECRET_ACCESS_KEY = cconfig.get('aws_creds', 'aws_secret_key')
AWS_REGION_NUMBER = cconfig.get('aws_creds', 'region')

curr_endpoint = cconfig.get("aws_creds","regioninfo")

regions = boto.ec2.regions(aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
i = int(AWS_REGION_NUMBER)

curr_region = regions[i]
conn =  boto.connect_ec2(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)
conn = boto.ec2.connect_to_region(curr_endpoint,aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY)

e = len(conn.get_all_instances())
rs = conn.get_all_instances()

class EC2_info:
    def __init__(self, cmd=None, count=None, node_info=None, images=None ):
        self.command = cmd
        self.count = count
        self.instances = []

    def get_node_info(self):
        node_info = conn.get_all_instances()

    def get_image_list(self):
        images = conn.get_all_images()
        for image in images:
            print "%s" %(image)


    def get_instances(self, instances, secgroup=""):
        for nodes in conn.get_all_instances(secgroup):
          self.instances.extend(nodes.instances)

    def get_instance_info(self, secgroup=""):
        
	""" EC2_info.get_cluster_info('secgroup_name') 
	 or EC2_info.get_cluster_info() for all """

        self.get_instances(self)
        for node in self.instances:
            print "%s %s %s %s %s" %( node.id, node.dns_name, node.ip_address, node.private_ip_address, node.state)
    
    def get_cluster_info(self, cluster=""):
        for x in range(e):
            r = rs[x]
            s = r.groups[0]
            i = r.instances[0]
            rows = ("%s %s %s %s" %(s.id, i.dns_name, i.private_dns_name, i.state))
            lines = rows.split("\n")
            for line in lines:
                if cluster in line:
                    print "%s" %(line)
    
    def get_clustered_region_info(self, cluster=""):
        for x in range(e):
            r = rs[x]
            s = r.groups[0]
            i = r.instances[0]
            rows = ("%s %s %s %s %s" %(s.id, i.dns_name, i.private_dns_name, i.state, i.placement ))
            lines = rows.split("\n")
            for line in lines:
                if cluster in line:
                    print "%s" %(line)
    
    def get_cluster_node_count(self, cluster=""):
        count = 0
        for x in range(e):
            r = rs[x]
            s = r.groups[0]
            i = r.instances[0]
            rows = ("%s %s %s %s" %(s.id, i.dns_name, i.private_dns_name, i.state))
            lines = rows.split("\n")
            for line in lines:
                if cluster in line:
                    print "%s" %(line)
                    count = count+1
     
        return count
    
    def get_image_list(self):
        i = self.get_image_list()
        return i
    
    
    def get_instance_by_secgroup(self, secgroup=""):
        for nodes in conn.get_all_instances():
            self.instances.extend(nodes.instances)
        for node in self.instances:
            print "%s %s %s %s %s %s" %( node.id, node.dns_name, node.ip_address, node.private_ip_address, node.state, node.placement)
    
    
    def get_instance_by_secgroup_private(self, secgroup=""):
        from commands import getoutput
        rstatus = 'running'
        for nodes in conn.get_all_instances():
            self.instances.extend(nodes.instances)
        for node in self.instances:
            if rstatus in node.state:
                h = getoutput("/usr/bin/host %s |/bin/awk '{print $5}' |/bin/cut -d '.' -f1" %(node.private_ip_address))
                print "%s %s %s %s %s %s %s" %( node.id, node.dns_name, node.ip_address, node.private_ip_address, h, node.state, node.placement)
            if not rstatus in node.state:
                print "%s %s %s %s %s %s" %( node.id, node.dns_name, node.ip_address, node.private_ip_address, node.state, node.placement)
    
    def get_all_private_ip(self):
        for nodes in conn.get_all_instances():
            self.instances.extend(nodes.instances)
        for node in self.instances:
            print "%s" %(node.private_ip_address)
    
    def get_instip_by_id(self, instance_id=""):
        info_inst = []
        check_instance_id = False
        if len(instance_id) > 0:
            check_instance_id = True
            for nodes in conn.get_all_instances(instance_id):
                self.instances.extend(nodes.instances)
                for node in self.instances:
                    return node.private_ip_address
        elif len(instance_id) == 0:
            for nodes in conn.get_all_instances():
                self.instances.extend(nodes.instances)
                for node in self.instances:
                    return node.private_ip_address
    
    def get_node_names(self):
        for nodes in conn.get_all_instances():
            self.instances.extend(nodes.instances)
            for node in self.instances:
                print "%s" %( node.dns_name )
    
    def get_security_groups(self):
        secgrp = conn.get_all_security_groups()
        for grp in secgrp:
            return grp
