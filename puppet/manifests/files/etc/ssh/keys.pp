class ssh_config
{
 include ssh_server
 include ssh_key_dir
 include sshd_config
}

class ssh_key_dir 
{
   file {["/etc/ssh/keys"]:
     mode => "0755",
     owner => "root",
     group => "root",
     ensure => directory
    }
}

class sshd_config
{
 file{ "/etc/ssh/sshd_config":
   owner=> "root",
   group => "root",
   mode => 0600,
   notify => Service[sshd],
   content =>template("/etc/puppet/manifests/templates/all/etc/ssh/sshd_config")
 }
}
