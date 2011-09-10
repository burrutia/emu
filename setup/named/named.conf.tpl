//
// See the BIND Administrator's Reference Manual (ARM) for details, in:
//   file:///usr/share/doc/bind-*/arm/Bv9ARM.html
// Also see the BIND Configuration GUI : /usr/bin/system-config-bind and 
// its manual.
//
options
{
        directory "/var/named"; // the default
        dump-file               "data/cache_dump.db";
        statistics-file         "data/named_stats.txt";
        memstatistics-file      "data/named_mem_stats.txt";
        allow-recursion { any; };

};
        include "/etc/named.root.hints";

        include "/etc/named.rfc1912.zones";
        include "/var/named/etc/namedb/client_zones/zones.include";

        zone "${BIZUNIT}${ENV}.internal" {
                type master;
                file "zones/master/${BIZUNIT}${ENV}.internal.zone.db";
        };
