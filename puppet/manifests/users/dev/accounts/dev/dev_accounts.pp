# accounts template
# these were all suffixed with _account
class web_user_account {
  include user::web_user
}
class dev_user2_account {
  include user::dev_user2
  include dev_user2_key_dir
  include dev_user2_ssh_key
}
