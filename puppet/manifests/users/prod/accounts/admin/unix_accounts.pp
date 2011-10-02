# accounts template
class unix_user1_account {
  include unix_user1_key_dir
  include unix_user1_ssh_key
  include user::unix_user1
}

class unix_user4_account {
  include user::unix_user4
  include unix_user4_key_dir
  include unix_user4_ssh_key
}

class unix_user2_account {
  include user::unix_user2
  include unix_user2_key_dir 
  include unix_user2_ssh_key
}

class unix_user3_account {
  include user::unix_user3
  include unix_user3_key_dir 
  include unix_user3_ssh_key
}
