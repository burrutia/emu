# site.pp

import "accounts"
import "nodes"
import "apps"

filebucket { main: server => puppet }
$extlookup_datadir = "/etc/extlookup/puppet"
$extlookup_precedence = ["%{fqdn}", "domain_%{domain}", "common", "ganglia",  "db", "cache", "code"]
File { backup => main }
Exec { path => "/usr/bin:/usr/sbin/:/bin:/sbin" }

Package {
    provider => $operatingsystem ? {
        debian => aptitude,
        redhat => yum,
        Linux  => yum,
        CentOS => yum
    }
}
