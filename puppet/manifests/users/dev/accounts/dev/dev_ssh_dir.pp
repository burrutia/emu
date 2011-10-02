# unix template for sshdir
class web_user_key_dir {
  file { "/etc/ssh/keys/web_user":
   ensure => directory,
   mode => 0755,
   owner => root,
   group => root,
   }
}

class dev_user1_key_dir {
  file { "/etc/ssh/keys/dev_user1":
   mode => "0755",
   owner => "root",
   group => "root",
   ensure => directory
   }
}

class dev_user2_key_dir {
  file { "/etc/ssh/keys/dev_user2":
   mode => "0755",
   owner => "root",
   group => "root",
   ensure => directory
   }
}
