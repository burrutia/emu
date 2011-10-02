# place holder for unix admin keys

class unix_user1_ssh_key {
 file { "/etc/ssh/keys/unix_user1/authorized_keys2":
    ensure => present,
    mode => 644,
    owner => root,
    group => root,
    content => template ("/etc/puppet/manifests/users/unix/unix_user1/authorized_keys2")
    }
}

class unix_user4_ssh_key {
 file { "/etc/ssh/keys/unix_user4/authorized_keys2":
    ensure => present,
    mode => 644,
    owner => root,
    group => root,
    content => template ("/etc/puppet/manifests/users/unix/unix_user4/authorized_keys2")
 }
}

class unix_user2_ssh_key {
 file { "/etc/ssh/keys/unix_user2/authorized_keys2":
    ensure => present,
    mode => 644,
    owner => root,
    group => root,
    content => template ("/etc/puppet/manifests/users/unix/unix_user2/authorized_keys2")
 }
}

class unix_user3_ssh_key {
 file { "/etc/ssh/keys/unix_user3/authorized_keys2":
    ensure => present,
    mode => 644,
    owner => root,
    group => root,
    content => template ("/etc/puppet/manifests/users/unix/unix_user3/authorized_keys2")
 }
}
