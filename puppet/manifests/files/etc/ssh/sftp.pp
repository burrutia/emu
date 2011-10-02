class sftpod {
    include sftpod_conf
    include sftpod_init
    include sftpod_bin
}

class sftpod_conf {
    file {"/etc/ssh/sftpod_config":
    owner => 'root',
    group => 'root',
    mode => 0644,
    content => template("/etc/puppet/manifests/templates/sft/sshd/sftpod_config")
    }
}


class sftpod_init {
    file {"/etc/init.d/sftpod":
    owner => 'root',
    group => 'root',
    mode => 0755,
    content => template("/etc/puppet/manifests/templates/sft/init.d/sftpod")
    }
}


class sftpod_bin {
   file {"/usr/sbin/sftpod":
   ensure => link,
   target => "/usr/sbin/sshd",
   }
}

