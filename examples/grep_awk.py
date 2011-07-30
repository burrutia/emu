#!/usr/bin/python
# example usage for unix_util module

import os, sys, string, re
sys.path.append("/home/control/modules")
from unix_util import shell_utils
from ec2_cluster import conn

a = shell_utils()
rstatus = 'running'
e = len(conn.get_all_instances())
rs = conn.get_all_instances()
for x in range(e):
    r = rs[x]
    s = r.groups[0]
    i = r.instances[0]
    if rstatus in i.state:
        position = int(1)
        unicode_dnsname = i.private_dns_name
        string_dnsname = str(unicode_dnsname)
        ipaddr_tmp = string_dnsname.replace('-', '.')
        ip_match = re.compile('[0-9]{2}.[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}')
        ip_string = ip_match.findall(ipaddr_tmp)
        ip = ip_string[0]
        fqdn = a.host(object=i.state, ip=ip)
        shorthostname = a.cut(object=fqdn, delimeter='.', position=position)
        print "%s %s %s %s %s %s" %(s.id, i.dns_name, i.private_dns_name, ip, shorthostname, i.state)
    if not rstatus in i.state:
        print "%s %s %s %s " %(s.id, i.dns_name, i.private_dns_name, i.state)