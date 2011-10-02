#!/bin/bash
# simple script to clean out blank lines
# from dns zone files
pushd /var/named/zones/master
 for file in $(/bin/ls |/bin/grep in-addr.arpa);do
  /bin/sed -i  -e '/^$/d' $file
 done
/bin/sed -i  -e '/^$/d' /var/named/zones/master/*.internal.zone.db
if [ $? -ne 0 ]
  then
  echo "Warning exit status not 0"
fi
popd
