class qa_user1_account {
  include user::qa_user1
  include qa_user1_key_dir
  include qa_user1_ssh_key
}
class qa_user2_account {
  include user::qa_user2
  include qa_user2_key_dir
  include qa_user2_ssh_key
}
