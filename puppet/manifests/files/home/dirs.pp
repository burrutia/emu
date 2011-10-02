class web_user_home {
  include web_user_root
  include web_user_ssh_dir
  include web_user_ssh_config
  include wbashrc
  include wbashpfl
}

class web_user_root {
  file {"/home/web_user":
  ensure => directory,
  owner => "web_user",
  group => "web_user",
  mode => 0700,
  }
}

class wbashrc {
file {"/home/web_user/.bashrc":
  owner => "web_user",
  group => "web_user",
  mode => 0644,
  content => template("/etc/puppet/manifests/templates/all/home/web_user/bashrc")
 }
}

class wbashpfl {
file {"/home/web_user/.bash_profile":
  owner => "web_user",
  group => "web_user",
  mode => 0644,
  content => template("/etc/puppet/manifests/templates/all/home/web_user/bashpfl")
 }
}

class web_user_ssh_dir {
  file {"/home/web_user/.ssh":
   ensure => directory,
   owner => "web_user",
   group => "web_user",
   mode => 0700,
  }
}

class web_user_ssh_config {
  file {"/home/web_user/.ssh/config":
  owner => "web_user",
  group => "web_user",
  mode => 0644,
  content => template("/etc/puppet/manifests/templates/all/home/web_user/config"),
  require => File["/home/web_user/.ssh"]
  }
}
