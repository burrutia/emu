# resolv.conf
class resolv_conf {
    file {"/etc/resolv.conf":
    owner => "root",
    group => "root",
    mode => "0644",
    content => template("/etc/puppet/manifests/templates/all/etc/resolv.conf") 
    }
}
