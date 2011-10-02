class qa_user2_key_dir {
  file { ["/etc/ssh/keys/qa_user2"]:
     mode => "0755",
     owner => "root",
     group => "root",
     ensure => directory
   }
}

class qa_user1_key_dir {
  file { ["/etc/ssh/keys/qa_user1"]:
     mode => "0755",
     owner => "root",
     group => "root",
     ensure => directory
   }
}

