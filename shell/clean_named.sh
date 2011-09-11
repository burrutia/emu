#!/bin/bash
###
# i'll enventually fix this in python
#  for now its a simple hack
###
ZONEDIR='/var/named/zones/master'
cd $ZONEDIR &&  for zone in $(/bin/ls |/bin/grep in-addr.arpa);do echo $zone; /bin/sed -i  -e '/^$/d' $zone; done
/bin/sed -i  -e '/^$/d' ${ZONEDIR}/*.internal.zone.db
