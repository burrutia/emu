# gitosis conf and parent dir
class gitosis_configs
{
 include gitosis_pdirs
 include gitosis_expkey
 include projects_list
 include gitosis_conf
}

class gitosis_pdirs
{
  $git_base = "/home/git"
   file{["$git_base","$git_base/repositories","$git_base/repositories/gitosis-admin.git","$git_base/gitosis",
         "$git_base/repositories/gitosis-admin.git/gitosis-export"]:
          mode => "0755",
          owner => "git",
          group => "git",
          ensure => directory,
          recurse => true
       }
}

class gitosis_conf
{
 file {"/home/git/repositories/gitosis-admin.git/gitosis.conf":
   owner => "git",
   group => "git",
   mode => "0644",
   content => template("/etc/puppet/manifests/class/git/overlay/home/git/repositories/gitosis-admin.git/gitosis.conf")
   }
}

class gitosis_conflink
{
 file {"/home/git/.gitosis.conf":
 ensure => link,
 target => "/home/git/repositories/gitosis-admin.git/gitosis.conf",
 }
}

class projects_list
{
 file{"/home/git/gitosis/projects.list":
  owner => "git",
  group => "git",
  mode => "0644",
  content => template("/etc/puppet/manifests/class/git/overlay/home/git/gitosis/projects.list")
 }
}


class gitosis_expkey
{
 file { "/home/git/repositories/gitosis-admin.git/gitosis-export/keydir":
  owner => "git",
  group => "git",
  purge => true,
  recurse => true,
  force => true,
  source => "puppet:///files/git/overlay/home/git/repositories/gitosis-admin.git/gitosis-export/keydir"
  }
}
