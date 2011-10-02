# unix template for sshdir
class unix_user1_key_dir {
  file { ["/etc/ssh/keys/unix_user1"]:
     mode => "0755",
     owner => "root",
     group => "root",
     ensure => directory
   }
}

class unix_user4_key_dir {
  file { ["/etc/ssh/keys/unix_user4"]:
     mode => "0755",
     owner => "root",
     group => "root",
     ensure => directory
   }
}

class unix_user2_key_dir {
  file { ["/etc/ssh/keys/unix_user2"]:
     mode => "0755",
     owner => "root",
     group => "root",
     ensure => directory
   }
}

class unix_user3_key_dir {
  file { ["/etc/ssh/keys/unix_user3"]:
     mode => "0755",
     owner => "root",
     group => "root",
     ensure => directory
   }
}

