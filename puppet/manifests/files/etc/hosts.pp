# resolv.conf
class hosts_file  {
    file {"/etc/hosts":
    owner => "root",
    group => "root",
    mode => "0644",
    content => template("/etc/puppet/manifests/templates/all/etc/hosts") 
    }
}
