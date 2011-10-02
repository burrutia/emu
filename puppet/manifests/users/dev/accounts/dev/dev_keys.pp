# place holder for unix dev keys
class dev_user2_ssh_key {
 file { "/etc/ssh/keys/dev_user2/authorized_keys2":
    ensure => present,
    mode => 644,
    owner => root,
    group => root,
    content => template ("/etc/puppet/manifests/users/dev/dev_user2/authorized_keys2"),
    }
}

class dev_user1_ssh_key {
 file { "/etc/ssh/keys/dev_user1/authorized_keys2":
    ensure => present,
    mode => 644,
    owner => root,
    group => root,
    content => template ("/etc/puppet/manifests/users/dev/dev_user1/authorized_keys2"),
    }
}
