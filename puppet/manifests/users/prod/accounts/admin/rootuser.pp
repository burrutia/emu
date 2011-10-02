# user virtual class for unix group
#class user::suuser {
class root_account {
    user { 'root':
    ensure => 'present',
    name => 'root',
    groups => ['root','bin','daemon','sys','adm','disk','wheel'],
    uid => '0',
    gid => '0',
    password => '$1$SubstitueR3alH@5H3r3',
    comment => 'root',
    shell => '/bin/bash',
    home => '/root'
    }
}
