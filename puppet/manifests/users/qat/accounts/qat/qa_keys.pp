# place holder for qat admin keys
# /etc/puppet/manifests/class/users/qat/
class qa_user2_ssh_key {
 file { "/etc/ssh/keys/qa_user2/authorized_keys2":
    ensure => present,
    mode => 644,
    owner => root,
    group => root,
    content => template ("/etc/puppet/manifests/users/qat/qa_user2/authorized_keys2")
    }
}

class qa_user1_ssh_key {
 file { "/etc/ssh/keys/qa_user1/authorized_keys2":
    ensure => present,
    mode => 644,
    owner => root,
    group => root,
    content => template ("/etc/puppet/manifests/users/qat/qa_user1/authorized_keys2")
 }
}

